# puppet change benchmark of nginx

exec { 'nginx':
command  => "sed -i 's/worker_processes 4/worker_processes 7/' /etc/nginx/nginx.conf && sudo service nginx restart",
provider => shell,
}
