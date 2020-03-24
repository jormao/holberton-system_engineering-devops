# Using Puppet, create a manifest that kills a process named killmenow.
exec {'killmenow':
    path    =>  ['/usr/bin', '/bin', '/sbin', '/usr/sbin'],
    command =>  'pkill -f killmenow',
    provider => 'shell',
}
