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

    def button_handler(self, event):
        self.model.remove_blank()
        print(self.model.history)
        txt = event.widget['text']
        # print(self.model.track)
        current_txt = self.view.box.get("1.0", "end-1c")
        if txt == 'CLR':
            self.view.clear_display()
            self.model.reset()
            # print(self.model.history)
        elif txt == 'DEL':
            self.view.delete()
            # self.model.unroll.pop()
            # print('t',self.model.track)
            # print('u',self.model.unroll)

        elif txt == '=':
            ans = self.model.solve(current_txt)
            if ans is not None:
                new_txt = '=' + str(ans)
                self.view.set_display(new_txt)  # TODO after get reesult add the eq t histpry
                equation = self.view.get_current_display()
                # if self.model.track != 0:
                #     self.model.unroll.append(self.model.track[0])
                    # self.model.unroll += self.model.track
                self.model.save_history(equation,self.model.unroll)


            else:
                self.view.error()  # TODO play sound and reset then chang color back to yellow

        else:
            self.notify_model(txt)
        # state = self.change_state() #rn

    def notify_model(self,txt):
        # print('button',txt)
        self.model.remove_blank()
        new_state = self.model.find_current_state()
        # print('n',new_state)
        self.model.set_state(new_state)
        # print('s',self.model.state)
        # self.model.unroll.append(txt)
        # print(676767,txt)
        if txt in CalculatorUI.operators:
            print('notify')
            new_state = self.model.find_current_state()
            print(new_state)
            self.model.set_state(new_state)
            self.model.unroll.append(txt)
        else:
            self.model.track.append(txt)


        # if self.model.track[0] in CalculatorUI.operators:
        #     print('ok')
        #
        #     self.model.set_state(txt)
        #     self.model.unroll.append(txt)
        #     self.model.track.clear()
        print('track2', self.model.track)
        print('unroll2',self.model.unroll)
        print('state2',self.model.state)
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
            self.view.clear_display()
            self.view.set_display(new_txt)
        else:
    #     #case1
            print('454545454case1')
            print(button)
            new_txt = current_txt + f'{button}('
            self.view.clear_display()
            self.view.set_display(new_txt)
            # self.model.unroll.append(f'{button}(')
            # self.model.unroll[-1] = new_txt





        # self.model.remove_blank()
        # button = event.widget['text']
        #
        # new_state = self.model.find_current_state()
        # self.model.set_state(new_state)
        # current = self.view.get_current_display()
        #
        # if current != '':
        #     #case1
        #     if current[-1] in CalculatorUI.math_fn + CalculatorUI.operators:
        #         print('454545454case1')
        #         print(button)
        #         new_txt = current + f'{button}('
        #         self.view.clear_display()
        #         self.view.set_display(new_txt)
        #         self.model.unroll.append(f'{button}(')
        #
        #
        #     if len(self.model.unroll)>= 3:
        #         if self.model.unroll[-2] in CalculatorUI.operators and self.model.state != '':
        #             print('case3')
        #             num = f'{self.model.unroll[len(self.model.unroll)-3]}{self.model.unroll[len(self.model.unroll)-2]}{self.model.state}'
        #             new_state = f'{button}({num})'
        #             self.view.clear_display()
        #             new_txt = current.replace(num,new_state)
        #             self.view.set_display(new_txt)
        #             self.model.set_state(new_state)
        #
        #     # case 2
        #     elif self.model.floatable(self.model.state):
        #         print('case2')
        #         new_state = f'{button}({self.model.state})'
        #         print(new_state)
        #         new_txt = current.replace(self.model.state,new_state)
        #         self.view.clear_display()
        #         self.view.set_display(new_txt)
        #         self.model.unroll[-1] = new_txt
        #     # print('state2',self.model.state)
        #     print(self.model.track,2)
        #     print(self.model.unroll,2)









    # def combobox_handler(self, event):

    #     self.model.remove_blank()
    #     button = event.widget['text']
    #     # if len(self.model.track):
    #     #     self.model.unroll.append(self.model.unroll[0])
    #     new_state = self.model.find_current_state()
    #     self.model.set_state(new_state)
    #     current = self.view.get_current_display()
    #
    #     if current != '':
    #         #case1
    #         if current[-1] in CalculatorUI.math_fn + CalculatorUI.operators:
    #             print('454545454case1')
    #             print(button)
    #             new_txt = current + f'{button}('
    #             self.view.clear_display()
    #             self.view.set_display(new_txt)
    #             self.model.unroll.append(f'{button}(')
    #
    #
    #         if len(self.model.unroll)>= 3:
    #             if self.model.unroll[-2] in CalculatorUI.operators and self.model.state != '':
    #                 print('case3')
    #                 num = f'{self.model.unroll[len(self.model.unroll)-3]}{self.model.unroll[len(self.model.unroll)-2]}{self.model.state}'
    #                 new_state = f'{button}({num})'
    #                 self.view.clear_display()
    #                 new_txt = current.replace(num,new_state)
    #                 self.view.set_display(new_txt)
    #                 self.model.set_state(new_state)
    #
    #         # case 2
    #         elif self.model.floatable(self.model.state):
    #             print('case2')
    #             new_state = f'{button}({self.model.state})'
    #             print(new_state)
    #             new_txt = current.replace(self.model.state,new_state)
    #             self.view.clear_display()
    #             self.view.set_display(new_txt)
    #             self.model.unroll[-1] = new_txt
    #         # print('state2',self.model.state)
    #         print(self.model.track,2)
    #         print(self.model.unroll,2)





        # print(self.model.track)
        # print(self.model.unroll)
        # print('---')

    def run(self):
        self.view.run()

    # def button_handler(self, event):
    #     txt = event.widget['text']
    #     current_txt = self.view.box.get("1.0", "end-1c")
    #     self.view.box.config(state="normal")
    #     if txt == 'CLR':
    #         self.view.clear_display()
    #         # self.view.box.delete('1.0', 'end')
    #     elif txt == 'DEL':
    #         new_txt = current_txt[: -1]
    #         self.view.box.delete('1.0', 'end')
    #         self.view.box.insert('end', new_txt)
    #     elif txt == '=':
    #         ans = self.model.solve(current_txt)
    #         if ans or ans == 0:
    #             new_txt = '=' + str(ans)
    #             self.view.box.insert('end', new_txt)#TODO after get reesult add the eq t histpry
    #         else:
    #             print('error')
    #             self.error() #TODO play sound and reset then chang color back to yellow
    #     # elif txt != '%':
    #     #
    #     else:
    #         print('hell')
    #         self.view.box.insert('end', txt)
    #     self.view.box.tag_add("right", 1.0, "end")
    #     self.view.box.config(state="disabled")
    # def combobox_handler(self, event):
    #     #TODO close the paren by itself
    #     txt = event.widget['text']
    #     print(6666,txt)
    #     # txt = event.widget.get()
    #     current = self.view.get_current_display()
    #     # print(current[-1])
    #     # current = self.view.box.get("1.0", "end-1c")
    #     if txt != '**':
    #
    #         # if not self.model.floatable(current[-1]):
    #         #     txt += '('
    #     self.view.set_display(txt)
    #     # self.view.box.config(state="normal")
    #     # self.view.box.insert('end', txt)
    #     # self.view.box.tag_add("right", 1.0, "end")
    #     # self.view.box.config(state="disabled")
    # def get_num(self, num=0):
    #     #get num before operators
    #     temp = []
    #     eq = self.view.box.get("1.0", "end-1c")
    #     for index in range(len(eq)-1,-1,-1):
    #         if self.floatable(eq[index]):
    #             temp.append(eq[index])
    #
    #     return reversed(temp)


# if __name__ == '__main__':
#     x = Controller()
#     x.run()






#MODEL
#EXIST ON ITS OWN