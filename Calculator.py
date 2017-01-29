""" James Grey """
""" Description: A calculator made with a GUI using tkinter """

import sys
from tkinter import *

class Gui:

    main_screen = ["0"]
    sub_screen = []

    operator = ""

    number_1 = 0
    number_2 = 0

    answer = 0

    blank = True
    show_sum = False

    def __init__(self, root):
        self.root = root

        ## initialise frames containers

        ## main frames

        self.screen_frame = Frame(self.root)
        self.screen_frame.pack()

        self.buttons_frame = Frame(self.root)
        self.buttons_frame.pack()

        ## button frames

        self.line_7 = Frame(self.buttons_frame)
        self.line_7.pack()

        self.line_6 = Frame(self.buttons_frame)
        self.line_6.pack()

        self.line_5 = Frame(self.buttons_frame)
        self.line_5.pack()

        self.line_4 = Frame(self.buttons_frame)
        self.line_4.pack()

        self.line_3 = Frame(self.buttons_frame)
        self.line_3.pack()

        self.line_2 = Frame(self.buttons_frame)
        self.line_2.pack()

        self.line_1 = Frame(self.buttons_frame)
        self.line_1.pack()

        ## label text on screens

        self.main_text = Label(self.screen_frame, text = Gui.main_screen)
        self.main_text.pack()

        self.sub_text = Label(self.screen_frame, text = Gui.sub_screen)
        self.sub_text.pack()

        ## buttons for the numbers and functions

        Button(self.line_4, text = "7", command = lambda: self.num_press("7")).pack(side = LEFT)
        Button(self.line_4, text = "8", command = lambda: self.num_press("8")).pack(side = LEFT)
        Button(self.line_4, text = "9", command = lambda: self.num_press("9")).pack(side = LEFT)
        Button(self.line_4, text = "DEL", command = lambda: self.backspace()).pack(side = LEFT)
        Button(self.line_4, text = "AC", command = lambda: self.clear_all()).pack(side = LEFT)

        Button(self.line_3, text = "4", command = lambda: self.num_press("4")).pack(side = LEFT)
        Button(self.line_3, text = "5", command = lambda: self.num_press("5")).pack(side = LEFT)
        Button(self.line_3, text = "6", command = lambda: self.num_press("6")).pack(side = LEFT)
        Button(self.line_3, text = "*", command = lambda: self.operation_press("*")).pack(side = LEFT)
        Button(self.line_3, text = "/", command = lambda: self.operation_press("/")).pack(side = LEFT)

        Button(self.line_2, text = "1", command = lambda: self.num_press("1")).pack(side = LEFT)
        Button(self.line_2, text = "2", command = lambda: self.num_press("2")).pack(side = LEFT)
        Button(self.line_2, text = "3", command = lambda: self.num_press("3")).pack(side = LEFT)
        Button(self.line_2, text = "+", command = lambda: self.operation_press("+")).pack(side = LEFT)
        Button(self.line_2, text = "-", command = lambda: self.operation_press("-")).pack(side = LEFT)

        Button(self.line_1, text = "0", command = lambda: self.num_press("0")).pack(side = LEFT)
        Button(self.line_1, text = ".", command = lambda: self.num_press(".")).pack(side = LEFT)
        Button(self.line_1, text = " ", command = lambda: self.blank_space).pack(side = LEFT)
        Button(self.line_1, text = "ans", command = lambda: self.call_answer()).pack(side = LEFT)
        Button(self.line_1, text = "=", command = lambda: self.equals(Gui.main_screen)).pack(side = LEFT)

    # number button is pressed
    def num_press(self, num):
        if Gui.show_sum == True:
            Gui.main_screen = []
            self.main_text.config(text = Gui.main_screen)
            Gui.show_sum = False
            
        if Gui.blank == True:
            Gui.main_screen[0] = num
            Gui.blank = False
        else:
            Gui.main_screen.append(num)

        self.main_text.config(text = Gui.main_screen)

    # operation button is pressed
    def operation_press(self, char):
        if Gui.show_sum == True:
            Gui.main_screen = []
            self.main_text.config(text = Gui.main_screen)    
            Gui.show_sum = False

        if Gui.blank == True:
            Gui.main_screen[0] = char
            Gui.blank = False

        else: 
            Gui.main_screen.append(char)
            
        self.main_text.config(text = Gui.main_screen)

    def backspace(self):
        if Gui.show_sum == True:
            Gui.main_screen = ["0"]
            self.main_text.config(text = Gui.main_screen)
            Gui.show_sum = False
            
        Gui.main_screen.pop(-1)
        if Gui.main_screen == []:
            Gui.main_screen = ["0"]
            Gui.blank = True
        self.main_text.config(text = Gui.main_screen)

    def clear_all(self):
        if Gui.show_sum == True:
            Gui.main_screen = ["0"]
            self.main_text.config(text = Gui.main_screen)
            Gui.show_sum = False
            
        Gui.main_screen = ["0"]
        Gui.blank = True
        Gui.sub_screen = []
        Gui.answer = []
        self.main_text.config(text = Gui.main_screen)
        self.sub_text.config(text = Gui.sub_screen)

    def call_answer(self):
        if Gui.show_sum == True:
            Gui.main_screen = []
            self.main_text.config(text = Gui.main_screen)    
            Gui.show_sum = False

        if Gui.blank == True:
            Gui.main_screen = Gui.answer
            Gui.blank = False

        else:
            Gui.main_screen.append(Gui.answer)

        self.main_text.config(text = Gui.main_screen)

    def blank_space(self):
        pass
    
    def equals(self, screen_list):
        num_1 = []
        num_2 = []

        ans = 0

        operators = {"+", "-", "*", "/"}

        count = 0
        for char in screen_list:
            count += 1
            # separating strings of numbers
            # from either side of operator
            if char in operators:
                Gui.operator = char

                for i in range(0, count-1):
                   num_1.append(screen_list[i])

                for i in range(count, len(screen_list)):
                    num_2.append(screen_list[i])

        # when = pressed if nothing there
        # 0 = 0
        if num_1 == [] and num_2 == []:
            num_1 = ["0"]
            num_2 = ["0"]

        # i.e. answer to last question was 0
        elif num_1 == [] and Gui.answer == []:
            num_1 = ["0"]

        # use answer from last question in next question
        # carries over to be used
        elif num_1 == []:
            num_1.append(Gui.answer)

        num_1 = float(''.join(map(str, num_1)))
        num_2 = float(''.join(map(str, num_2)))

        if Gui.operator == "+":
            ans = operations.add(num_1, num_2)
               
        elif Gui.operator == "-":
            ans = operations.subtract(num_1, num_2)
               
        elif Gui.operator == "*":
            ans = operations.multiply(num_1, num_2)
               
        elif Gui.operator == "/":
            ans = operations.divide(num_1, num_2)

        # make int if can do so
        if ans %1 == 0:
            ans = int(ans)

        Gui.answer = ans
        num_1 = []
        num_2 = []

        self.sub_text.config(text = Gui.answer)

        ans = 0
        Gui.show_sum = True

class operations:
    def __init__(self):
        pass

    def add(num_1, num_2):
        return(num_1 + num_2)

    def subtract(num_1, num_2):
        return(num_1 - num_2)

    def multiply(num_1, num_2):
        return(num_1 * num_2)

    def divide(num_1, num_2):
        return(num_1 / num_2)


        

def main():
    root = Tk()
    gui = Gui(root)
    root.mainloop()

if __name__ == "__main__":
    sys.exit(main())
