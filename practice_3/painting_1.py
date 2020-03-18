import graphics as gr

window = gr.GraphWin("Beach Bitch Project", 500, 500)

def draw_sky():
    sky = gr.Line(gr.Point(0, 150), gr.Point(500, 150))
    sky.setWidth(300)
    sky.setOutline('#4097D5')

    sky.draw(window)

def draw_rays():
    ray1 = gr.Line(gr.Point(0, 250), gr.Point(250, 300))
    ray2 = gr.Line(gr.Point(250, 300), gr.Point(250, 0))
    ray3 = gr.Line(gr.Point(250, 300), gr.Point(500, 0))
    ray4 = gr.Line(gr.Point(250, 300), gr.Point(0, 0))
    ray5 = gr.Line(gr.Point(250, 300), gr.Point(500, 250))
    ray1.setWidth(50)
    ray2.setWidth(50)
    ray3.setWidth(50)
    ray4.setWidth(50)
    ray5.setWidth(50)
    ray1.setFill('#FFD201')
    ray2.setFill('#FFD201')
    ray3.setFill('#FFD201')
    ray4.setFill('#FFD201')
    ray5.setFill('#FFD201')

    ray1.draw(window)
    ray2.draw(window)
    ray3.draw(window)
    ray4.draw(window)
    ray5.draw(window)

def draw_circle_sun():
    sun = gr.Circle(gr.Point(250, 300), 80)
    sun.setFill('#FFA500')

    sun.draw(window)

def draw_sun_eyes():
    eye1 = gr.Circle(gr.Point(225, 270), 20)
    eye2 = gr.Circle(gr.Point(275, 270), 15)
    eye1_center = gr.Circle(gr.Point(225, 270), 8)
    eye2_center = gr.Circle(gr.Point(275, 270), 7)
    eye1.setFill('red')
    eye2.setFill('red')
    eye1_center.setFill('black')
    eye2_center.setFill('black')

    eye1.draw(window)
    eye2.draw(window)
    eye1_center.draw(window)
    eye2_center.draw(window)

def draw_sun_eyebrows():
    eyebrow1 = gr.Line(gr.Point(210, 242), gr.Point(245, 262))
    eyebrow2 = gr.Line(gr.Point(255, 265), gr.Point(290, 245))
    eyebrow1.setWidth(10)
    eyebrow2.setWidth(10)
    eyebrow1.setOutline('black')
    eyebrow2.setOutline('black')

    eyebrow1.draw(window)
    eyebrow2.draw(window)

def draw_sea():
    sea = gr.Line(gr.Point(0, 400), gr.Point(500, 400))
    sea.setWidth(200)
    sea.setOutline('#002D9E')

    sea.draw(window)

def draw_landscape():
    draw_sky()
    draw_rays()
    draw_circle_sun()
    draw_sun_eyes()
    draw_sun_eyebrows()
    draw_sea()

def draw_cloud(x, y, radius):
    cloud1 = gr.Circle(gr.Point(x - radius//4, y - radius//2), radius)
    cloud2 = gr.Circle(gr.Point(x + radius//4, y - radius//2), radius)
    cloud3 = gr.Circle(gr.Point(x, y), radius)
    cloud4 = gr.Circle(gr.Point(x - radius//1.5, y), radius)
    cloud5 = gr.Circle(gr.Point(x + radius//1.5, y), radius)
    cloud1.setFill('white')
    cloud1.setOutline('white')
    cloud2.setFill('white')
    cloud2.setOutline('white')
    cloud3.setFill('white')
    cloud3.setOutline('white')
    cloud4.setFill('white')
    cloud4.setOutline('white')
    cloud5.setFill('white')
    cloud5.setOutline('white')

    cloud1.draw(window)
    cloud2.draw(window)
    cloud3.draw(window)
    cloud4.draw(window)
    cloud5.draw(window)

draw_landscape()
draw_cloud(100, 100, 30)
draw_cloud(400, 150, 30)
draw_cloud(300, 50, 30)

window.getMouse()

window.close()