# Manifest that kills a process named killmenow

exec { 'kill_killmenow_process':
  command  => 'pkill -f killmenow',
  provider => 'shell',
  path     => ['/usr/bin', '/usr/sbin']
}
