from tkinter import *

root = Tk()
root.title('Simple Calculator')
# root.iconbitmap('/home/ovaixe/Documents/GUI/icons')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, pady=10)



# Function for numbers
def numbers(num):
    current = e.get()
    if current == "" and num == 0:
        pass
    elif current == '-' and num == 0:
        pass
    else:
        e.delete(0, END)
        e.insert(0, current + str(num))




# Function for add
def add():
    first_num = e.get()
    if first_num == '':
        pass
    else:
        nums = first_num.split()
        if len(nums) >= 2:
            pass
        else:
            if first_num == '-':
                pass
            else:
                e.delete(0, END)
                e.insert(0, str(first_num) + " + ")


# Function for subtraction
def sub():
    first_num = e.get()
    nums = first_num.split()
    if len(nums) >= 2:
        pass
    else:
        if first_num == '':
            e.insert(0, str(first_num) + "-")
        elif first_num == '-':
            pass
        else:
            e.delete(0, END)
            e.insert(0, str(first_num) + " - ")


# Function for multiplication
def mul():
    first_num = e.get()
    if first_num == '':
        pass
    else:
        nums = first_num.split()
        if len(nums) >= 2:
            pass
        else:
            if first_num == '-':
                pass
            else:
                e.delete(0, END)
                e.insert(0, str(first_num) + " * ")


# Function for division
def div():
    first_num = e.get()
    if first_num == '':
        pass
    else:
        nums = first_num.split()
        if len(nums) >= 2:   
            pass
        else:
            if first_num == '-':
                pass
            else:
                e.delete(0, END)
                e.insert(0, str(first_num) + " / ")


# Function for equality
def eq():
    global button_eq
    current = e.get()
    nums = current.split()
    if len(nums) <= 2:
        pass
    else:
        e.delete(0, END)
        if nums[1] == "+":
            ans = float(nums[0]) + float(nums[2])
            e.insert(0, ans)
            # button_eq.config(bg='green')
        elif nums[1] == '-':
            ans = float(nums[0]) - float(nums[2])
            e.insert(0, ans)
        elif nums[1] == '*':
            ans = float(nums[0]) * float(nums[2])
            e.insert(0, ans)
        elif nums[1] == '/':
            ans = float(nums[0]) / float(nums[2])
            e.insert(0, ans)


# Function for Clear
def clear():
    e.delete(0, END)



# Row 1
button_7 = Button(root, text='7', padx=25, pady=15, command=lambda: numbers(7))
button_8 = Button(root, text='8', padx=25, pady=15, command=lambda: numbers(8))
button_9 = Button(root, text='9', padx=25, pady=15, command=lambda: numbers(9))
button_mul = Button(root, text='*', width=10, pady=15, bg='#badbf2', command=mul)

button_7.grid(row=1, column=0, pady=10)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_mul.grid(row=1, column=3)


# Row 2
button_4 = Button(root, text='4', padx=25, pady=15, command=lambda: numbers(4))
button_5 = Button(root, text='5', padx=25, pady=15, command=lambda: numbers(5))
button_6 = Button(root, text='6', padx=25, pady=15, command=lambda: numbers(6))
button_div = Button(root, text='/', width=10, pady=15, bg='#badbf2', command=div)

button_4.grid(row=2, column=0, pady=10)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_div.grid(row=2, column=3)


# Row 3
button_1 = Button(root, text='1', padx=25, pady=15, command=lambda: numbers(1))
button_2 = Button(root, text='2', padx=25, pady=15, command=lambda: numbers(2))
button_3 = Button(root, text='3', padx=25, pady=15, command=lambda: numbers(3))
button_sub = Button(root, text='-', width=10, pady=15, bg='#badbf2', command=sub)

button_1.grid(row=3, column=0, pady=10)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_sub.grid(row=3, column=3)


# Row 4
button_0 = Button(root, text='0', padx=25, pady=15, command=lambda: numbers(0))
button_add = Button(root, text='+', padx=25, pady=15, bg='#badbf2', command=add)
button_eq = Button(root, text='=', padx=25, pady=15, bg='#badbf2', command=eq)
clearButton = Button(root, text='Clear', width=10, pady=15, bg='#badbf2', command=clear)

button_0.grid(row=4, column=0, pady=10)
button_add.grid(row=4, column=1)
button_eq.grid(row=4, column=2)
clearButton.grid(row=4, column=3)




root.mainloop()