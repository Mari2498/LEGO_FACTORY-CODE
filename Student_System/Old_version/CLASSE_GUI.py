import tkinter as tk
import tkinter.font as font
from tkinter import ttk
import json
import datetime
import time


class GUI():

    def __init__(self):
        self.root = tk.Tk()
        #load setup file (JSON fomat)
        setup_file = open("GUI_SETUP.txt")
        self.setup = json.load(setup_file)
        setup_file.close()
        #Set attributes
        self.root_setup = self.setup["root"]
        self.root_title = self.root_setup["title"]
        self.root_height = self.root_setup["height"]
        self.root_width = self.root_setup["width"]
        self.root_table = self.root_setup["table"]
        self.root_buttons = self.root_setup["buttons"]
        #Set GUI parameters
        self.root.title(self.root_title)
        self.root.geometry("%dx%d+0+0" % (self.root_width, self.root_height))
        self.root.resizable(False, False)
        #Initialize GUI variables
        self.scroll_table_rows = 0


    #Function to prevent resizing of the table columns
    def handle_click(self, event):
        if self.log_table.identify_region(event.x, event.y) == "separator":
            return "break"

    def attach_root_table(self):
        #table:
        #FRAME:
        self.table_frame = tk.Frame(self.root)
        self.table_frame.pack(side ="right",
                              pady = self.root_table["pad_y"],
                              padx = self.root_table["pad_x"])
        #TABLE CONFIG
        self.log_table = ttk.Treeview(self.table_frame, height=self.root_table["table_rows"])

        self.table_style = ttk.Style()
        self.table_style.configure("Treeview.Heading",
                                   font=(None, self.root_table["font_dim"]))
        self.table_style.configure("Treeview",
                                   rowheight = self.root_table["rows_height"],
                                   font=(None, self.root_table["font_dim"]))

        self.log_table["columns"] = ("Log", "Time")

        self.log_table.column("#0", width=0, stretch=False)
        self.log_table.column("Log", width=self.root_table["log_width"])
        self.log_table.column("Time", width=self.root_table["time_width"])

        self.log_table.heading("#0", text="")
        self.log_table.heading("Log", text="Log")
        self.log_table.heading("Time", text="Time")

        self.log_table.bind('<Button-1>', self.handle_click)

        self.log_table.grid(row=0, column=0)

        #SCROLL BAR CONFIG
        self.scrollbar = ttk.Scrollbar(self.table_frame, orient=tk.VERTICAL, command=self.log_table.yview)
        self.log_table.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

    def insert_table_data(self, log_value):

        self.current_datetime = datetime.datetime.now()
        self.current_datetime_f = self.current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        self.log_table.insert("", tk.END, values=(log_value,self.current_datetime_f ))
        #"" = doesn,t show 0 column
        self.log_table.yview(self.scroll_table_rows)
        self.scroll_table_rows += 1


    def start_function(self):
        print("start button pressed")
        self.insert_table_data("start button pressed")


    def stop_function(self):
        print("stop button pressed")
        self.insert_table_data("stop button pressed")

    def show_data(self, data):
        print("data printed on table!")
        self.insert_table_data(data)

    def attach_root_buttons(self):
        #buttons:
        #FRAME BUTTONS
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(side ="left")
        #START BUTTON CONFIG
        self.start_button = tk.Button(self.buttons_frame,
                                 text="Start TEST",
                                 bg="green",
                                 command = self.start_function)
        self.start_button["font"] = font.Font(size=self.root_buttons["font_dim"])
        self.start_button.config(height=self.root_buttons["height"],
                            width=self.root_buttons["width"])
        self.start_button.grid(row=0,
                          column=0,
                          pady= self.root_buttons["pad_y"],
                          padx = self.root_buttons["pad_x"])
        #STOP BUTTON CONFIG
        self.stop_button = tk.Button(self.buttons_frame,
                                text="Stop TEST",
                                bg="red",
                                command = self.stop_function)
        self.stop_button["font"] = font.Font(size=self.root_buttons["font_dim"])
        self.stop_button.config(height=self.root_buttons["height"],
                           width=self.root_buttons["width"])
        self.stop_button.grid(row=1,
                         column=0,
                         pady= self.root_buttons["pad_y"],
                         padx = self.root_buttons["pad_x"])


    def start_GUI(self):
        self.attach_root_table()
        self.attach_root_buttons(func_input)
        self.root.mainloop()


if __name__ == "__main__":
    gui = GUI()
    gui.start_GUI()
