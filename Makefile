server-run: 
	docker-compose up -dV --remove-orphans mongodb server

server-logs:
	docker-compose logs server

mongodb-logs:
	docker-compose logs mongodb

down-all: 
	docker-compose down -v --remove-orphans && docker network prune --force