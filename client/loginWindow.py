import tkinter as tk
import tkinter.messagebox
from client.api.resolvers import login

class LoginWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.user_login = tk.StringVar()
        self.user_password = tk.StringVar()

        self.font = ('Arial Bold', 30)
        self.resizable(width=False, height=False)

        lbl_main = tk.Label(self, text="Вход в систему", font=self.font)
        lbl_login = tk.Label(self, text="Логин", font=self.font)
        lbl_pass = tk.Label(self, text='Пароль', font=self.font)
        entry_login = tk.Entry(self, font=self.font,
                               textvariable=self.user_login)
        entry_pass = tk.Entry(self, font=self.font,
                              textvariable=self.user_password)
        btn_enter = tk.Button(self, text='Вход', font=self.font,
                              command=self.login)
        btn_close = tk.Button(self, text='Отмена', font=self.font,
                              command=self.destroy)

        lbl_main.grid(row=0, columnspan=2, column=1)
        lbl_login.grid(row=1, column=0, pady=10, ipadx=10)
        entry_login.grid(row=1, column=1, columnspan=3, padx=30, pady=10)
        lbl_pass.grid(row=2, column=0, pady=10, ipadx=10)
        entry_pass.grid(row=2, column=1, columnspan=3, padx=30, pady=10)
        btn_enter.grid(row=3, column=1, pady=10)
        btn_close.grid(row=3, column=2, pady=10)

    def login(self):
        post = login(user_login=self.user_login.get(),
                     user_password=self.user_password.get())
        if post:
            tk.messagebox.showinfo(title="Login correct", message="Авторизация успешна")
            self.parent.loginComplete()
            self.destroy()
        else:
            tk.messagebox.showerror(title="Wrong login", message="Логин или пароль не верны")


