import socket
from urllib.parse import urlparse
import re
#import string

# from data get number of headers and store it
# from data get number of lines in body and store it
# Print to user:
# Headers: number
# Body: lines


#####################################################################################################
# Accept URL from User and Then Parse it
userurl = input('Enter a url:')
url = urlparse(userurl)
path = url.path
if path == "":
    path = "/"
HOST = url.netloc  # The remote host
PORT = 80
######################################################################################################
# Variables used to Build our Request Payload
CRLF = "\r\n\r\n"
query = '?' + url.query
gets = 'GET ' + path + query + ' HTTP/1.1\r\n'
hosts = 'Host:' + HOST + CRLF
payload = (gets + hosts)
#######################################################################################################

def GET(url):  # Get Function, This creates our socket connects to our website sends the Payload, and then Saves the Response
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.30)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((HOST, PORT))
    s.sendall(payload.encode('utf-8'))
    global data
    data = (s.recv(512))
    data = data.decode('utf-8')
    s.shutdown(1)
    s.close()

#########################This section of Code no longer used####################################
#def normalize_line_endings(s):
#   return ''.join((line + '\n') for line in s.splitlines())

#def datas(): #Pulls Data we need, and then Prints it to user (still to be done currently displays full GET response)
 #   global data2
 #   data2 = normalize_line_endings(data)
 #   data2 = data2.split('\n')
#################################################################################################
def contenttype():
    cont1 = re.compile('text/plain')
    textplain = cont1.search(data)
    cont2 = re.compile('text/html')
    texthtml = cont2.search(data)
    if textplain:
        print('Content Type: ', textplain.group())
    elif texthtml:
        print('Content Type: ', texthtml.group())

def responsecode():
    r = re.compile('[1-9][0-9][0-9] ')
    rc = r.search(data)
    if rc:
        print('Response Code: ', rc.group())

def headercount():
    print('Header Count: ')

def bodylines():
    print('Body Line Count: ')


GET(url)
#datas()
print('\n****************************************')
contenttype()
responsecode()
headercount()
bodylines()
print('****************************************')