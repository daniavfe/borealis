# Initialize db
flask db init

# Add migration
flask db migrate -m "MIGRATION_NAME"

# Apply migration
flask db upgrade

# database
docker run -p 3306:3306 -p 33060:33060 -v mysql-data:/var/lib/mysql --name borealis -e MYSQL_ROOT_PASSWORD=pass -d mysql


