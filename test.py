import PyTouchBar
from tkinter import *

root = Tk()
PyTouchBar.prepare_tk_windows(root)

root.title("PIN")
root.geometry("400x400")
root.focus()

lbl = Label(root, text="Enter pin code on touch bar.")
lbl.pack()

sv = StringVar(value="_ _ _ _")
lbl1 = Label(root, textvariable=sv)
lbl1.config(font=("Arial", 44))
lbl1.pack()
now_item = {}

sv_trust = StringVar(value="Press to check pin")
lbl_trust = Label(root, textvariable=sv_trust)

def accept_btn():
    global now_item, sv_trust
    pin_ = now_item[1] + now_item[2] + now_item[3] + now_item[4]
    def correct_pin_action(pin):
        sv_trust.set("Pin is correct")
        if pin == "0000":
            pin_l = Entry(root, textvariable=StringVar(value="+88005553535:12345qwerty"))
            pin_l.pack()
        if pin == "1111":
            print("Test message")

    correct_pin_action(pin_) if pin_ in ["5810", "0000", "1111"] else sv_trust.set("Pin is incorrect")
    lbl_trust.pack()


class Pins:
    global now_item, sv, root
    num_ = 1
    lbl2 = Button(root, text="Check", width=15, height=3, command=accept_btn)

    def __init__(self, num):
        self.num_ = num

    def createTouchbar(self):
        PyTouchBar.set_touchbar([PyTouchBar.TouchBarItems.Stepper(min=0, max=9, action=Pins(x + 1).update) for x in range(self.num_)])

    def update(self, stepper):
        now_item[self.num_] = str(int(stepper.value))
        sv.set(sv.get()[:({1: 0, 2: 2, 3: 4, 4: 6}[self.num_])] + str(int(stepper.value)) + sv.get()[(({1: 0, 2: 2, 3: 4, 4: 6}[self.num_]) + 1):])
        if len({key: val for key, val in now_item.items() if val != ""}.items()) == 4: self.lbl2.pack()


Pins(4).createTouchbar()
root.mainloop()
