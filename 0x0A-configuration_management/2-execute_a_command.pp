# Using Puppet, create a manifest that kills a process named killmenow.
exec {'killmenow':
    command =>  '/usr/bin/env/pkill -f killmenow'
}
