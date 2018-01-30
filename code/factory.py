def factory(aClass, *pargs, **kargs):        # Varargs tuple, dict
    return aClass(*pargs, **kargs)           # Call aClass (or apply in 2.X only)

class Spam:
    def doit(self, message):
        print(message)

class Person:
    def __init__(self, name, job=None):
        self.name = name
        self.job  = job

object1 = factory(Spam)                      # Make a Spam object
object2 = factory(Person, "Arthur", "King")  # Make a Person object
object3 = factory(Person, name='Brian')      # Ditto, with keywords and default
