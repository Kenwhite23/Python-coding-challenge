# SOLUTION

Sites I referenced for Python 3 Sockets/http Requests:

https://docs.python.org/3/library/socket.html
https://www.w3.org/Protocols/rfc2616/rfc2616.html (overview of HTTP components)
https://docs.python.org/3/library/urllib.parse.html



************************************************************************************************
Program Flow documentation:
________________________________________________________________________________________________
 Get Url from user
 parse the url
 create and initialize socket
 set socket timeout
 connect to site
 send request
 receive data and store it
 close socket
 from data get content type and store it
 from data get response code and store it
 from data get number of headers and store it
 from data get number of lines in body and store it if content type (text/html or text/plain)
 Print to user:
    Content Type:
    Response:
    Headers:
    Body Lines:

*************************************************************************************************

Script Description:

We accept the input of a url from the user, and then parse that url.
We then use the parsed data to Generate our GET request formated as follows:

Get /path http/1.0
Host:url

We Send the utf-8 encoded GET payload and Then decode the Websites Response, and save the Resulting String to the
global variable Data.

At this point a Second function runs that Filters the Data to pull the Necessary information required.
We then Print the necessary information to the user.