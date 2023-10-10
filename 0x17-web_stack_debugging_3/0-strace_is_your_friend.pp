# Fix bad 'phpp' extension to 'php' in wordpress file

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path	  => '/usr/local/bin/:/bin/'
}
