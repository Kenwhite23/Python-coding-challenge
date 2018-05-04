# Pycom's Python coding challenge


Hi there! Here is a coding exercise to help us assess your technical skills.

## Before you start
Please **fork** this repository and commit all your changes to it. When you're done, send us the email with your Github repository URL.

Document steps taken and any other information you find usefull in SOLUTION.md file.

If you have any questions at any point, please reach us on email.

## HTTP and sockets

Write a Python program that inputs a full URL like
"http://www.url.com/path/a/b/c?p=1&p=2", sends the request, reads the
full response, and prints:

1. the content type and response code
2. the number of headers in the response
3. the number of lines in the body if the content type is text/html or text/plain.

It's OK to
assume HTTP-only (no HTTPS).

The catch is: write this using only the `socket` library to
send/receive, and do not use any libraries for crafting HTTP
requests and processing HTTP responses — craft the request bytes
manually and process the response bytes manually. It's OK to use
`urlparse` to break down the input url.

Good luck!
