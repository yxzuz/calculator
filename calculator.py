import math
class Model():

    def __init__(self):
        self._history = [] #keep eq track, unroll (dict of)
        self.current_info = {'eq': '', 'track': []}
        self._track = []
        self._state = ''
        self._unroll = []

    @property
    def state(self):
        return self._state

    def find_current_state(self):
        result = ''.join(string for string in self.track if self.floatable(string) or string == '0')
        self.unroll.append(result)
        self.track.clear()
        return result

    def reset(self):
        self.track.clear()
        self.set_state('')
        self.current_info = {'eq': '', 'track': []}
        self.unroll.clear()
        # self.current_info['eq']= ''
        # self.current_info['track'] = []

        print(self.track,self.state,self.unroll)
    def set_state(self,new_state):
        # use when pressed operator
        # print('cahnge',self.track[0] )
        self._state = new_state

    @property
    def history(self):
        return self._history

    @property
    def track(self):
        return self._track

    @property
    def unroll(self):
        return self._unroll

    # @state.setter
    # def set_state(self): #use when pressed operator
    #     print('cahnge',self.track[0] )
    #     self._state = self.track[0]


    def remove_blank(self):
        for i in self.unroll:
            if i == '':
                self.unroll.remove(i)

    @staticmethod
    def is_evaluable(expression):
        try:
            eval(expression)
            return True
        except Exception:
            return False

    def solve(self, eq):
        # TODO fix error when /0 , paren not close
        #TODO NOT COVERED LOG
        #TODO log 2
        new_eq = eq.replace('sqrt', 'math.sqrt').replace('ln', 'math.log').replace('exp', 'math.exp').replace('log10','math.log10')
        if self.is_evaluable(new_eq):
            # print(3333,eval(new_eq))
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
        self.remove_blank()
        self.current_info = {'eq': eq, 'track': self.unroll}
        self._history.append(self.current_info)
        # print('1',self.current_info)
        # print(2,self._history)








