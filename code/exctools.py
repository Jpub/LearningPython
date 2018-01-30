import sys, traceback

def safe(callee, *pargs, **kargs):
    try:
        callee(*pargs, **kargs)            # Catch everything else
    except:                                # Or "except Exception as E:"
        traceback.print_exc()
        print('Got %s %s' % (sys.exc_info()[0], sys.exc_info()[1]))

if __name__ == '__main__':
    import oops2
    safe(oops2.oops)
