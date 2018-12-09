from math import *

def typeInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def typeFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def convertType(s):
    for n in s:
        if typeInt(s):
            return int(s)
        elif typeFloat(s):
            return float(s)
        else:
            return str(s)
    return s

def pick (n, k):
    return (factorial(n)/(factorial(n-k)*factorial(k)))

def vecmagadd(mag1, dir1, mag2, dir2):
    vec1 = [mag1*cos(radians(dir1)),mag1*sin(radians(dir1))]
    vec2 = [mag2*cos(radians(dir2)),mag2*sin(radians(dir2))]
    vAdd = [vec1[0]+vec2[0],vec1[1]+vec2[1]]
    vMag = sqrt(vAdd[0]*vAdd[0]+vAdd[1]*vAdd[1])
    vDir = atan2(vAdd[1],vAdd[0])
    vDir = degrees(vDir)
    if vDir < 0 :
        vDir+=360.0
    return [vMag,vDir]

def vecmagaddunits(mag1, dir1, mag2, dir2):
    vAdd = [mag1+mag2,dir1+dir2]
    vMag = sqrt(vAdd[0]*vAdd[0]+vAdd[1]*vAdd[1])
    vDir = atan2(vAdd[1],vAdd[0])
    return [vMag,vDir]

def vecmagsub(mag1, dir1, mag2, dir2):
    vec1 = [mag1*cos(radians(dir1)),mag1*sin(radians(dir1))]
    vec2 = [mag2*cos(radians(dir2)),mag2*sin(radians(dir2))]
    vSub = [vec1[0]-vec2[0],vec1[1]-vec2[1]]
    vMag = sqrt(vSub[0]*vSub[0]+vSub[1]*vSub[1])
    vDir = atan2(vSub[1],vSub[0])
    vDir = degrees(vDir)
    if vDir < 0 :
        vDir+=360.0
    return [vMag,vDir]

def vecmagsubunits(mag1, dir1, mag2, dir2):
    vSub = [mag1-mag2,dir1-dir2]
    vMag = sqrt(vSub[0]*vSub[0]+vSub[1]*vSub[1])
    vDir = atan2(vSub[1],vSub[0])
    return [vMag,vDir]

def complexangle(realn, compn, degrad):
    if degrad == 'd':
        return degrees(atan2(compn,realn))
    elif degrad == 'r':
        return atan2(compn,realn)
    else:
        return atan2(compn,realn)

def compmagdir(mag, dir):
    return [mag*cos(radians(dir)),mag*sin(radians(dir))]

r=[convertType(x) for x in input("Stuff: ").split()]

# print(vecmagsub(r[0],r[1],r[2],r[3]))
print(complexangle(r[0],r[1],r[2]))
# print(vecmagadd(r[0],r[1],r[2],r[3]))
# print(pick(r[0],r[1]))
# def sixtext(n):
#     for i in range(100000):
#         if(i % 2 == 0):
#             print(6.0*i)
# print(sixtext(r));
