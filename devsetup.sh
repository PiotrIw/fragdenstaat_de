#!/bin/bash
set -e

# macOS's System Integrity Protection purges the environment variables controlling
# `dyld` when launching protected processes (https://developer.apple.com/library/archive/documentation/Security/Conceptual/System_Integrity_Protection_Guide/RuntimeProtections/RuntimeProtections.html#//apple_ref/doc/uid/TP40016462-CH3-SW1)
# This causes macOS to remove the DYLD_ env variables when running this script, so we have to set them again
if [ !  -z "${FRAGDENSTAAT_DYLD_LIBRARY_PATH:-}" ]; then
    export LD_LIBRARY_PATH=${FRAGDENSTAAT_DYLD_LIBRARY_PATH:-}:${LD_LIBRARY_PATH:-}
    export DYLD_LIBRARY_PATH=$LD_LIBRARY_PATH:${DYLD_LIBRARY_PATH:-}
fi

MAIN=fragdenstaat_de
REPOS=("froide" "froide-campaign" "froide-legalaction" "froide-food" "froide-payment" "froide-crowdfunding" "froide-govplan" "froide-fax" "froide-exam" "django-filingcabinet")
FRONTEND_DIR=("froide" "froide_food" "froide_exam" "froide_campaign" "froide_payment" "froide_legalaction" "filingcabinet")
FRONTEND=("froide" "froide_food" "froide_exam" "froide_campaign" "froide_payment" "froide_legalaction" "@okfde/filingcabinet")
FRONTEND_DEPS=("froide" "@okfde/filingcabinet")

ask() {
    # https://djm.me/ask
    local prompt default reply

    if [ "${2:-}" = "Y" ]; then
        prompt="Y/n"
        default=Y
    elif [ "${2:-}" = "N" ]; then
        prompt="y/N"
        default=N
    else
        prompt="y/n"
        default=
    fi

    while true; do

        # Ask the question (not using "read -p" as it uses stderr not stdout)
        echo -n "$1 [$prompt] "

        # Read the answer (use /dev/tty in case stdin is redirected from somewhere else)
        read reply </dev/tty

        # Default?
        if [ -z "$reply" ]; then
            reply=$default
        fi

        # Check if the reply is valid
        case "$reply" in
            Y*|y*) return 0 ;;
            N*|n*) return 1 ;;
        esac

    done
}

install_precommit() {
  local repo_dir="$1"
  if [ -e "$repo_dir/.pre-commit-config.yaml" ]; then
    pushd "$repo_dir"
    pre-commit install
    popd
  fi
}

venv() {
  echo "You need python >= 3.10, uv and yarn installed."

  python3 --version
  yarn --version
  uv --version

  if [ ! -d fds-env ]; then
    if ask "Do you want to create a virtual environment using $(python3 --version)?" Y; then
      echo "Creating virtual environment with uv and $(python3 --version)"
      uv venv fds-env
    fi
  fi

  if [ ! -d fds-env ]; then
    echo "Could not find virtual environment fds-env"
  fi

  source fds-env/bin/activate
}

pull() {
  echo "Cloning / installing $MAIN"

  if [ ! -d $MAIN ]; then
    git clone git@github.com:okfde/$MAIN.git
  else
    pushd $MAIN
      git pull origin "$(git branch --show-current)"
    popd
  fi

  for name in "${REPOS[@]}"; do
    if [ ! -d $name ]; then
      git clone git@github.com:okfde/$name.git
    else
      pushd $name
        git pull origin "$(git branch --show-current)"
      popd
    fi
  done
}

dependencies() {
  echo "Installing $MAIN..."

  uv pip sync $MAIN/requirements-dev.txt
  uv pip install -e $MAIN
  install_precommit "$MAIN"

  echo "Cloning / installing all editable dependencies..."

  for name in "${REPOS[@]}"; do
    uv pip uninstall $name
    uv pip install -e $name
    install_precommit "$name"
  done
}

frontend() {
  echo "Linking frontend dependencies..."

  for name in "${FRONTEND_DIR[@]}"; do
    python -c "import $name as mod; print(mod.__path__[0])"
    pushd $(python -c "import $name as mod; print(mod.__path__[0])")
    yarn link
    popd
  done

  echo "Installing frontend dependencies..."
  for name in "${FRONTEND_DIR[@]}"; do
    pushd $(python -c "import $name as mod; print(mod.__path__[0])")/..
    for dep in "${FRONTEND_DEPS[@]}"; do
      if [ "$name" != "$dep" ]; then
        yarn link $dep
      fi
    done
    yarn install
    popd
  done

  pushd $MAIN
  for name in "${FRONTEND[@]}"; do
    yarn link $name
  done
  yarn install
  popd
}

messages() {
  fds-env/bin/python fragdenstaat_de/manage.py compilemessages -l de
}

forall() {
  echo "Executing '$@' in all repos"
  pushd $MAIN
    "$@"
  popd

  for name in "${REPOS[@]}"; do
    pushd $name
      "$@"
    popd
  done
}

help() {
  echo "Available commands:"
  echo "setup: setup / update all repos"
  echo "forall: run command in all repos"
}


if [ -z "$1" ]; then
  venv
  pull
  dependencies
  frontend
  messages
  setup
  
  echo "Done!"
else
  if [[ $(type -t "$1") == function ]]; then
    "$@"
  else
    help
    exit 1
  fi
fi
