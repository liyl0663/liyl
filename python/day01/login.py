# import json
# var1={'500':'this is string',500:'this is number', "500":'this is string2'}
# var2=json.loads(json.dumps(var1))

a = [[1,2,3,4,5]] * 3
print(a[2])
a[0][1] = 100
var = a[2][1]
print(var)