from tkinter import *
from random import *

class Questions:
    def __init__(self):
        print(1)

    def generate(self):
        a = randint(0, 12)
        b = randint(0, 12)
        ans = (a*b)
        return a,b,ans


class TimesTables:
    def __init__(self, parent):
        self.times_table = Questions()

        self.num = self.times_table.generate() #[a, b ,ans]

        f1 = Frame(parent)

        self.q_label = Label(f1, text=f"{self.num[0]} x {self.num[1]}")
        self.q_label.grid(row=0, column=0)

        self.var = StringVar()

        self.q_entry = Entry(f1, textvariable=self.var)
        self.q_entry.grid(row=0, column=1)

        self.check_Ans = Button(f1, text="Check Answer", command=self.check)
        self.check_Ans.grid(row=1, column=0)

        self.next = Button(f1, text="Next", state=DISABLED, command=self.next_q)
        self.next.grid(row=1, column=1)

        self.output_label = Label(parent, text=self.var.get())
        self.output_label.pack()

        f1.pack()


    def check(self):
        try:
            if int(self.var.get()) == self.num[2]:
                self.output_label.configure(text="Correct!")
                self.output_label.configure(font=("Helvetica", 40))
                self.next.configure(state=ACTIVE)
            else:
                if int(self.var.get()) != self.num[2]:
                    self.output_label.configure(text="Incorrect!")
                    self.output_label.configure(font=("Helvetica", 40))
        except:
            self.output_label.configure(text="Incorrect Input!")
            self.output_label.configure(font=("Helvetica", 40))

    def next_q(self):
        self.num = self.times_table.generate()
        self.q_label.configure(text=f"{self.num[0]} x {self.num[1]}")


if __name__ == "__main__":
    root = Tk()
    buttons = TimesTables(root)
    root.mainloop()
