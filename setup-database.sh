#!/bin/bash
set -e

DB_NAME=${2:-my_awesome_db}
DB_USER=${1:-my_pg_user}
DB_USER_PASS=${3:-hard_password}
sudo -u postgres psql <<EOF
CREATE USER $DB_USER WITH PASSWORD '$DB_USER_PASS';
CREATE DATABASE $DB_NAME;
GRANT ALL PRIVILEGES ON DATABASE $DB_NAME to $DB_USER;
EOF

echo "Postgres User '$DB_USER' and database '$DB_NAME' created."
