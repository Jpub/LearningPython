# Same, but with generic __getattribute__ all attribute interception

class Powers(object):                                    # Need (object) in 2.X only
    def __init__(self, square, cube):
        self._square = square
        self._cube   = cube

    def __getattribute__(self, name):
        print('get:',name)
        if name == 'square':
            return self._square ** 2             # <= works, but causes an extra __getattribute__ call
        elif name == 'cube':
            return self._cube ** 3
        else:
            return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == 'square':
            object.__setattr__(self, '_square', value)   # Or use __dict__
        else:
            object.__setattr__(self, name , value)

X = Powers(3, 4)
print(X.square)      # 3 ** 2 = 9
print(X.cube)        # 4 ** 3 = 64
X.square = 5
print(X.square)      # 5 ** 2 = 25
