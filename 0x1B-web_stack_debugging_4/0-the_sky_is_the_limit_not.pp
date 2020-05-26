# Change the limits
exec { 'limits_fixed':
  command  => 'sed -i "s/-n 15/-n 5000/g"\
  /etc/default/nginx; sudo service nginx restart',
  provider => 'shell'
}
