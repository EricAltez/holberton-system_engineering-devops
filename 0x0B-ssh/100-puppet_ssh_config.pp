#using Puppet change the configuration file.
file { '/etc/ssh/ssh_config':
  ensure  => 'present',
  mode    => '0744',
  content => 'Host * \n PasswordAuthentication no \n IdentityFile ~/.ssh/school',
  group   => 'root',
  owner   => 'root',
}
