import Data

a = 0
b = 0
sign = ''


def init(num_str):
    global a
    global b
    global sign
    if num_str.find('+') != -1:
        a = int(num_str[0:num_str.find('+'):])
        b = int(num_str[num_str.find('+') + 1::])
        sign = '+'
    elif num_str.find('-') != -1:
        a = int(num_str[0:num_str.find('-'):])
        b = int(num_str[num_str.find('-') + 1::])
        sign = '-'
    elif num_str.find('*') != -1:
        a = int(num_str[0:num_str.find('*'):])
        b = int(num_str[num_str.find('*') + 1::])
        sign = '*'
    elif num_str.find('/') != -1:
        a = int(num_str[0:num_str.find('/'):])
        b = int(num_str[num_str.find('/') + 1::])
        sign = '/'
    answer = calc()
    Data.give_Answer(answer)
 
    

def calc():
    if sign == '+':
        return a + b
    elif sign == '-':
        return a - b
    elif sign == '*':
        return a * b
    elif sign == '/':
        if b == 0:
            ValueError('Делить на 0 нельзя')
        else:
            return a / b
    
def get_an_answer():
   answer = Data.get_data()  
   return answer
    
