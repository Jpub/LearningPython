def kaboom(x, y):
    print(x + y)               # Trigger TypeError

try:
    kaboom([0, 1, 2], 'spam')
except TypeError:              # Catch and recover here
    print('Hello world!')
print('resuming here')         # Continue here if exception or not
