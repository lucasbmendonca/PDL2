import svgwrite
import math
import os


class LOGODraw:


    def __init__(self):
        self.initialPoint = (400, 300)
        self.track = [self.initialPoint]
        self.angle = 90
        self.penStatus = 1
        self.filename = "logo.svg"
        self.r = 0
        self.g = 255
        self.b = 0
        self.svgFile = svgwrite.Drawing(filename = self.filename, size = ("3200px", "2400px"))


    def SaveSVG(self):
        self.svgFile.save()
    
    def display(self):
        os.startfile(self.filename)
        return    

    def Right(self, ang):
        self.angle  = self.angle + ang

    def Left(self, ang):
        self.angle = self.angle - ang

    def Forward(self, distance):    
        x = distance * math.cos(math.radians(self.angle)) - self.track[len(self.track)-1][0]
        if x < 0:
            x = x * (-1)
        y = distance * math.sin(math.radians(self.angle)) - self.track[len(self.track)-1][1]
        if y < 0:
            y = y * (-1)
        self.svgFile.add(self.svgFile.polyline(points = [(self.track[len(self.track)-1]),(x,y)], stroke = svgwrite.rgb(self.r, self.g, self.b, '%'), stroke_width= self.penStatus, fill = 'none'))
        self.track.append((x,y))

    def Back(self, distance):
        x = distance * math.cos(math.radians(self.angle)) + self.track[len(self.track)-1][0]
        if x < 0:
            x = x * (-1)
        
        y = distance * math.sin(math.radians(self.angle)) + self.track[len(self.track)-1][1]
        if y < 0:
            y = y * (-1)
        self.svgFile.add(self.svgFile.polyline(points = [(self.track[len(self.track)-1]),(x,y)], stroke = svgwrite.rgb(self.r, self.g, self.b, '%'), stroke_width= self.penStatus, fill = 'none'))
        self.track.append((x,y))

    def SetPos(self, x, y):
        self.track.append((x, y))
        self.svgFile.add(self.svgFile.polyline(points = self.track, stroke = svgwrite.rgb(self.r, self.g, self.b, '%'), stroke_width= self.penStatus, fill = 'none'))

    def SetXY(self, x, y):
        self.track.append((x,y))
        print(self.track)
        self.svgFile.add(self.svgFile.polyline(points = self.track, stroke = svgwrite.rgb(self.r, self.g, self.b, '%'), stroke_width= self.penStatus, fill = 'none'))

    def SetX(self, x):
        self.track.append((x, self.track[len(self.track)-1][1]))
        self.svgFile.add(self.svgFile.polyline(points = self.track, stroke = svgwrite.rgb(self.r, self.g, self.b, '%'), stroke_width= self.penStatus, fill = 'none'))

    def SetY(self, y):
        self.track.append((self.track[len(self.track)-1][0], y))
        self.svgFile.add(self.svgFile.polyline(points = self.track, stroke = svgwrite.rgb(self.r, self.g, self.b, '%'), stroke_width= self.penStatus, fill = 'none'))
    
    def Home(self):
        self.track.append(self.initialPoint)
        self.svgFile.add(self.svgFile.polyline(points = self.track, stroke = svgwrite.rgb(self.r, self.g, self.b, '%'), stroke_width= self.penStatus, fill = 'none'))

    def PenDown(self):
        self.penStatus = 1

    def PenUp(self):
        self.penStatus = 0

    def SetPenColor(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b