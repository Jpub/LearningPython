# Extend with a decorator: same as providing __init__ in a metaclass

def eggsfunc(obj):
    return obj.value * 4

def hamfunc(obj, value):
    return value + 'ham'

def Extender(aClass):
    aClass.eggs = eggsfunc                   # Manages class, not instance
    aClass.ham  = hamfunc                    # Equiv to metaclass __init__
    return aClass

@Extender
class Client1:                               # Client1 = Extender(Client1)
    def __init__(self, value):               # Rebound at end of class stmt
        self.value = value
    def spam(self):
        return self.value * 2

@Extender
class Client2:
    value = 'ni?'

X = Client1('Ni!')                           # X is a Client1 instance
print(X.spam())
print(X.eggs())
print(X.ham('bacon'))

Y = Client2()
print(Y.eggs())
print(Y.ham('bacon'))
