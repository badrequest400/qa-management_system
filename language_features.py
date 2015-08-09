
# SUPER CLASS FROM WHICH WE CAN INHERIT
class BaseClass():

    __type = 'BaseClass'    # PRIVATE CLASS VARIABLE, SUBCLASSES INHERIT IT

    def __init__(self, id, name, mode): # CONSTRUCTOR METHOD FOR THE CLASS
        self.__id = id      # PRIVATE INSTANCE VARIABLE
        self._name = name   # PROTECTED INSTANCE VARIABLE
        self.mode = mode    # UNPROTECTED PUBLIC INSTANCE VARIABLE

    def getName(self):      # CLASS METHOD
        return self.name

    def getInfo(self):      # ABSTRACT CLASS METHOD, NOT IMPLEMENTED, SUBCLASSES WILL IMPLEMENT
        raise NotImplementedError

# SUBCLASS THAT INHERITS FROM THE SUPER CLASS
class SubClass(BaseClass):

    # NO CONSTRUCTOR METHOD IS IMPLEMENTED, SINCE IT IS INHERITED FROM THE SUPER CLASS
    # THE CONSTRUCTOR COULD BE OVERWRITTEN WITH POLYMORPHISM
    # HOWEVER WE WANT TO PRESERVE THE COMMON BEHAVIOUR

    # POLYMORPHISM LET'S US CHANGE THE BEHAVIOUR OF CLASS METHODS IN THE SUBCLASSES
    # THAT INHERIT FROM THE SUPER CLASS
    def getInfo(self):
        return {'id': self.__id, 'name': self._name, 'mode': self.mode }
