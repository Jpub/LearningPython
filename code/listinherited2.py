#!python
# File listinherited.py (2.X + 3.X)

class ListInherited:
    """
    Use dir() to collect both instance attrs and names inherited from 
    its classes;  Python 3.X shows more names than 2.X because of the 
    implied object superclass in the new-style class model;  getattr() 
    fetches inherited names not in self.__dict__;  use __str__, not 
    __repr__, or else this loops when printing bound methods!
    """
    def __attrnames(self, indent=' '*4):
        result  = 'Unders%s\n%s%%s\nOthers%s\n' % ('-'*77, indent, '-'*77)
        unders = []
        for attr in dir(self):                              # Instance dir()
            if attr[:2] == '__' and attr[-2:] == '__':      # Skip internals
                unders.append(attr)
            else:
                display = str(getattr(self, attr))[:82-(len(indent) + len(attr))]
                result += '%s%s=%s\n' % (indent, attr, display)
        return result % ', '.join(unders)

    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
                           self.__class__.__name__,         # My class's name
                           id(self),                        # My address
                           self.__attrnames())              # name=value list

if __name__ == '__main__': 
    import testmixin
    testmixin.tester(ListInherited)
