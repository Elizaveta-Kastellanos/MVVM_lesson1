from distutils.cmd import Command
from sys import maxsize
from turtle import bgcolor
import Model_logic
import tkinter as tk

def get_value():
    expression = text_value.get()
    Model_logic.init(expression)
    return expression

def give_answer():
    answer = Model_logic.get_an_answer()
    text_answer.insert(0,answer)



root = tk.Tk()
root.title('Calculator')
icon = tk.PhotoImage(file='calculator.png')
root.iconphoto(False, icon)
root.config(bg='grey')
root.geometry(f"400x200+{int(root.maxsize()[0]/2) - 150}+{int(root.maxsize()[1]/2) - 150}")
root.resizable(False, False)
tk.Label(root, text='Введите выражение',bg='grey').grid(row=0, column=0)
tk.Label(root,text=f'Пример: 1+10\n2*20 и т.д',bg='grey').grid(row=1, column=0)
text_value = tk.Entry(root, font=('Arial',15))
text_value.grid(row=0,column=1,rowspan=3)
btn_calc = tk.Button(root, text='Calculate', command=get_value)
btn_calc.grid(row=3,column=1, columnspan=2,stick='we')
tk.Label(root,bg='grey').grid(row=4, column=0,columnspan=2,stick='we')
tk.Label(root,text='Answer',bg='grey').grid(row=5, column=0,columnspan=2,stick='we')
btn_answer = tk.Button(root,text='Получить ответ',command=give_answer).grid(row=7,column=0,stick='w')
text_answer = tk.Entry(root, state='normal', font=('Arial',15))
text_answer.grid(row=6, column=0,rowspan=2,columnspan=2)
root.grid_columnconfigure(0,minsize = 200)
root.grid_columnconfigure(1,minsize = 200)
root.mainloop()
