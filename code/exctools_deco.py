import sys, traceback

def safe(callee):
    def callproxy(*pargs, **kargs):
        try:
            return callee(*pargs, **kargs)  
        except:                                
            traceback.print_exc()
            print('Got %s %s' % (sys.exc_info()[0], sys.exc_info()[1]))
            raise
    return callproxy

if __name__ == '__main__':
    import oops2

    @safe
    def test():
        oops2.oops()

    test()
