class Catcher:
    def __getattr__(self, name):
        print('Get: %s' % name)
    def __setattr__(self, name, value):
        print('Set: %s %s' % (name, value))

X = Catcher()
X.job                               # Prints "Get: job"
X.pay                               # Prints "Get: pay"
X.pay = 99                          # Prints "Set: pay 99"
