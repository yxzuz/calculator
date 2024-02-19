import math
class Model():

    def __init__(self):
        self._history = [] #keep eq track, unroll (dict of)
        self.current_info = {'eq': ''}

    @property
    def history(self):
        return self._history


    @staticmethod
    def is_evaluable(expression):
        try:
            eval(expression)
            return True
        except Exception:
            return False

    def solve(self, eq):
        new_eq = eq.replace('sqrt', 'math.sqrt').replace('ln', 'math.log').replace('exp', 'math.exp').replace('log10','math.log10').replace('log2','math.log2')
        if self.is_evaluable(new_eq):
            ans = eval(new_eq)
            if ans < 1e-5 or ans > 10 ** 7:
                return f'{ans:.5g}'
            return f'{ans:.5f}'
        return None



    def floatable(self,string):
        """check if str (val) can convert to float, otherwise the value is invalid"""
        try:
            if float(string):
                return True
        except ValueError:
            return False

    def save_history(self, eq):
        self.current_info = {'eq': eq}
        self._history.append(self.current_info)
        print('1',self.current_info)
        print(2,self._history)




