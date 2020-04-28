from graph import*



penColor('black')
brushColor('black')
rectangle(0, 0, 794, 1123)

penColor(100, 100, 100)
brushColor(100, 100, 100)
rectangle(0, 0, 794, 300)

penColor('white')
brushColor('white')
circle(420, 80, 45)

penSize(25)
penColor(200, 200, 200)
p = [(240, 90), (220, 80), (240, 70), (300, 68), (360, 70), (380, 80), (360, 90), (300, 92), (240, 90), (220, 80)]
polyline(p)

penSize(25)
penColor(80, 80, 80)
p = [(200, 90+30), (180, 80+30), (200, 70+30), (260, 68+30), (320, 70+30), (340, 80+30), (320, 90+30), (260, 92+30), (200, 90+30), (180, 80+30)]
polyline(p)

penSize(1)
penColor(80, 60, 0)
brushColor(80, 60, 0)
rectangle(30, 180, 270, 500)

penColor('black')
brushColor('black')
polygon(points = [(10, 180), (290, 180), (270, 150), (30, 150)])



run()
