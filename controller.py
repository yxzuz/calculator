"""this module acts as controller in MVC model and handles user's interaction with UI"""
from calculator_ui import CalculatorUI
from calculator import Model


class Controller():
    """Controller class acts as controller
    by manipulating user's input
    and connect to model and view
    """

    def __init__(self):
        self.model = Model()
        self.view = CalculatorUI(self)

    def get_history(self) -> list:
        """users history"""
        return self.model.history

    def show_history(self) -> list:
        """return histories of equations that user inputs"""
        history_eq = []
        history = self.get_history()
        for equation in history:
            history_eq.append(equation['eq'])
        return history_eq

    def button_handler(self, event):  # for equal
        """handling when user press equal button and some numbers"""
        txt = event.widget['text']
        current_txt = self.view.box.get("1.0", "end-1c")
        if txt == '=':
            ans = self.model.solve(current_txt)
            if ans is not None:
                new_txt = '=' + str(ans)
                self.view.set_display(new_txt)
                equation = self.view.get_current_display()
                self.model.save_history(equation)
            else:
                self.view.error()

        else:
            self.view.set_display(txt)


    def combobox_handler(self, event):
        """handling when user pressed math functions"""
        button = event.widget['text']
        floatable_chars = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        current_txt = self.view.box.get("1.0", "end-1c")
        if current_txt.endswith(floatable_chars):
            # case 2
            new_state = f'{button}({current_txt})'
            new_txt = current_txt.replace(current_txt, new_state)
            self.view.clear_display(event)
            self.view.set_display(new_txt)
        elif '=' in current_txt:
            self.view.error()
        else:
            # case1
            new_txt = current_txt + f'{button}('
            self.view.clear_display(event)
            self.view.set_display(new_txt)

    def run(self):
        """running program"""
        self.view.run()
