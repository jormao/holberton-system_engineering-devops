#fix error
exec { 'fix php error':
    command => '/bin/sed -i \'s/.phpp/.php\' /var/www/html/wp-settings.php'
}
