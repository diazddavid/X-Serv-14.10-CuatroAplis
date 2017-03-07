#!/usr/bin/python3

class aleat:
    """Root of a hierarchy of classes implementing web applications

    This class does almost nothing. Usually, new classes will
    inherit from it, and by redefining "parse" and "process" methods
    will implement the logic of a web application in particular.
    """

    def parse(self, request):
        """Parse the received request, extracting the relevant information."""

        return None

    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """
        import random

        nextDirection = str(random.randrange(100000000000))
        return("HTTP/1.1 200 OK\r\n\r\n" +
                "<html><body><h1><a href=" + nextDirection +
                ">Dame otra </a> </h1></body></html>" + "\r\n")
