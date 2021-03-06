import drawSvg as draw
pic = draw.Drawing(900,800,origin='center',displayInline=False)
bg= draw.Circle(-11,1,900,fill='#00008B')
pic.append(bg)
derevo1 = draw.Rectangle(170,-250,35,230, fill='#8B4513')
pic.append(derevo1)
lis=draw.Circle(185,70,105, fill='red')
pic.append(lis)
lis1=draw.Circle(240,40,90, fill='#8B0000')
pic.append(lis1)
lis2=draw.Circle(135,40,90, fill='#FF4500')
pic.append(lis2)
derevo2 = draw.Rectangle(-245,-250,35,230, fill='#8B4513')
pic.append(derevo2)
liss=draw.Circle(-225,70,115, fill='red')
pic.append(liss)
liss1=draw.Circle(-175,30,105, fill='#8B0000')
pic.append(liss1)
liss2=draw.Circle(-265,30,105, fill='#FF4500')
pic.append(liss2)
ground=draw.Rectangle(-500,-400,1000,185, fill='#008000')
pic.append(ground)
way = draw.Path()
way.M(90, 0)
way.A(90, 30, 360, True, True, 90, 0)  
way.A(90, 40, 360, True, True, -90, 0)
way.Z()
star= draw.Circle(-250,200,4,fill='yellow')
star.appendAnim(draw.AnimateMotion(way,'16s',repeatCount='indefinite'))
pic.append(star)
star1 = draw.Circle(170, 200, 3,fill="yellow")
star1.appendAnim(draw.AnimateMotion(way, '7s', repeatCount='indefinite'))
pic.append(star1)
star2 = draw.Circle(120, 0, 3,fill="yellow")
star2.appendAnim(draw.AnimateMotion(way, '5s', repeatCount='indefinite'))
pic.append(star2)
star3 = draw.Circle(190, -100, 3,fill="yellow")
star3.appendAnim(draw.AnimateMotion(way, '10s', repeatCount='indefinite'))
pic.append(star3)
star4 = draw.Circle(-250, -100, 3,fill="yellow")
star4.appendAnim(draw.AnimateMotion(way, '6s', repeatCount='indefinite'))
pic.append(star4)
pic.saveSvg('Drawing.svg')
pic
