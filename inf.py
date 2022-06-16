from tkinter import *
import os

class inf(Toplevel):
    def init(self, root):
        super().init(root)
        self.root = root
        self.title("О нас")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.geometry('400x225')
        self.resizable(False, False)

        self.image_about = PhotoImage(file="./aaa.png")

        self.lbl_about = Label(self, image=self.image_about)
        self.lbl_about.pack(fill = BOTH, expand=True)



        #opts = { 'ipadx': 10, 'ipady': 10, 'fill': BOTH }

        self.lbl_text = Label(self.lbl_about, text='ФИО: Быстрова Елизавета Шамилевна', justify = LEFT)
        #self.lbl_text.pack(side=TOP, opts)
        self.lbl_text.place(relx=.5, rely=.4, anchor="c")

        self.lbl_text_2 = Label(self.lbl_about, text='Группа: 208',  justify = LEFT)
        #self.lbl_text_2.pack(side=TOP, opts)
        self.lbl_text_2.place(relx=.5, rely=.5, anchor="c")

        self.lbl_text_3 = Label(self.lbl_about, text='e-mail: Lizabb@bk.ru',  justify = LEFT)
        #self.lbl_text_3.pack(side=TOP, **opts)
        self.lbl_text_3.place(relx=.5, rely=.6, anchor="c")
