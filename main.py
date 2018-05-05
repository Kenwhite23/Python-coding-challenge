import socket
from urllib.parse import urlparse

# from data get content type and store it
# from data get response code and store it
# from data get number of headers and store it
# from data get number of lines in body and store it
# from data get body content type (text/html or text/plain) and store it
# Print to user:
# content: type
# Response: code
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
gets = 'GET ' + path + url.query + ' HTTP/1.0%s' % CRLF
hosts = 'Host: ' + HOST
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

def datas(): #Pulls Data we need, and then Prints it to user (still to be done currently displays full GET response)

    print (url, '\n')
    print (payload,'\n')
    print (data)



GET(url)
datas()


