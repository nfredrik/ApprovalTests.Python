import inspect
import os

class Namer(object):
    """description of class"""

    ClassName = ''
    MethodName = ''
    Directory = ''

    def setForStack(self, caller):
        self.MethodName = caller[1][3]
        self.ClassName = caller[1][0].f_globals["__name__"]
        self.Directory = os.path.dirname(caller[1][1])

    def __init__(self):
        self.setForStack(inspect.stack(1))

    def getClassName(self):
        return self.ClassName

    def getMethodName(self):
        return self.MethodName

    def getDirectory(self):
        return self.Directory

    def get_basename(self):
        return self.Directory + "\\" + self.ClassName + "." + self.MethodName;
