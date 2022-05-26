#LEGB

# Local
# Enclosed
# Global

glob = "This is in the global scope"

def local_function():
    def inner_function():
        print(__name__)
    inner_function()

def type(x):
    return "I dunno, probably a string"

# Built-In

