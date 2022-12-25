import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
from loginWindow import LoginWindow
from registerWindow import RegisterWindow
from client.api.resolvers import get,getAll
import server.sql_base.models

font = ('Arial Bold', 30)
tables = ["user", "Ticket"]

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.login_btn = tk.Button(text="Login", font=font,
                             command=self.open_login)
        self.register_btn = tk.Button(text="Register", font=font,
                             command=self.open_register)
        self.lbl_table = tk.Label(self,text="", font=font)
        self.id = tk.StringVar()

        self.login_btn.grid(row=1, column=0, pady=50, padx=50)
        self.register_btn.grid(row=1, column=1, pady=50, padx=50)

        #self.loginComplete()

    def open_login(self):
        _loginWindow = LoginWindow(self)
        _loginWindow.grab_set()

    def open_register(self):
        _registerWindow = RegisterWindow(self)
        _registerWindow.grab_set()

    def loginComplete(self):
        self.login_btn.destroy()
        self.register_btn.destroy()

        dName = tk.StringVar()
        dName.set(tables[0])
        dropDownList = tk.OptionMenu(self, dName, *tables, command=self.showTabel)
        self.showTabel(tables[0])

        dropDownList.grid(row=0, column=0)

    def showTabel(self, tableSelected):
        self.lbl_table.config(text= f"Таблица {tableSelected}")
        entry_id = tk.Entry(self, textvariable=self.id)
        btn_select = tk.Button(self, text='Выбрать', command=self.selectRecord)

        records = getAll(tableSelected)
        record = records[0]
        treeview = ttk.Treeview(self, show="headings", columns=(record.keys()))
        value = 0
        for key in record.keys():
            treeview.heading(column=value, text=key)
            value += 1
        for row in records:
            if (tableSelected == tables[0]):
                treeview.insert("", "end", values=(row["id"], row["login"], row["password"]))
            elif (tableSelected == tables[1]):
                treeview.insert("", "end", values=(row["id"], row["excursionId"], row["userId"], row["price"]))

        self.lbl_table.grid(row=3,column=0,columnspan=2,pady=10)
        entry_id.grid(row=4,column=0,pady=10,padx=10)
        btn_select.grid(row=4,column=1,pady=10,padx=10)
        treeview.grid(row=5,column=0,columnspan=10,pady=10,padx=10)

    def selectRecord(self):
        id = self.id.get()
        record = get(id)
        if record:
            print(record)
        else:
            print("Такой записи нету")

if __name__ == '__main__':
    root = MainWindow()
    root.title("База Музея")
    root.geometry('800x600')
    root.mainloop()