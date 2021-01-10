import os

CENTER = (100,100)
CORDINATES = list(CENTER)
MAX_PIXEL = 200.00
CENTER_PIXEL = 100
MIN_PIXEL = 0

      
class Draw:
    def __init__(self,name="svg",begin=0,end=MAX_PIXEL):
        self.name = name
        self.items = []
        self.begin = begin
        self.end = end
        return

    def add(self,item): self.items.append(item)

    def strarray(self):
        var = [
               '<svg viewBox=\"%d %d %.2f %.2f\" xmlns="http://www.w3.org/2000/svg" >\n' % (self.begin,self.begin,self.end,self.end),
               ]
        for item in self.items: var += item.strarray()            
        var += ["</svg>\n"]
        return var

    def write_svg(self,filename=None):
        if filename:
            self.svgname = filename
        else:
            self.svgname = self.name + ".svg"
        file = open(self.svgname,'w')
        file.writelines(self.strarray())
        file.close()
        return

    def display(self):
        os.startfile(self.svgname)
        return    
            
class Line:
    def __init__(self,start,end,color):
        self.start = start #xy tuple
        self.end = end     #xy tuple
        self.color = color #rgb tuple in range(0,256)
        return

    def strarray(self):
        return ["  <line x1=\"%.10f\" y1=\"%.10f\" x2=\"%.10f\" y2=\"%.10f\" style=\"stroke: rgb(%d, %d, %d); stroke-width: 2px\" />\n" %\
                (self.start[0],self.start[1],self.end[0],self.end[1],self.color,self.color,self.color)]
           
#def colorstr(rgb): return "#%x%x%x" % (int(rgb[0]/16),int(rgb[1]/16),int(rgb[2]/16))

draw = Draw('test')

def transformXY(new_cord):
    new_x = CORDINATES[0] + new_cord[0]
    new_y = CORDINATES[1] + new_cord[1]
    max_x = new_x
    max_y = new_y
    min_x = CORDINATES[0]
    min_y = CORDINATES[1]

    if new_x > MAX_PIXEL:
        max_x = MAX_PIXEL
        min_x = MIN_PIXEL
        new_x = new_x % MAX_PIXEL
        min_y = (100 - new_cord[1])
        new_y = min_y + (new_y-CENTER_PIXEL)/(CENTER_PIXEL/new_x)
    if new_y > MAX_PIXEL:
        max_y = MAX_PIXEL
        min_y = MIN_PIXEL
        new_y = new_y % MAX_PIXEL
        min_x = (100 - new_cord[0])
        new_x = min_x + (new_x-CENTER_PIXEL)/(CENTER_PIXEL/new_y)

    draw.add(Line(tuple(CORDINATES),(max_x,max_y), 0))
    draw.add(Line((min_x,min_y),(new_x,new_y),0))
    CORDINATES[0] = new_x
    CORDINATES[1] = new_y

def test():
    transformXY((90,150))
    transformXY((40,-80))
    draw.write_svg()
    draw.display()
    return

test()