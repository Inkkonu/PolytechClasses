from tkinter import *

# function definition
def draw_point(canvas: Canvas, x: int, y: int, color: str="black") -> None:
    canvas.create_rectangle(x, y, x, y, fill=color, width=0)


def draw_segment(canvas: Canvas, xA: int, yA: int, xB: int, yB: int, color: str='black') -> None:
    x = (xA + xB)//2
    y = (yA + yB)//2

    draw_point(canvas, x, y, color)

    if abs(xA-xB) > 1 or abs(yA - yB) > 1:
        draw_segment(canvas, xA, yA, x, y, color)
        draw_segment(canvas, x, y, xB, yB, color)


def sierpinski(canvas: Canvas, n: int, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> None:
    if n <= 1:
        draw_segment(canvas, x1, y1, x2, y2)
        draw_segment(canvas, x2, y2, x3, y3)
        draw_segment(canvas, x3, y3, x1, y1)
    else:
        mx1 = (x1+x2)//2
        my1 = (y1+y2)//2

        mx2 = (x2 + x3) // 2
        my2 = (y2 + y3) // 2

        mx3 = (x3 + x1) // 2
        my3 = (y3 + y1) // 2

        sierpinski(canvas, n-1, x1, y1, mx1, my1, mx3, my3)
        sierpinski(canvas, n - 1, mx1, my1, x2, y2, mx2, my2)
        sierpinski(canvas, n - 1, mx3, my3, mx2, my2, x3, y3)


# window creation
window = Tk()

# canvas creation
w = Canvas(window, width=400, height=300)
w.pack()

# drawing functions
# put your own drawing below
sierpinski(w, 10, 10, 300, 410, 300, 210, 10)

# main event loop to allow interaction
mainloop()
