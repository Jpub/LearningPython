import sys
def bye():
    sys.exit(40)                 # Crucial error: abort now!
try:
    bye()
except:
    print('got it')              # Oops--we ignored the exit
print('continuing...')
