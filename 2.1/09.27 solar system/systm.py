import drawSvg as draw

d=draw.Drawing(900,1000,origin='center',)
bg= draw.Circle(-11,1,900,fill='#000000')
d.append(bg)

sun=draw.Circle(10,20,25,fill='yellow')#Солнце
d.append(sun)

class Planet(object):
    
    def __init__(self,size,color,renge,pos):
        self.size=size
        self.color=color
        self.renge=renge
        self.pos=pos

    def Draw_plan(self):
        ellipse = draw.Path()
        ellipse.M(-self.pos, 0)
        ellipse.A(self.pos, self.pos, 0, False, False, self.pos, 0)  
        ellipse.A(self.pos, self.pos, 0, False, False, -self.pos, 0)
        ellipse.Z()

        m = draw.Circle(0,0, self.size, fill=self.color)
        m.appendAnim(draw.AnimateMotion(ellipse, self.renge, repeatCount='indefinite'))
        d.append(m)


Mercury=Planet(10,"gray", "8s",90)
Mercury.Draw_plan()

Venus=Planet(10,"#00BFFF","10s", 130)
Venus.Draw_plan()

Earth=Planet(15,"#00BFFF", "15s",170)
Earth.Draw_plan()

Mars = Planet(15, "#FF4500", "20s", 210)
Mars.Draw_plan()

Jupiter = Planet(24, "#F4A460", "24s", 260)
Jupiter.Draw_plan()

Saturn = Planet(17, "#FF4500", "40s", 320)
Saturn.Draw_plan()

Uran = Planet(20, "#87CEEB", "45s", 370)
Uran.Draw_plan()

Neptun = Planet(25, "#A0522D", "60s", 420)
Neptun.Draw_plan()

        
        




d.saveSvg('syst.svg')
