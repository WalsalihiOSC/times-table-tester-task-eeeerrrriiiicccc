from tkinter import *

class TimesTables:
    def __init__(self, parent):

        f1 = Frame(parent)

        self.output_label = Label(f1, text="9 x 3 ")
        self.output_label.grid(row=0, column=0)

        self.q_entry = Entry(f1)
        self.q_entry.grid(row=0, column=1)

        self.check_Ans = Button(f1, text="Check Answer")
        self.check_Ans.grid(row=1, column=0)

        self.next = Button(f1, text="Next")
        self.next.grid(row=1, column=1)

        f1.pack()


if __name__ == "__main__":
    root = Tk()
    buttons = TimesTables(root)
    root.mainloop()
