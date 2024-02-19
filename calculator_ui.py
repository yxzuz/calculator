from math import *
import tkinter as tk
from tkinter import ttk
from keypad import Keypad
from pygame import mixer,time
# from controller import Controller
#THE VIEW FOR DISPLAY
#OBSERVER
class CalculatorUI(tk.Tk):
    keys = ['CLR', 'DEL', '%'] + list('7894561230.')
    operators = ['*', '/', '-', '+', '=']
    math_fn = ['(', ')', '**', 'sqrt', 'ln', 'log10', 'log2', 'exp']

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Calculator")
        self.geometry("300x300")
        self.init_components()

    def create_menubar(self):
        # Create a menubar
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        # Create a File menu
        file_menu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Menu", menu=file_menu)

        # Add options to the File menu
        file_menu.add_command(label='History', command=self.history_box)
        file_menu.add_command(label='Exit', command=self.destroy)

    def get_current_display(self):
        return self.box.get('1.0', 'end').replace('\n', '')

    def history_box(self):
        eqs = self.controller.show_history()  # Fetch history from the controller
        window2 = tk.Tk()
        window2.geometry('300x200')
        window2.resizable(False, False)
        window2.title('History preview')
        # label
        label = ttk.Label(window2, text="Please select an equation:")
        label.grid(row=0, column=0, padx=3, pady=3)

        # create a combobox
        selected_eq = tk.StringVar()
        equation_select = ttk.Combobox(window2, textvariable=selected_eq)

        # get first 3 letters of every month name
        equation_select['values'] = eqs

        # prevent typing a value
        equation_select['state'] = 'readonly'

        # place the widget
        equation_select.grid(row=1, column=0, padx=3, pady=3)

        equation_select.bind('<<ComboboxSelected>>', self.display_history)

        window2.mainloop()

    def display_history(self, event):
        selected_equation = event.widget.get()
        print(selected_equation)
        self.clear_display(event) #TODO
        self.set_display(selected_equation)


    def play_sound(self):
        # Initialize Pygame mixer
        mixer.init()

        # Load the sound file
        sound = mixer.Sound('error_sound.mp3')  # Update the path to your sound file

        # Play the sound
        sound.play()

        while mixer.get_busy():
            time.Clock().tick(2)
        sound.stop()

    def init_components(self) -> None:
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        """

        self.create_menubar()

        # display
        self.text = tk.StringVar()
        self.box = tk.Text(self, background='black', fg='yellow', font=('Arial', 40), height=1, width=14)
        self.box.tag_configure('right', justify='right')
        self.box.insert('1.0', '')
        self.box.tag_add("right", 1.0, "end")
        self.box.config(state="disabled")

        keypad = Keypad(self, CalculatorUI.keys, 3)

        keypad.bind(self.controller.button_handler)

        keypad.rebind(['CLR'],self.clear_display) # TODO
        keypad.rebind('DEL',self.delete) # TODO

        operators = Keypad(self, CalculatorUI.operators, 1)

        operators.bind(self.controller.button_handler)

        self.pick_math_fuc = tk.StringVar()
        math_fn_buttons = Keypad(self, CalculatorUI.math_fn, 2)
        math_fn_buttons.bind(self.controller.combobox_handler)
        math_fn_buttons.rebind(['**'], self.controller.button_handler)
        math_fn_buttons.rebind(['(', ')'], self.controller.button_handler)


        self.box.grid(row=0, column=0, sticky="NSEW", columnspan=3)
        math_fn_buttons.grid(row=1, column=0, sticky="NSEW")
        keypad.grid(row=1, column=1, sticky="NSEW")
        operators.grid(row=1, column=2, sticky="NSEW")

        operators.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

    def set_display(self, new_txt):
        # new_txt = event.widget['text']
        self.box.config(state="normal")
        self.box.insert('end', new_txt)

        self.box.tag_add("right", 1.0, "end")
        self.box.config(state="disabled")

    def clear_display(self,event): # TODO event
        self.box.config(state="normal")
        self.box.delete('1.0', 'end')
        self.box.tag_add("right", 1.0, "end")
        self.box.config(fg='yellow')
        self.box.config(state="disabled")

    def error(self):
        self.box.config(fg='red')
        self.play_sound()

    def delete(self,event):# TODO event
        # TODO sqaurt delete whole not just t

        current_txt = self.box.get("1.0", "end-1c")
        for math in CalculatorUI.math_fn:
            if current_txt.endswith(math + '('):
                new_txt = current_txt.replace(math + '(', '')
                self.clear_display(event) # TODO
                self.set_display(new_txt)

                return

        new_txt = current_txt[: -1]
        self.clear_display(event)
        self.set_display(new_txt)

    def run(self):
        self.mainloop()
