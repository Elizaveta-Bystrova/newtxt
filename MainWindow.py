from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import Menu
import os
from RegexToplevel import RegexToplevel
from util import *
from inf import inf

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Простой текстовый редактор")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

      

        self.txt_edit = Text(self, undo=True)
        self.txt_edit.grid(row=0,column=1,sticky="nsew")

        mainmenu = Menu(self)
        self.config(menu=mainmenu)
        filemenu = Menu(mainmenu, tearoff=0)
        mainmenu.add_cascade(label="Файл",menu=filemenu)
        filemenu.add_command(label="Открыть", command=self._click_open_file)
        filemenu.add_command(label="Сохранить как", command=self._click_save_file)
        

        mmainmenu = Menu(self)
        self.config(menu=mainmenu)
        filemenu = Menu(mmainmenu, tearoff=0)
        mainmenu.add_cascade(label="Правка",menu=filemenu)
        filemenu.add_command(label="Анализатор", command=self._click_open_re_tl)
        
        newmainmenu = Menu(self)
        self.config(menu=mainmenu)
        filemenu = Menu(newmainmenu, tearoff=0)
        mainmenu.add_cascade(label="О нас",menu=filemenu)
        filemenu.add_command(label="Информация", command=self._click_open_inf)

        self.mainloop()
    
 
    def _click_open_file(self):
        filepath = askopenfilename(
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")] 
        )
        if not filepath:
            return
    
        text = open_file(filepath)
    
        self.txt_edit.delete("1.0",END)
        self.txt_edit.insert(END,text)
        self.title(f"Простой текстовый редактор - {filepath}")

    def _click_save_file(self):
        filepath = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")], 
        )
        if not filepath:
            return
    
           
        text = self.txt_edit.get("1.0",END)
        save_file(filepath,text)
        self.title(f"Простой текстовый редактор - {filepath}")
    
    def _click_open_re_tl(self):
        tl_reg = RegexToplevel(self)
        #tl_reg.grab_set()

    def _click_open_inf(self):
        tl_reg = inf(self)
        #tl_reg.grab_set()

   
MainWindow().__init__

