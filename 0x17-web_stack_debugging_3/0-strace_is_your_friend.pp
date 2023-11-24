# Puppet manifest to fix Apache 500 error

$file_pth = '/var/www/html/wp-settings.php'
exec{ 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_pth}",
  path    => ['/bin','/usr/bin']
}
