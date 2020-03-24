# using Puppet to make changes to our configuration file
file { '/etc/ssh/ssh_config':
  ensure  =>  present,
}
file_line { 'private_key':
  path  =>  '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/holberton',
}
file_line { 'Pass_authent':
  path  =>  '/etc/ssh/ssh_config',
  line  =>  'PasswordAuthentication no',
}
