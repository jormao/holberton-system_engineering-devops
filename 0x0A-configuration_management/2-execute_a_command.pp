# Using Puppet, create a manifest that kills a process named killmenow.
exec { 'kill_the_process':
    path    =>  '/usr/bin:/usr/sbin:/bin:/sbin',
    command =>  'pkill -f killmenow'
}
