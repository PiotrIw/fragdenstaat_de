#!/bin/bash
set -e

# Pull or build containers
setup() {
  echo "Starting Docker containers..."
  docker compose -f compose-dev.yaml up -d
  echo "Containers are running."
}

# Install dependencies in the dev container
dependencies() {
  echo "Installing dependencies in the dev container..."
  docker-compose exec dev bash -c "
    uv pip install -r fragdenstaat_de/requirements-dev.txt &&
    pnpm install &&
    pnpm link --global
  "
}

# Run commands in all repos
# forall() {
#   echo "Executing '$@' in all repos..."
#   docker-compose exec dev bash -c "
#     for repo in froide froide-campaign froide-legalaction froide-food froide-payment froide-crowdfunding froide-govplan froide-fax froide-exam django-filingcabinet froide-evidencecollection; do
#       pushd /app/\$repo
#       $@
#       popd
#     done
#   "
# }

# Show help
help() {
  echo "Available commands:"
  echo "setup: Start the Docker containers"
  echo "dependencies: Install all dependencies"
#  echo "forall: Run a command in all repositories"
}

# Main entry point
if [ -z "$1" ]; then
  help
else
  "$@"
fi

