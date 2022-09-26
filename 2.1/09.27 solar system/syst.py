import drawSvg as draw



d  =draw.Drawing(900, 800, origin='center',fill='red')
bg= draw.Circle(-11,1,900,fill='#000000')
d.append(bg)
# background

s = draw.Circle(0, 0, 20, fill='yellow')


d.append(s) # Вывод Солнца 0



ellipse = draw.Path()
ellipse.M(-60, 0)
ellipse.A(50, 50, 150, True, True, 60, 0) 
ellipse.A(50, 50, 150, True, True, -60, 0)
ellipse.Z()
m = draw.Circle(0, 0, 4,fill='#2F4F4F')

m.appendAnim(draw.AnimateMotion(ellipse, '9s',
 repeatCount='indefinite'))

d.append(m)  #Вывод Меркурия на орбиту (1 планета)




ellipse = draw.Path()
ellipse.M(-90, 0)
ellipse.A(70, 70, 190, True, True, 90, 0) 
ellipse.A(70, 70, 190, True, True, -90, 0)
ellipse.Z()
v = draw.Circle(0, 0, 6,fill='#DAA520')

v.appendAnim(draw.AnimateMotion(ellipse, '13s',
 repeatCount='indefinite'))

d.append(v) # Вывод Венеры на орбиту (2 планета)




ellipse = draw.Path()
ellipse.M(-130, 0)
ellipse.A(110, 110, 190, True, True, 130, 0) 
ellipse.A(110, 110, 190, True, True, -130, 0)
ellipse.Z()
z = draw.Circle(0, 0, 7,fill='#00BFFF')

z.appendAnim(draw.AnimateMotion(ellipse, '15s',
 repeatCount='indefinite'))

d.append(z) # Вывод Земли на орбиту (3 планета)




ellipse = draw.Path()
ellipse.M(-160, 0)
ellipse.A(150, 150, 210, True, True, 160, 0) 
ellipse.A(150, 150, 210, True, True, -160, 0)
ellipse.Z()
m = draw.Circle(0, 0, 6,fill='#FF4500')

m.appendAnim(draw.AnimateMotion(ellipse, '16s',
 repeatCount='indefinite'))

d.append(m) # Вывод Марса на орбиту (4 планета)




ellipse = draw.Path()
ellipse.M(-195, 0)
ellipse.A(170, 170, 230, True, True, 195, 0) 
ellipse.A(170, 170, 230, True, True, -195, 0)
ellipse.Z()
up = draw.Circle(0, 0, 15,fill='#F4A460')

up.appendAnim(draw.AnimateMotion(ellipse, '19s',
 repeatCount='indefinite'))

d.append(up) # Вывод Юпитер на орбиту (5 планета)




ellipse = draw.Path()
ellipse.M(-240, 0)
ellipse.A(190, 190, 250, True, True, 240, 0) 
ellipse.A(190, 190, 250, True, True, -240, 0)
ellipse.Z()
sat = draw.Circle(0, 0, 13,fill='#FF4500')

sat.appendAnim(draw.AnimateMotion(ellipse, '20s',
 repeatCount='indefinite'))

d.append(sat) # Вывод Сатурн на орбиту (6 планета)




ellipse = draw.Path()
ellipse.M(-270, 0)
ellipse.A(210, 210, 270, True, True, 270, 0) 
ellipse.A(210, 210, 270, True, True, -270, 0)
ellipse.Z()
ur = draw.Circle(0, 0, 11,fill='#87CEEB')

ur.appendAnim(draw.AnimateMotion(ellipse, '23s',
 repeatCount='indefinite'))

d.append(ur) # Вывод Уран на орбиту (7 планета)




ellipse = draw.Path()
ellipse.M(-300, 0)
ellipse.A(230, 230, 290, True, True, 300, 0) 
ellipse.A(230, 230, 290, True, True, -300, 0)
ellipse.Z()
n = draw.Circle(0, 0, 9,fill='#A0522D')

n.appendAnim(draw.AnimateMotion(ellipse, '26s',
 repeatCount='indefinite'))

d.append(n) # Вывод Нептун на орбиту (8 планета)

d.saveSvg('sys.svg') 
