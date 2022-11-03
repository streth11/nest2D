from nest2D import Point as nest2s_Point
from nest2D import Box as nest2s_Box
from nest2D import Item as nest2s_Item
from nest2D import nest  as nest2s_nest
from nest2D import SVGWriter as nest2s_SVGWriter

class Box():
    def __init__(self,w:int,h:int) -> None:
        self.w = w
        self.h = h
        self.box = nest2s_Box(w,h)


class Point():
    def __init__(self,x:int,y:int) -> None:
        self.point = nest2s_Point(x,y)


class Item():
    def __init__(self,pointList:list) -> None:
        self.item = nest2s_Item([point.point for point in pointList])

    @property
    def area(self):
        return self.item.area
    @property
    def translation(self):
        return self.item.translation
    @property
    def rotation(self):
        return self.item.rotation


class NestInput():
    def __init__(self) -> None:
        self.input = []

    def add_shape_n(self,n:int,shape:Item):
        for i in range(n):
            self.input.append(shape.item)
        return self


def nest(input:NestInput,box:Box,dist:int = 0):
    return nest2s_nest(input.input, box.box, dist)


class SVGWriter():
    def __init__(self) -> None:
        self.sw = nest2s_SVGWriter()

    def write_packgroup(self,pgrp,box:Box):
        self.sw.write_packgroup(pgrp,box.w,box.h)

    def save(self):
        self.sw.save()




def main():
    x = -11750000
    y = 13057900

    Q = nest2s_Point(x, y)
    print(Q)
    print(type(Q))

    P = Point(-11750000, 13057900)
    print(P)
    print(type(P.point))

    item = Item([
        Point(-11750000, 13057900),
        Point(-9807860, 15000000),
        Point(4392139, 24000000),
        Point(11750000, 24000000),
        Point(11750000, -24000000),
        Point(4392139, -24000000),
        Point(-9807860, -15000000),
        Point(-11750000, -13057900),
        Point(-11750000, 13057900)
    ])

    box = Box(150000000, 150000000)
    dist = 5000000
    shape_input = NestInput().add_shape_n(5,item)

    print(shape_input.input)

    pkgrp = nest(shape_input,box=box,dist=dist)

    sw = SVGWriter()
    sw.write_packgroup(pkgrp,box)
    sw.save()

if __name__ == '__main__':
    main()
