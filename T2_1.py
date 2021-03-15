from tkinter import Tk, Canvas, Frame, BOTH

class TransMatr:
    MATR = [[],[]]


class Dot:

    def __init__(self,X,Y):
        self.COORD = [X,Y]


class Cons:

    BOARD_WIDTH = 500
    BOARD_HEIGHT = 500


class Board(Canvas):

    def __init__(self):
        super().__init__(
            width = Cons.BOARD_WIDTH, height = Cons.BOARD_HEIGHT,
            background="white"
        )
        self.pack()
        self.initFigure()
        
    def initFigure(self):
        x1 = 10
        y1 = 10
        x2 = 100
        y2 = 100
        dot1 = Dot(x1,y1)
        dot2 = Dot(x2,y2)
        canvas = Canvas(self)
        self.pack(fill=BOTH, expand=1)
        
        canvas.create_oval(dot1.COORD[0], dot1.COORD[1],
            dot2.COORD[0], dot2.COORD[1])
        #line1
        #canvas.create_line(dot1.COORD[0], dot2.COORD[1], dot1.COORD[1], dot2.COORD[1])
        canvas.create_line(dot1.COORD[0], (dot1.COORD[1]+dot2.COORD[1])/2, dot2.COORD[0], (dot1.COORD[1]+dot2.COORD[1])/2)
        #line2
        canvas.create_line((dot1.COORD[0]+dot2.COORD[0])/2, dot1.COORD[1], (dot1.COORD[0]+dot2.COORD[0])/2, dot2.COORD[1])
        canvas.pack(fill=BOTH, expand=1)
    

    

class Example(Frame):

    def __init__(self):
        super().__init__()
        self.master.title('Task 1')
        self.board = Board()
        self.pack()


     

 
def main():
    root = Tk()
    ex = Example()
    root.mainloop()
 
 
if __name__ == '__main__':
    main()