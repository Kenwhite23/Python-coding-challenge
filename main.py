import socket
from urllib.parse import urlparse
import re

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
que = url.query
if que == "":
    query = url.query
elif que != "":
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

def contenttype():  # The contenttype() funtion searches for the content type either text/html or text/plain and displays it to the user.
    #  if neither are found it displays no content type returned to user
    cont1 = re.compile('text/plain')
    textplain = cont1.search(data)
    cont2 = re.compile('text/html')
    texthtml = cont2.search(data)
    other = ""
    if textplain:
        print('Content Type: ', textplain.group())
    elif texthtml:
        print('Content Type: ', texthtml.group())
    else:
        print('Content Type: No content type was returned!')

def responsecode():  #  the responsecode function searches our data for the 3 digit response code and displays it to the user.
    #  In the odd event theres an error or no response code is sent it displays no response code returned to the user while sighing painfully at someones broken website
    r = re.compile('[1-9][0-9][0-9] ')
    rc = r.search(data)
    if rc:
        print('Response Code: ', rc.group())
    else:
        print('Response Code: No response code was returned')


def headercount():
    # This section searches data using a regex to find all valid headers and then remove all known false positives
    h = re.findall('[-!#-*+.A-Z^-z|~]+:',data)
    if h.__contains__('https:'):
        h.remove('https:')
    elif h.__contains__('http:'):
        h.remove('http:')

    # we then use len to get the total number of regex matches minus the false positives and display it to the user,
    hc = len(h)
    if hc:
        print('Header Count: ', hc)
    else:  #  In the unlikely event that we cant ascertain the header count we display a prompt to let the user know the count is unvailable
        print('Header Count: Header Count unavailable!')

def bodylines():
    bl = ""
    if bl == 6:
        print('Body Line Count: ')
    else:
        print('Body Line Count: Body Line Count Unavailable!')

def viewfullresponse():  # viewfullresponse gives the user the option at the end to view the full response that was recieved after sending our payload
    s = input('Would you like to view the full response? (y/n)')
    if s == 'y' or 'Y' or 'yes' or 'Yes':
        print('\n****************************************')
        print (data)
        print('****************************************')

def main():
    # Technically not a requirement in python but i like clean code, this is our main loop, and runs everything we need done in order,
    # by using a main() we can customize what we are doing and modify the program to change how it runs at a later date much faster,
    #  then searching through lines of code to find a specific operation.
    print('\n****************************************')
    contenttype()
    responsecode()
    headercount()
    bodylines()
    print('****************************************')
    viewfullresponse()

GET(url)  # this takes the user inputed url, generates a payload, sends the payload, and stores the response
main()  # this runs our main loop, the creme dela creme of the program



