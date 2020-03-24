# Using Puppet, create a manifest that kills a process named killmenow.
exec { 'killmenow':
    path    =>  '/usr/bin:/usr/sbin:/bin:/sbin',
    command =>  'pkill -f killmenow'
}
