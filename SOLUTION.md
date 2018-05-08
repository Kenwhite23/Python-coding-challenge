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
 from data get content type and print to user
 from data get response code and print to user
 from data get number of headers and print to user
 from data get number of lines in body and print to user (text/html or text/plain)
 Print to user:
    Content Type:
    Response:
    Headers:
    Body Lines:
 Give User Option to View Full Response from url

*************************************************************************************************

Program Description:

We accept the input of a url from the user, and then parse that url.
We then use the parsed data to Generate our GET request formatted as follows:

Get /path/query http/1.0
Host:url

We Send the utf-8 encoded GET payload and Then decode the Websites Response, and save the Resulting String to the
global variable Data.

We then take the data and run it through function contenttype to filter out and print to user the content type

This then repeats but with function responsecode to filter out and print to the user the response code

afterwords we run the data through a regex to locate the headers and then after
removing false headers (the location header returns a url causing http: or https: to give a false regex match)
we count the total number of headers using len(result) and display it to the user.

Finally we get the number of body lines and display it to the user.

At the end we provide the user the option to display the full response from the URL in case they want more detailed information
the prompt accepts y, Y, yes, and Yes all as valid options to display the full response because people do not often follow instructions when prompted to enter y/n

