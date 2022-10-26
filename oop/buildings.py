#!/usr/bin/env python
from random import randint


class Building():
    def __init__(self, x, y, dx, dy):
        self.left   = x
        self.right  = x + dx
        self.bottom = y
        self.top    = y + dy
    
    def __str__(self):
        return '({},{},{},{})'.format(self.left, self.bottom, \
            (self.right-self.left), (self.top-self.bottom))

    def __and__(self,other):
        if intersect2(self,other):
            return True
        else:
            return False

    def area(self):
        return (self.top-self.bottom)*(self.right-self.left)

def intersect1(b1,b2):
    if (b2.right>=b1.left>=b2.left and \
        b2.top>=b1.bottom>=b2.bottom) or \
       (b2.right>=b1.right>=b2.left and \
        b2.top>=b1.bottom>=b2.bottom) or \
       (b2.right>=b1.left>=b2.left and \
        b2.top>=b1.top>=b2.bottom) or \
       (b2.right>=b1.right>=b2.left and \
        b2.top>=b1.top>=b2.bottom):
        return True
    else:
        return False       



def intersect2(b1,b2):
    hoverlaps = True
    voverlaps = True
    if (b1.left > b2.right) or (b1.right < b2.left):
        hoverlaps = False
    if (b1.top < b2.bottom) or (b1.bottom > b2.top):
        voverlaps = False
    return (hoverlaps and voverlaps)

def get_coor():
    x=randint(0,9)
    y=randint(0,9)
    dx=randint(1,(10-x))
    dy=randint(1,(10-y))
    return [x,y,dx,dy]

def get_building(p):
    return Building(p[0],p[1],p[2],p[3])

class Building3D(Building):
    def __init__(self, Building, z, dz):
        x=Building.left
        dx=Building.right-Building.left
        y=Building.bottom
        dy=Building.top-Building.bottom
        super().__init__(x,y,dx,dy)
        self.front  = z
        self.back = z + dz

    def __str__(self):
        return '({},{},{},{},{},{})'.format(self.left, self.bottom, \
                (self.front),(self.right-self.left), (self.top-self.bottom), \
                (self.back-self.front))

    def __and__(self,other):
        if intersect3D(self,other):
            return True
        else:
            return False

    def volume(self):
        return (self.top-self.bottom)*(self.right-self.left)*\
               (self.back-self.front)

def intersect3D(b1,b2):
    xoverlaps = True
    yoverlaps = True
    zoverlaps = True
    if (b1.left > b2.right) or (b1.right < b2.left):
        xoverlaps = False
    if (b1.top < b2.bottom) or (b1.bottom > b2.top):
        yoverlaps = False
    if (b1.back < b2.front) or (b1.front > b2.back):
        zoverlaps = False
    return (xoverlaps and yoverlaps and zoverlaps)
        

def get_building3d(Building):
    z = randint(0,9)
    dz = randint(1, (10-z))
    return Building3D(Building,z,dz)

def main():
    for i in range(100):
        p1=get_coor()
        p2=get_coor()

        b1=get_building(p1)
        b2=get_building(p2)

        b3=get_building3d(b1)
        b4=get_building3d(b2)

        
        if ((b1&b2)!=intersect1(b1,b2)):
            print('******************************')
            print("1st building's (x,y,dx,dy) = ",str(b1), \
                  " It's area = ",b1.area())
            print("2nd building's (x,y,dx,dy) = ",str(b2), \
                  " It's area = ",b2.area())
            print("intersect2: ",b1&b2,"intersect1:",intersect1(b1,b2))
            print("1st 3D building's (x,y,z,dx,dy,dz) = ",str(b3), \
                  " It's volume = ",b3.volume())
            print("2nd 3D building's (x,y,z,dx,dy,dz) = ",str(b4), \
                  " It's volume = ",b4.volume())
            print("intersect3D: ",b3&b4)
            print('******************************')

if __name__ == '__main__':
    main()

