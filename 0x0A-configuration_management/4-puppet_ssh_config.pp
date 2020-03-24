# using Puppet to make changes to our configuration file
file { '/etc/ssh/ssh_config':
  ensure  =>  present,
}
file_line { 'private_key':
  ensure  =>  present,
  path  =>  '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/holberton',
  match =>  '^IdentityFile.*$'
}
file_line { 'Pass_authent':
  ensure  =>  present,
  path  =>  '/etc/ssh/ssh_config',
  line  =>  'PasswordAuthentication no',
  match =>  '^PasswordAuthentication.*$'
}
