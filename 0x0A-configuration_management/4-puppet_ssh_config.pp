# using Puppet to make changes to our configuration file
file { '/etc/ssh/ssh_config':
  ensure  =>  present,
}->
file_line { 'passwd auth':
  ensure =>  'present',
  path   =>  '/etc/ssh/ssh_config',
  line   =>  'PasswordAuthentication no',
}->
file_line { 'Declare identity file':
  ensure => 'present',
  path   =>  '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
}
