import tkinter as tk
from tkinter import END, messagebox
from calculator import Calculator

class CalculatorGUI():

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x400")
        self.root.title('Calculator')
        my_calc = Calculator()

        mainFrame =tk.Frame(self.root) # main frame containing all frames
        mainFrame.columnconfigure(0,weight=3) # calc Frame
        #mainFrame.columnconfigure(1,weight=1) # list of inputs
        #mainFrame.columnconfigure(2,weight=1) # list of results
        mainFrame.rowconfigure(0,weight=1)


        calcFrame = tk.Frame(mainFrame) # calculator frame which contains screen and text
        calcFrame.rowconfigure(0,weight=1) # text screen
        calcFrame.rowconfigure(1,weight=2) # button Frame
        calcFrame.columnconfigure(0,weight=1)
        calcFrame.grid(row=0,column=0,sticky=tk.W+tk.E+tk.S+tk.N)

        buttonFrame = tk.Frame(calcFrame)
        buttonFrame.columnconfigure(0,weight=1)
        buttonFrame.columnconfigure(1,weight=1)
        buttonFrame.columnconfigure(2,weight=1)
        buttonFrame.columnconfigure(3,weight=1)
        buttonFrame.rowconfigure(0,weight=1)
        buttonFrame.rowconfigure(1,weight=1)
        buttonFrame.rowconfigure(2,weight=1)
        buttonFrame.rowconfigure(3,weight=1)
        buttonFrame.rowconfigure(4,weight=1)
        buttonFrame.rowconfigure(5,weight=1)
        buttonFrame.grid(row=1,column=0,sticky=tk.W + tk.E + tk.S + tk.N)
        
        
        button_list = [
            'Clear', 'CE', '%','del',
            '(', ')', '^', '/', '7',
            '8', '9', '*', '4', '5', '6',
            '-', '1', '2', '3', '+',
            '+/-', '0', '.', '='
        ]

        # special keys:
        # Clear, CE, del, +/-, =
        def button_click(event):
            btn = event.widget
            match btn.cget('text'):
                
                case 'Clear':
                    my_calc.clear()
                case 'CE':
                    my_calc.clear_Entry()
                case 'del':
                    my_calc.expr = my_calc.expr[:len(my_calc.expr)-1]
                case '+/-':
                    my_calc.expr = my_calc.expr + '-'
                case '=':
                    
                    
                    s = my_calc.get_Result()
                    if s == 'ERR':
                        messagebox.showerror("Invalid Expression", "Please input a valid expression")
                    else:
                        my_calc.expr = s

                case _:
                    my_calc.expr = my_calc.expr + btn.cget('text')

            text_screen.delete('1.0',END)
            text_screen.insert('1.0',my_calc.expr)
      
            

        for i in range(6):
            for j in range(4):
                button = tk.Button(buttonFrame,text=button_list[4*i + j], font=("Arial",14))
                button.bind('<Button-1>',button_click)
                button.grid(row=i,column=j,sticky=tk.W + tk.E + tk.N + tk.S)

        
        calcFrame.grid_propagate(False)
        text_screen = tk.Text(calcFrame, width=1,height=1)
        text_screen.insert('1.0', my_calc.expr)
        text_screen.grid(row=0,column=0,sticky=tk.W + tk.E + tk.N + tk.S)

        # btn1 = tk.Button(mainFrame,text='calc')
        # btn1.grid(row=0,column=1,sticky=tk.W + tk.E + tk.N + tk.S)
        # btn2 = tk.Button(mainFrame,text='calc2')
        # btn2.grid(row=0,column=2,sticky=tk.W + tk.E + tk.N + tk.S)
        mainFrame.grid_propagate(False)
        mainFrame.pack(expand=True,fill='both')


    def run(self):
        self.root.mainloop()

