class Wrapper:
    def __init__(self, object):
        self.wrapped = object                    # Save object
    def __getattr__(self, attrname):
        print('Trace: ' + attrname)              # Trace fetch
        return getattr(self.wrapped, attrname)   # Delegate fetch

X = Wrapper([1, 2, 3])
X.append(4)                                      # Prints "Trace: append"
print(X.wrapped)                                 # Prints "[1, 2, 3, 4]"
