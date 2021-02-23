import sys

GREETING = "Hello, "  # const I dont want to use outside this file
print(sys.modules)
_WontIMPORT = "Hello, " # works same as __all__ =

class BadName(Exception):
    pass


def greet(name):
    if name[0].isupper():
        return GREETING + name
    else:
        raise BadName(name + " is inappropriate name")


__all__ = ["BadName", "greet"]  # these functions and classes I will use outside of this file, other variables - no
