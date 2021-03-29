from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.geometry ("300x300")
root.title ('Enter to the system')

def registration():
    text = Label(text = 'Для входа зарегистрируйтесь!')
    text_log = Label (text = "Введите логин")
    register_login = Entry()
    text_password = Label (text = "Введите пароль")
    register_password = Entry()
    text_password2 = Label(text="Еще раз введите пароль")
    register_password2 = Entry(show = "*")
    button_register = Button(text = "Зарегистрироваться", command = lambda : save_pass())
    text.pack()
    text_log.pack()
    register_login.pack()
    text_password.pack()
    register_password.pack()
    text_password2.pack()
    register_password2.pack()
    button_register.pack()
    while False:
        if text_password2 != text_password:
            print("Ошибка!")


    def save_pass():
        login_pass_save = {}
        login_pass_save[register_login.get()] = register_password.get()
        f = open('login.txt', "wb")
        pickle.dump(login_pass_save, f)
        f.close()
        login()

def login():
    text_log = Label(text = "Congrats! You are registered!")
    text_enter_login = Label (text = "Your login")
    enter_login = Entry()
    text_enter_pass = Label(text = 'Your password')
    enter_password = Entry(show = '*')
    button_enter = Button(text = "Enter", command = lambda: log_pass())
    text_log.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_pass.pack()
    enter_password.pack()
    button_enter.pack()

    def log_pass():
        f = open('login.txt', 'rb')
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_password.get() == a[enter_login.get()]:
                messagebox.showinfo("Вход выполнен", "Привет. У тебя несколько сообщений!")
            else:
                messagebox.showerror("Ошибка", "Вы ввели неверный логин или пароль")









# login()

registration()

root.mainloop()
