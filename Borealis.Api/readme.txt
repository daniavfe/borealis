# Initialize db
flask db init

# Add migration
flask db migrate -m "MIGRATION_NAME"

# Apply migration
flask db upgrade

# Revert migration
flask db downgrade <<migrationhash>>

# database
docker run -p 3306:3306 -p 33060:33060 -v mysql-data:/var/lib/mysql --name borealis -e MYSQL_ROOT_PASSWORD=pass -d mysql --linux
docker run -p 3306:3306 -p 33060:33060 -v D:\Projects\ddbb:/var/lib/mysql --name borealis -e MYSQL_ROOT_PASSWORD=pass -d mysql --windows


