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

    def parse(self, request, rest):
        """Parse the received request, extracting the relevant information."""

        return rest[1:]

    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """

        if self.odd_petition:
            try:
                self.last_num = int(parsedRequest)
            except ValueError:
                return ("HTTP/1.1 404 Not Found", "<html><body><p>Introduzca un numero por favor</p></body></html>")
            self.odd_petition = False
            return ("HTTP/1.1 200 OK", "<html><body><h1>Me has enviado un :</h1>" +
                            "<p>" + parsedRequest + " ,enviame otro y hare la suma </p>" +
                            "</body></html>" )
        else:
            try:
                suma = str(self.last_num + int(parsedRequest))
            except ValueError:
                return ("HTTP/1.1 404 Not Found", "<html><body><p>Introduzca un numero por favor</p></body></html>")
            self.odd_petition = True
            return("200 OK", "<html><body><h1>La suma es :</h1>" +
                            "<p>" + suma + "</p>" +
                            "</body></html>" )
