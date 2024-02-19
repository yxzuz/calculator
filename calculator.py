"""module for model in mvc"""
import math


class Model():
    """This class saves data and manipulate them"""

    def __init__(self):
        self._history = []  # keep eq track, unroll (dict of)
        self.current_info = {'eq': ''}

    @property
    def history(self) -> list:
        """history getter"""
        return self._history

    @staticmethod
    def is_evaluable(expression: str) -> bool:
        """check whether if the expression is evaluable by eval function"""
        try:
            eval(expression)
            return True
        except Exception:
            return False

    def solve(self, equation: str):
        """try solving expression and return the answer"""
        new_eq = equation.replace('sqrt', 'math.sqrt').replace('ln', 'math.log').\
            replace('exp', 'math.exp').replace('log10', 'math.log10').replace(
            'log2', 'math.log2')
        if self.is_evaluable(new_eq):
            ans = eval(new_eq)
            if ans < 1e-5 or ans > 10 ** 7:
                return f'{ans:.5g}'
            return f'{ans:.5f}'
        return None

    # def floatable(self, string: str) -> bool:
    #     """check if str (val) can convert to float, otherwise the value is invalid"""
    #     try:
    #         if float(string):
    #             return True
    #     except ValueError:
    #         return False

    def save_history(self, equation: str):
        """saving hequation into history """
        self.current_info = {'eq': equation}
        self._history.append(self.current_info)
