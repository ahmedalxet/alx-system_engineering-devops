class web_stack_debugging {
  package { 'apache2':
    ensure => installed,
  }

  file { '/var/www/html/index.html':
    ensure  => file,
    content => '<html><body><h1>It works!</h1></body></html>',
    require => Package['apache2'],
  }

  service { 'apache2':
    ensure  => running,
    enable  => true,
    require => File['/var/www/html/index.html'],
  }
}

include web_stack_debugging
