# filepath: /app/entrypoint.sh
#!/bin/bash
set -e

# Source the pnpm environment variables
source /etc/profile.d/pnpm.sh

# Update caniuse-lite
npx update-browserslist-db@latest

# Start the development server
exec "$@"
