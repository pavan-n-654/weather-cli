#!/bin/sh

docker network create custom_network
alias build_app='docker build -t weather-cli .'
alias delete_db="docker rm -f mongo"
alias delete_app="docker rm -f app"
alias run_db="docker run -d --network custom_network -h mongo --name mongo -p 27017:27017 mongo"
alias run_app="docker run -it --rm --network custom_network -h app --name app weather-cli"
alias setup_db="docker exec -it app /bin/sh"
