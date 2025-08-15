import tkinter as tk
from tkinter import messagebox
def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == '+':
            result = num1+num2
        elif operation == '-':
            result = num1-num2
        elif operation == '*':
            result = num1*num2
        elif operation == '/':
            if num2 ==0:
                messagebox.showerror("error","cannot divide by zero.")
                return
            result = num1/num2
        else:
            result="unknown operation"
        result_label.config(text=f"result:{result}")
    except valueerror:
        message.boxshowerror("error","please enter the valid number.")
root=tk.Tk()
root.title("simple calculator")
root.geometry("300x250")
tk.Label(root,text="enter first number:").pack()
entry1=tk.Entry(root)
entry1.pack()
tk.Label(root,text="enter the second number:").pack()
entry2=tk.Entry(root)
entry2.pack()
tk.Label(root,text="choose operation:").pack(pady=5)
tk.Button(root,text="Add(+)", command=lambda:calculate('+')).pack(fill='x',padx=20)
tk.Button(root,text="subtract(-)",command=lambda:calculate('-')).pack(fill='x',padx=20)
tk.Button(root,text="multiply(*)",command=lambda:calculate('*')).pack(fill='x',padx=20)
tk.Button(root,text="divide(/)",command=lambda:calculate('/')).pack(fill='x',padx=20)
result_label=tk.Label(root,text="result:")
result_label.pack(pady=10)
root.mainloop()
        
