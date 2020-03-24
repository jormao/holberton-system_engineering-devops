# Using Puppet, create a manifest that kills a process named killmenow.
exec {'killmenow':
    path    =>  ['/usr/bin', '/usr/sbin', '/bin', '/sbin', '/usr/local/sbin', '/usr/local/bin'],
    command =>  'pkill -f killmenow'
}
