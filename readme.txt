# Initialize db
flask db init

# Add migration
flask db migrate -m "MIGRATION_NAME"

# Apply migration
flask db upgrade