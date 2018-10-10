from collections import namedtuple
Point = namedtuple('Point',['x','y','z'])
a = Point(10,20,50)
print(len(a))
print(a[0])
print(a[:2])
print(a.x)
print(a.y)
print(a.z)