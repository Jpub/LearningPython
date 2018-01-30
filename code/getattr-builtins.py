class GetAttr:
    eggs = 88                    # eggs stored on class, spam on instance
    def __init__(self):
       self.spam = 77
    def __len__(self):           # len here, else __getattr__ called with __len__
        print('__len__: 42')
        return 42
    def __getattr__(self, attr):     # Provide __str__ if asked, else dummy func
        print('getattr: ' + attr)
        if attr == '__str__':
            return lambda *args: '[Getattr str]'
        else:
            return lambda *args: None

class GetAttribute(object):          # object required in 2.X, implied in 3.X
    eggs = 88                        # In 2.X all are isinstance(object) auto
    def __init__(self):              # But must derive to get new-style tools,
        self.spam = 77               # incl __getattribute__, some __X__ defaults
    def __len__(self):
        print('__len__: 42')
        return 42
    def __getattribute__(self, attr):
        print('getattribute: ' + attr)
        if attr == '__str__':
            return lambda *args: '[GetAttribute str]'
        else:
            return lambda *args: None

for Class in GetAttr, GetAttribute:
    print('\n' + Class.__name__.ljust(50, '='))

    X = Class()
    X.eggs                   # Class attr
    X.spam                   # Instance attr
    X.other                  # Missing attr
    len(X)                   # __len__ defined explicitly

# New-styles must support [], +, call directly: redefine

    try:    X[0]             # __getitem__?
    except: print('fail []')

    try:    X + 99           # __add__?
    except: print('fail +')

    try:    X()              # __call__?  (implicit via built-in)
    except: print('fail ()')

    X.__call__()             # __call__?  (explicit, not inherited)
    print(X.__str__())       # __str__?   (explicit, inherited from type)
    print(X)                 # __str__?   (implicit via built-in)
