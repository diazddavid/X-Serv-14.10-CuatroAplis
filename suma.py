#!/usr/bin/python3

class sumSimple:
    """Root of a hierarchy of classes implementing web applications

    This class does almost nothing. Usually, new classes will
    inherit from it, and by redefining "parse" and "process" methods
    will implement the logic of a web application in particular.
    """

    def __init__(self):
        self.odd_petition = True
        self.last_num = 0

    def parse(self, request):
        """Parse the received request, extracting the relevant information."""

        return None

    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """

        if parsedRequest.isdigit():
            if self.odd_petition:
                return("HTTP/1.1 200 OK\r\n\r\n" +
                                "<html><body><h1>Me has enviado un :</h1>" +
                                "<p>" + parsedRequest + " ,enviame otro y hare la suma </p>" +
                                "</body></html>" + "\r\n")
                self.last_num = int(parsedRequest)
                self.odd_petition = False
            else:
                suma = str(last_num + int(recurso))
                self.odd_petition = True
                return("HTTP/1.1 200 OK\r\n\r\n" +
                                "<html><body><h1>La suma es :</h1>" +
                                "<p>" + suma + "</p>" +
                                "</body></html>" + "\r\n")
