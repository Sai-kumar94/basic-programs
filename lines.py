class Line:
    def __init__(self,co1,co2):
        self.coor1=co1
        self.coor2=co2
    def distance(self):
        x1,y1=self.coor1
        x2,y2=self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    def slope(self):
        x1,y1=self.coor1
        x2,y2=self.coor2
        return (y2-y1)/(x2-x1)
c1=(3,2)
c2=(8,10)
my_line=Line(c1,c2)
print(my_line.distance())
print(my_line.slope())

