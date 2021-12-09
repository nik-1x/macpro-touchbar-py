import PyTouchBar
from tkinter import *

root = Tk()
PyTouchBar.prepare_tk_windows(root)

root.title("PIN")
root.geometry("400x400")
root.focus()


lbl = Label(root, text="Enter pin code on touch bar.")
lbl.pack()

now_item = 5
pin_entered = ""

def scroll(stepper):
    global now_item
    now_item = int(stepper.value)


def add_button(button):
    global now_item, pin_entered
    pin_entered += str(now_item)


def finish_button(button):
    global pin_entered
    print(pin_entered)
    pin_entered = ""

text1_ = PyTouchBar.TouchBarItems.Label(text='Enter pin:')
scroll_ = PyTouchBar.TouchBarItems.Stepper(min=0, max=9, action=scroll)
add_button_ = PyTouchBar.TouchBarItems.Button(title='+', action=add_button)
finish_button_ = PyTouchBar.TouchBarItems.Button(title='Finish', action=finish_button)

PyTouchBar.set_touchbar([
    text1_,
    scroll_,
    add_button_,
    finish_button_
])

root.mainloop()
