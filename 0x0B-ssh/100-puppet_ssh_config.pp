# connect to a seerver Execute a command

exec { 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config': path     => '/bin/'
}
