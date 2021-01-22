import os

CENTER = (0,0)
CORDINATES = list(CENTER)
MAX_PIXEL = 200.00
CENTER_PIXEL = 100
MIN_PIXEL = 0

class Svg:
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

draw = Svg('test')

def test():
    draw.add(Line(tuple(CORDINATES),(120,120), 0))
    draw.write_svg()
    draw.display()
    return
#test()