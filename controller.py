#event handlers
#BUTTONS DEL PRESSED
#CONTROLLER
from calculator_ui import CalculatorUI
from calculator import Model

class Controller():
    def __init__(self):
        self.model = Model()
        self.view = CalculatorUI(self)


    def get_history(self):
        print('history')
        print(self.model.history)
        return self.model.history

    def show_history(self):
        history_eq = []
        history = self.get_history()
        for eq in history:
            history_eq.append(eq['eq'])
        return history_eq

    def button_handler(self, event): #for equal
        print(self.model.history)
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
            self.notify_model(txt)
    def notify_model(self,txt): ## TODO
        print('button',txt)
        if txt in CalculatorUI.operators:
            print('notify')
        self.view.set_display(txt)


    def combobox_handler(self, event):

        button = event.widget['text']
        floatable_chars = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        current_txt = self.view.box.get("1.0", "end-1c")
        print(current_txt)
        if current_txt.endswith(floatable_chars):
            print('case2')
            new_state = f'{button}({current_txt})'
            print(new_state)
            new_txt = current_txt.replace(current_txt,new_state)
            self.view.clear_display(event)
            self.view.set_display(new_txt)
        elif '=' in current_txt:
            self.view.error()
        else:
            #case1
            print('454545454case1')
            print(button)
            new_txt = current_txt + f'{button}('
            self.view.clear_display(event)
            self.view.set_display(new_txt)

    def run(self):
        self.view.run()