book = { }

book['tom'] = {
    'name' : 'tom',
    'address' : 'Red Street, NY',
    'phone' : 272382942

}


book['bob'] = {
    'name' : 'bob',
    'address' : 'Pink Street, NY',
    'phone' : 272307642

}

import json
s= json.dumps(book)
print(s)
print(type(book))