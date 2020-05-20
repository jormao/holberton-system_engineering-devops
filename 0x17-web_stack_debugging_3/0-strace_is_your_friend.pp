#fix error
exec { 'fix php error':
    command => '/bin/sed -i \'s/.phpp/.php/\' /var/www/html/wp-settings.php'
}
exec { 'restart apache':
    command => '/usr/sbin/service apache2 restart'
}
