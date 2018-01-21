#!/usr/bin/python3

import tkinter as tk
from tkinter import messagebox

class Myframe:
    '''
    The class of defining the frame of the window
    '''
    def __init__(self):
        # create the window for the project
        self.window = tk.Tk()
        self.window.title('TSP solver')
        self.window.resizable(False,False)    # limit to change the size of the window
        self.window.geometry('1000x600')

        # Init the menu bar for the user
        # We can use the lambda to transfer the prama into the command function
        self.menubar = tk.Menu(self.window)
        self.algorithm_menu = tk.Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = 'Algorithm', menu = self.algorithm_menu)
        self.algorithm_menu.add_command(label = 'GA', command = self.set_GA)
        self.algorithm_menu.add_command(label = 'PSO', command = self.set_PSO)
        self.algorithm_menu.add_command(label = 'Hopfield', command = self.set_Hopfield)
        self.algorithm_menu.add_separator()
        self.algorithm_menu.add_command(label = 'Exit', command = self.window.quit)
        self.window.config(menu = self.menubar)

        # Init the canvas and right frame for the window
        self.frm_r  = tk.Frame(self.window)
        self.frm_r.place(x = 196, y = 0)
        self.canvas = tk.Canvas(self.frm_r, bg = 'white', height = 600, width = 800)
        self.canvas.pack(side = 'left')

        # Init the left frame
        self.frm_l = tk.Frame(self.window)
        self.frm_l.place(x = 0, y = 0)

        # Init the function interface for user
        self.current_algorithm_msg = tk.StringVar()    # current algorithm, default GA
        self.current_algorithm_msg.set('GA')
        self.iterations_msg        = tk.IntVar()
        self.iterations_msg.set(0)    # if the value is -1, refuse to run and give the warning messagebox
        for i in range(7):
            if i == 0 :
                # init the label
                self.current_algorithm     = tk.Label(self.frm_l, textvariable = \
                self.current_algorithm_msg, bg = 'yellow', font = ('Arial', 12), \
                width =24   , height = 3)
                self.current_algorithm.grid(row = i, column = 0)
            elif i == 1:
                # init the button `init the map`
                self.init_map_button = tk.Button(self.frm_l, text = 'Init the map', \
                                     width = 24, height = 3, command = self.init_map)
                self.init_map_button.grid(row = i, column = 0)
            elif i == 2:
                # init the scale iterations setting widget
                # if the 
                self.iteration_scale = tk.Scale(self.frm_l, label = 'Set the iterations',\
                        from_ = 0, to = 3000, orient = tk.HORIZONTAL, length = 190,\
                        showvalue = 1, tickinterval = 1000, resolution = 1, \
                        command = self.set_iterations)
                self.iteration_scale.grid(row = i, column =0)
            elif i == 3:
                # init the button `run`
                self.run_button = tk.Button(self.frm_l, text = 'Search', \
                                     width = 24, height = 3, command = self.init_map)
                self.run_button.grid(row = i, column = 0)
            elif i == 4:
                # init the button `export result`
                self.export_button = tk.Button(self.frm_l, text = 'Export result', \
                                     width = 24, height = 3, command = self.init_map)
                self.export_button.grid(row = i, column = 0)  
            elif i == 5:
                pass
            elif i == 6:
                # init the text widget for result
                pass
        
    def start(self):
        # start the main loop of the window
        self.window.mainloop()
        
    def init_map(self):
        # Init the map for the solver (GA, PSO, Hopfield)
        pass

    def check_iterations(self):
        # the check function for running function
        # OK - True
        # NO - False
        if self.iterations_msg.get() == 0 :
            messagebox.error(title = 'Fatal Error', message = 'Iterations is ' + str(0) + \
                    ', refuse to execute, please reset the iterations !')
            return False
        elif self.iterations_msg.get() < 100 :
            return messagebox.showyesno(title = 'Warning', message = 'Iterations is small, suggest to reset, do you really want to execute ?')
        else:
            return True


    def set_GA(self):
        # ---- Init ---- #
        # 1. change the self.current_algorithm_msg
        self.current_algorithm_msg.set('GA')
        pass

    def set_PSO(self):
        # ---- Init ---- #
        # 1. change the self.current_algorithm_msg
        self.current_algorithm_msg.set('PSO')
        pass

    def set_Hopfield(self):
        # ---- Init ---- #
        # 1. change the self.current_algorithm_msg
        self.current_algorithm_msg.set('Hopfield')
        pass

    def set_iterations(self, value):
        # set iterations, just set
        self.iterations_msg.set(value)

if __name__ == "__main__":
    app = Myframe()
    app.start()