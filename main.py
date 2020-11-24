from tkinter import*
from decimal import*


root = Tk() # окно
root.title('Calculator') # заголовок

buttons = (('7', '8', '9', '/', '4'),  # кортеж кнопок
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4')
           )

activeStr = '' # хренение набираемого числп
stack = []     # список - стек для добавления чисел и операций, которые надо совершить


# Вычисление результата
# Функция calculate получает из списка stack операнды и операцию которую над ними надо произвести.
# Результат отображается в надписи label. Получать из списка строки будем с помощью метода pop.

def calculate():
    global stack
    global label
    result = 0
    operand2 = Decimal(stack.pop())
    operation = stack.pop()
    operand1 = Decimal(stack.pop())

    if operation == '+':
        result = operand1 + operand2
    if operation == '-':
        result = operand1 - operand2
    if operation == '/':
        result = operand1 / operand2
    if operation == '*':
        result = operand1 * operand2
    label.configure(text=str(result))

# В функции click выполняется обработка нажатой клавиши.
# В качестве ее аргумента передается текст, отображаемый на кнопке, которую нажали.
# В списке с операторами и командами для калькулятора не обязательно их будет 3. Но при обработке с помощью метода pop,
# будут рассматриваться 3 последних введенных значения. А после проведения расчета список очистится.
# Далее в него добавляется полученный результат,
# на случай если пользователь нажмет на калькуляторе клавишу операции сразу, а не будет вводить новое число.


def click(text):
    global activeStr
    global stack
    if text == 'CE':
        stack.clear()
        activeStr = ''
        label.configure(text='0')
    elif '0' <= text <= '9':
        activeStr += text
        label.configure(text=activeStr)
    elif text == '.':
        if activeStr.find('.') == -1:
            activeStr += text
            label.configure(text=activeStr)
    else:
        if len(stack) >= 2:
            stack.append(label['text'])
            calculate()
            stack.clear()
            stack.append(label['text'])
            activeStr = ''
            if text != '=':
                stack.append(text)
        else:
            if text != '=':
                stack.append(label['text'])
                stack.append(text)
                activeStr = ''
                label.configure(text='0')

# Теперь займемся оформлением внешнего вида калькулятора и зададим обработку нажатия кнопок.
# Создаем надпись для вывода набираемых значений и результатов. В цикле создаем кнопки. Расположение кнопок
# и надписи осуществляется в табличном виде с помощью упаковщика grid.
# И в завершении запускаем цикл обработки событий mainloop.


label = Label(root, text='0', width=35)
label.grid(row=0, column=0, columnspan=4, sticky="nsew")

button = Button(root, text='CE', command=lambda text='CE': click(text))
button.grid(row=1, column=3, sticky="nsew")
for row in range(4):
    for col in range(4):
        button = Button(root, text=buttons[row][col],
                command=lambda row=row, col=col: click(buttons[row][col]))
        button.grid(row=row + 2, column=col, sticky="nsew")

root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(4, weight=1)

root.mainloop()
