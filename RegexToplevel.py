from tkinter import * 
import re


class RegexToplevel(Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.title('Дополнительное окно')
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight=1)
        self.resizable(False, False)

        self.fr_functions = Frame(self)
        self.fr_functions.columnconfigure(0, weight=1)
        self.fr_functions.rowconfigure(6, weight=10)

        self.ent_regex = Entry(self.fr_functions)
        self.ent_regex.grid(column=0, row=0, sticky=N, padx=2, pady=2)

        self.ent_replace = Entry(self.fr_functions)
        self.ent_replace.grid(column=0, row=2, sticky=EW, padx=0, pady=0)

        self.btn_findall = Button(self.fr_functions, text='Найти', command=self._click_findall)
        self.btn_findall.grid(column=0, row=1,sticky=EW,padx=2,pady=2)

        self.btn_findadd = Button(self.fr_functions, text = 'Найти и добавить', command=self._click_find)
        self.btn_findadd.grid(column=0, row=4, sticky=EW, padx=2, pady=2 )

        self.btn_del = Button(self.fr_functions, text = 'Удалить', command=self._click_delete)
        self.btn_del.grid(column=0, row=5, sticky=EW, padx= 2, pady= 2)

        self.btn_change = Button(self.fr_functions, text='Заменить', command=self._click_search_and_change )
        self.btn_change.grid(column=0, row=3, sticky=EW, padx=2, pady=2)

        self.list_result = Listbox(self.fr_functions, height=10)
        self.list_result.grid(column=1,row=0,rowspan=6,sticky=NSEW,padx=2,pady=2)

        self.fr_functions.grid(column=0,row=0,sticky=NS)

    def _click_findall(self):
        self.list_result.delete(0,END)
        pattern = re.compile(self.ent_regex.get())
        result = pattern.findall(self.root.txt_edit.get('1.0',END))
        for i in result:
            self.list_result.insert(END, i)
    
    def _click_find(self):
        pattern = re.compile(self.ent_regex.get())
        result = pattern.findall(self.root.txt_edit.get('1.0',END))
        for i in result:
            self.list_result.insert(END, i)

    def _click_delete(self):
        self.list_result.delete(0, END)

    def _click_search_and_change(self):
        res = re.sub(self.ent_regex.get(), self.ent_replace.get(), self.root.txt_edit.get("1.0", END))
        self.root.txt_edit.delete("1.0", END)
        self.root.txt_edit.insert("1.0", res)