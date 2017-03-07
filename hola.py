#!/usr/bin/python3

class hola:
    """Root of a hierarchy of classes implementing web applications

    This class does almost nothing. Usually, new classes will
    inherit from it, and by redefining "parse" and "process" methods
    will implement the logic of a web application in particular.
    """

    def parse(self, request, rest):
        """Parse the received request, extracting the relevant information."""

        return None

    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """

        return("200 OK", "<html><body><h1> HOLA </h1></body></html>")

class adios:
    """Root of a hierarchy of classes implementing web applications

    This class does almost nothing. Usually, new classes will
    inherit from it, and by redefining "parse" and "process" methods
    will implement the logic of a web application in particular.
    """

    def parse(self, request, rest):
        """Parse the received request, extracting the relevant information."""

        return None

    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """

        return("200 OK", "<html><body><h1> ADIOS </h1></body></html>" )
