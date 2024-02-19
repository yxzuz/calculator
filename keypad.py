import tkinter as tk
from tkinter import ttk


# TODO Keypad should extend Frame so that it is a container
class Keypad(tk.Frame):

    def __init__(self, parent, keynames=[], columns=1, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        # keynames and columns
        self.keynames = keynames
        self.init_components(columns)

    def init_components(self, columns) -> None:
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        """
        for i, key in enumerate(self.keynames):
            button = tk.Button(self, text=key, width=1, height=2)
            row = i // columns
            col = i % columns
            button.grid(row=row, column=col, sticky=tk.NSEW, padx=2, pady=2)
        for row in range(row + 1):
            self.grid_rowconfigure(row, weight=1)  # Set weight for each row
        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)  # Set weight for each column

    def bind(self, todo, event='<Button>'):
        """Bind an event handler to an event sequence."""
        # Write a bind method with exactly the same parameters
        # as the bind method of Tkinter widgets.
        # Use the parameters to bind all the buttons in the keypad
        # to the same event handler.
        for button in self.winfo_children():
            button.bind(event, todo, add=None)

    def rebind(self, l_button, todo):
        for button in self.winfo_children():
            if button['text'] in l_button:
                button.unbind("<Button-1>")
                # Bind the event to the second button
                button.bind("<Button-1>", todo)

    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.

        Example: keypad['foreground'] = 'red'
        sets the font color on all buttons to red.
        """
        for button in self.winfo_children():
            button[key] = value

    # def __getitem__(self, key):
    #     """Overrides __getitem__ to allow reading of configuration values
    #     from buttons.
    #     Example: keypad['foreground'] would return 'red' if the button
    #     foreground color is 'red'.
    #     """
    #     for button in self.winfo_children():
    #         return button.cget(key)

    @property
    def frame(self):
        return super()

    # Write a property named 'frame' the returns a reference to
    # the superclass object for this keypad.
    # This is so that a programmer can set properties of a keypad's frame,
    # e.g. keypad.frame.configure(background='blue')

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.

        To configure properties of the frame that contains the buttons,
        use `keypad.frame.configure()`.
        """
        self.frame.configure(cnf, **kwargs)



