#!/bin/python3
def Smores(Crackers, Marshmallows, Chocolate):
    multiple = Crackers + Marshmallows + Chocolate
    crack= Crackers // 2
    marsh =  Marshmallows //1
    choc = Chocolate // 3
    return min(crack, marsh, choc)

print(Smores(24,12,36))
