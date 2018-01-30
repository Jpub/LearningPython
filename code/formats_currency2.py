# -*- coding: latin-1 -*-
from formats import money
X = 54321.987

print(money(X), money(X, 10, ''))   
result = "'$54,321.99', ' 54,321.99'"

print(money(X, currency=u'\xA3'), money(X, currency=u'\u00A5'))
   # '£54,321.99', '¥54,321.99'
result = "'£54,321.99', '¥54,321.99'"


print(money(X, currency=b'\xA3'.decode('latin-1')))
   # '£54,321.99'

#print(money(X, currency=u'\u20AC'), money(X, currency=b'\xA4'.decode('iso-8859-15')))
   # '€54,321.99', '€54,321.99'

