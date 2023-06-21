# Main - password handler
import sys
from tkinter import *
import os.path
class Data:
    def __init__(self, Login, Password, Email = None):
        self.info = {'Login' : Login,
                'Password' : Password,
                'Email' : Email
        }
class App:
    def __init__(self):
        window = Tk()
        window.resizable(False,False)
        w = 600
        h = 600
        window.geometry(f'{w}x{h}')
        window.title('PasswordManager')
        def exit():
            sys.exit()
        but = Button(window,text='Destroy', command=exit)
        but.pack(side='bottom')
        # try:
        #     file = open('masterpass.txt','r')
        #     master_pass = file.read()
        #     file.close
        # except FileNotFoundError:
        #     new_file = open('masterpass.txt','w+')
        #     new_file.write('')
        #     new_file.close 
        #     master_pass = ''
        def logo():
            welcome = Label(window,text= 'P', font= ('Roboto Mono Bold ',50), fg='black', width = 1)
            welcome_2 = Label(window,text= 'M', font= ('Roboto Mono Bold ',50), fg='black', width = 1)
            welcome.place(x=w/2-50,y=0)
            welcome_2.place(x=w/2-6,y=0)
        logo()
        def clear():
            all_widgets = window.slaves()
            for widget in all_widgets:
                widget.destroy()
        
        def login():
            clear()
            logo()
            def ismasterpass(event):
                try:
                    file = open(f'data\{log.get()}.txt','r')
                    master_pass = file.read()
                    file.close()
                except FileNotFoundError:
                    above_text.config(text='Неправильный логин или пароль')
                if text.get() == master_pass:
                    print('y')
                else:
                    above_text.config(text='Неправильный логин или пароль')
                    frame.focus_set()
            def travel_to_reg():
                register()
            def on_focus_in_text(event):
                if text.get() == '' or text.get() == 'Пароль':
                    text.config(fg='black')
                    text.delete(0,END)
            def on_focus_in_log(event):
                if log.get() == '' or log.get() == 'Логин':
                    log.config(fg='black')
                    log.delete(0,END)
            def on_focus_out_text(event):
                if text.get() == '' or text.get() == 'Пароль':
                    text.config(fg='#939599')
                    text.delete(0,END)
                    text.insert(0,'Пароль')
            def on_focus_out_log(event):
                if log.get() == '' or log.get() == 'Логин':
                    log.config(fg='#939599')
                    log.delete(0,END)
                    log.insert(0,'Логин')
            frame = Frame(window,width=300,height=100,borderwidth=2,) #bg=blue
            frame.pack(expand=True)
            
            above_text = Label(frame,text='Авторизация', width = 100, height = 1, font= ('Roboto',14), fg = 'black')
            above_text.pack()              
            
            log = Entry(frame,width=20,font= 'Roboto',fg = '#939599',borderwidth=2,)
            log.pack()
            log.bind('<FocusOut>',on_focus_out_log)
            log.bind('<FocusIn>',on_focus_in_log)
            log.bind('<Return>',ismasterpass)
            log.insert(0,'Логин')

            text = Entry(frame,width=20,font= 'Roboto',fg = '#939599',borderwidth=2,)
            text.pack()
            text.insert(0,'Пароль')
            text.bind('<FocusOut>',on_focus_out_text)
            text.bind('<FocusIn>',on_focus_in_text)
            text.bind('<Return>',ismasterpass)

            register_button = Button(frame,text='Нет аккаунта?',font= ('Roboto',10),fg = 'red',width=15,height = 1,border=0,command= lambda: travel_to_reg())
            register_button.pack(pady=15)

            frameb = Frame(window,width = 300, height= 1,borderwidth=2,) #bg='red'
            frameb.pack(side='bottom',fill=BOTH)
            # but = Button(frameb,text='Destroy', command=exit)
            # but.pack(side='bottom')
            # loginbutton = Button(frameb, text="Войти",height=1)
            # loginbutton.pack(side=RIGHT, padx=5, pady=5)
            closeButton = Button(frameb, text="Закрыть",height=1, command= exit)
            closeButton.pack(side=RIGHT, padx=5, pady=5)
            
        def register():
            clear()
            logo()
            def regmasterpass(event):
                if text.get() == '' or log.get() == '' or text.get() == 'Пароль' or log.get() == 'Логин':
                    pass
                elif os.path.isfile(f'data\{log.get()}.txt') == True:
                    above_text.config(text='Указанный логин уже занят')
                else:
                    def regmasterpass_again(event):
                        if first_pass == text.get():
                            master_pass = text.get()
                            print(master_pass)
                            file = open(f'data\{log.get()}.txt','w')
                            file.write(master_pass)
                            file.close
                            above_text.config(text='Регистрация завершена')
                            text.bind('<Return>',regmasterpass)
                            log.bind('<Return>',regmasterpass)
                            text.bind('<FocusOut>',on_focus_out_text)
                            frame.focus_set()
                        else:
                            text.bind('<Return>',regmasterpass)
                            text.bind('<FocusOut>',on_focus_out_text)
                            above_text.config(text='Пароли не совпадают, попробуйте ещё раз')
                            frame.focus_set()
                    def on_focus_out_text2(event):
                        if text.get() == '' or text.get() == 'Подтвердите':
                            text.config(fg='#939599')
                            text.delete(0,END)
                            text.insert(0,'Подтвердите')
                    text.bind('<Return>',regmasterpass_again)
                    log.bind('<Return>',regmasterpass_again)
                    text.bind('<FocusOut>',on_focus_out_text2)
                    first_pass = text.get() 
                    text.delete(0,END)
                    frame.focus_set()
                    text.insert(0,'Подтвердите')
            def travel_to_log():
                login()
            def on_focus_in_text(event):
                if text.get() == '' or text.get() == 'Пароль' or text.get() == 'Подтвердите':
                    text.config(fg='black')
                    text.delete(0,END)
            def on_focus_in_log(event):
                if log.get() == '' or log.get() == 'Логин':
                    log.config(fg='black')
                    log.delete(0,END)
            def on_focus_out_text(event):
                if text.get() == '' or text.get() == 'Пароль':
                    text.config(fg='#939599')
                    text.delete(0,END)
                    text.insert(0,'Пароль')
            def on_focus_out_log(event):
                if log.get() == '' or log.get() == 'Логин':
                    log.config(fg='#939599')
                    log.delete(0,END)
                    log.insert(0,'Логин')
            
            frame = Frame(window,width=300,height=100,borderwidth=2,) #bg='blue
            frame.pack(expand=True)

            above_text = Label(frame,text='Регистрация', width = 100, height = 1, font= ('Roboto',14), fg = 'black')
            above_text.pack()

            log = Entry(frame,width=20,font= 'Roboto',fg = '#939599',borderwidth=2,)
            log.pack()
            log.insert(0,'Логин')
            log.bind('<FocusOut>',on_focus_out_log)
            log.bind('<FocusIn>',on_focus_in_log)
            log.bind('<Return>',regmasterpass)

            text = Entry(frame,width=20,font= 'Roboto',fg = '#939599',borderwidth=2,)
            text.pack()
            text.insert(0,'Пароль')
            text.bind('<FocusOut>',on_focus_out_text)
            text.bind('<FocusIn>',on_focus_in_text)
            text.bind('<Return>',regmasterpass)

            register_button = Button(frame,text='Уже есть аккаунт?',font= ('Roboto',10),fg = 'red',width=20,height = 1,border=0,command= lambda: travel_to_log())
            register_button.pack(pady=15)

            frameb = Frame(window,width = 300, height= 1,borderwidth=2,) #bg='red'
            frameb.pack(side='bottom',fill=BOTH)

            # but = Button(frameb,text='Destroy', command=exit)
            # but.pack(side='bottom')

            # loginbutton = Button(frameb, text="Войти",height=1)
            # loginbutton.pack(side=RIGHT, padx=5, pady=5)
            closeButton = Button(frameb, text="Закрыть",height=1,command= exit)
            closeButton.pack(side=RIGHT, padx=5, pady=5)
        
        
        login()      
        window.mainloop()
app = App()
