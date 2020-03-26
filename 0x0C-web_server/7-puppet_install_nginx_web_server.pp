#!/usr/bin/env bash
# install nginx with puppet

exec { 'nginx':
command  => 'sudo apt-get update && sudo apt-get install -y nginx && echo "Holberton School for the win!" | sudo tee /var/www/html/index.html && sed -i "/server_name _;/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default && sudo service nginx restart',
provider => shell,
}