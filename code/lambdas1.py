L = [lambda x: x ** 2,               # Inline function definition
     lambda x: x ** 3,
     lambda x: x ** 4]               # A list of 3 callable functions

for f in L:
    print(f(2))                      # Prints 4, 8, 16

print(L[0](3))                       # Prints 9



def f1(x): return x ** 2
def f2(x): return x ** 3             # Define named functions
def f3(x): return x ** 4

L = [f1, f2, f3]                     # Reference by name

for f in L:
    print(f(2))                      # Prints 4, 8, 16

print(L[0](3))                       # Prints 9
