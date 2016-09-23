import telnetlib
#import getpass

user = 'cisco'
pwd = user
host = '192.168.191.227'

tn = telnetlib.Telnet(host)
tn.read_until('Username: ')
tn.write(user + '\n')
tn.read_until('Password: ')
tn.write(pwd + '\n')

tn.write('sh arp')
tn.read_very_eager()
tn.write('exit\n')
tn.close()
