#!/bin/bash
# Helper script to quickly inspect our Postgres DB running in Docker

# Change if your service name in docker-compose.yml is different
CONTAINER_NAME="thejourney-db"
DB_USER="journey_user"
DB_NAME="journey_db"

# Run SQL commands
docker exec -i $CONTAINER_NAME psql -U $DB_USER $DB_NAME <<'EOF'
-- Show tables
\dt

-- Show all users
TABLE users;

-- Show all weights
TABLE weights;

-- Join users + weights to check ownership
SELECT 
    u.id AS user_id,
    u.email,
    w.id AS weight_id,
    w.date,
    w.weight_kg,
    w.source
FROM users u
LEFT JOIN weights w ON u.id = w.user_id
ORDER BY u.id, w.date DESC;
EOF

