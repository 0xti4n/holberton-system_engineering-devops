# puppet script that change error 500 in apache server

exec { 'error':
command  => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/' /var/www/html/wp-settings.php",
provider => shell,
}
