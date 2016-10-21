import math

a=int (raw_input("A?"))
b=int (raw_input ("B?"))
c=int (raw_input ("C?"))


delta = (b*b)-4*a*c

print 'delta = ' + str(delta)

x=-b/(2*a)
y=-(delta)/(4*a)

print 'x wierzcholka= ' + str(x) + ' y wierzcholka= ' + str(y)

print "miejsca zerowe:"

if (delta) > 0:
    x1 = (-b- math.sqrt(delta))/(2*a)
    x2 = (-b + math.sqrt(delta))/(2*a)

if (delta) < 0:
    print 'nie ma miejsc zerowych'

if (b*b-4*a*c) == 0:
    print -b/(2*a)
