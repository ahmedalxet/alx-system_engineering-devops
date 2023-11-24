# Install Flask from pip3

package { 'python3-pip':
  ensure => present,
}

exec { 'install_flask':
  command     => '/usr/bin/pip3 install flask==2.1.0',
  path        => ['/usr/bin', '/usr/local/bin'],
  refreshonly => true,
  require     => Package['python3-pip'],
}
