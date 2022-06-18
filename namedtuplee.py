from collections import namedtuple
#creating a 2d point with the named tuple

Point = namedtuple("Point",["x","y"])
point= Point(7,8)
print(point)
print(point.x)
print(point.y)
print(point[0])
print(point[1])


#comma-separated values as fieldnames
Point = namedtuple("Point","x,y")
point= Point(7,8)
print(point)

#white space seperated values as fieldnames
Point = namedtuple("Point","x y")
point= Point(7,8)
print(point)


#genrator expression as field names
Point = namedtuple("Point",(field for field in "xy"))
point= Point(7,8)
print(point)

#white space seperated values as fieldnames
Point = namedtuple("Point","x y",defaults=["python developer"])
point= Point(7,8)

#create a dictionary from a named tuple,field names as keys
print(point._asdict())

#replace the value of a field. 
print(point._replace(x="new developer"))