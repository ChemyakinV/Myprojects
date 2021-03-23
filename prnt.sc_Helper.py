import requests 
import re
import tkinter as tk 
from PIL import Image, ImageTk
from io import BytesIO
import os
import shutil
from fake_useragent import UserAgent
import datetime
from tkinter import messagebox

headers = {'User-Agent': str(UserAgent().random)}

session = str(datetime.datetime.today())
session = session.replace(':', '-')

nomera = []
g1 = []
g2 = []
g3 = []
g4 = []
g5 = []
g6 = []
variants = []
com = list('0123456789abcdefghijklmnopqrstuvwxyz')


class wk():
    '''Рабочий класс для работы программмы'''
    def __init__(self):
        try:
            os.mkdir("saved_prnt.sc_Helper", 0o777)
        except FileExistsError:
            print('Директория существует')
        os.mkdir('saved_prnt.sc_Helper\\' + 'session ' + session)
        self.first()
        
    def first(self):
        self.root = tk.Tk()
        self.root.title('prnt.sc_HELPER')
        #self.root.resizable(width=False, height=False)
        self.label1 = tk.Label(text = "Input first url:")
        self.label2 = tk.Label(text = "Input last url:")
        self.uurl1 = tk.StringVar()
        self.uurl2 = tk.StringVar()
        self.url1 = tk.Entry(self.root, width = 50, textvariable = self.uurl1)
        self.url2 = tk.Entry(self.root, width = 50, textvariable = self.uurl2)
        print(self.uurl1.get(), self.uurl2.get())
        self.searchbtn = tk.Button(text = "Search", command = lambda: self.combinationgenerator(self.uurl1.get(), self.uurl2.get()), bg = "silver")
        self.label1.grid(row = 0, column = 0, sticky = tk.W, pady = 10, padx = 10)
        self.url1.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.label2.grid(row = 1, column = 0, sticky = tk.W, pady = 10, padx = 10)
        self.url2.grid(row = 1, column = 1, pady = 10, padx = 10)
        self.searchbtn.grid(row = 2, column = 1, sticky = tk.E, padx = 10, pady = 10)

    def combinationgenerator(self, uurl1, uurl2):
        self.url1list = list(uurl1)
        self.url2list = list(uurl2)
        
        #================================================================================
        if self.url1list[16] == self.url2list[16]:
            g1.append(self.url1list[16])
            #============================================================================
            if self.url1list[17] == self.url2list[17]:
                g2.append(self.url1list[17])
                #========================================================================
                if self.url1list[18] == self.url2list[18]:
                    g3.append(self.url1list[18])
                    #====================================================================
                    if self.url1list[19] == self.url2list[19]:
                        g4.append(self.url1list[19])
                        #================================================================
                        if self.url1list[20] == self.url2list[20]:
                            g5.append(self.url1list[20])
                            #============================================================
                            if self.url1list[21] == self.url2list[21]:
                                g6.append(self.url1list[21])
                            else: 
                                f1 = com.index(self.url1list[21])
                                f2 = com.index(self.url2list[21])
                                if com[f1] > com[f2]:
                                    for x in com[f2:f1+1]:
                                        g6.append(x)
                                else:
                                    for x in com[f1:f2+1]:
                                        g6.append(x)
                            #============================================================
                        else:
                            e1 = com.index(self.url1list[20])
                            e2 = com.index(self.url2list[20])
                            if com[e1] > com[e2]:
                                for x in com[e2:e1+1]:
                                    g5.append(x)
                            else:
                                for x in com[e1:e2+1]:
                                    g5.append(x)
                            for l in com:
                                g6.append(l)
                        #================================================================
                    else:
                        d1 = com.index(self.url1list[19])
                        d2 = com.index(self.url2list[19])
                        if com[d1] > com[d2]:
                            for x in com[d2:d1+1]:
                                g4.append(x)
                        else:
                            for x in com[d1:d2+1]:
                                g4.append(x)
                        for l in com:
                            g5.append(l)
                            g6.append(l)
                    #====================================================================
                else:
                    c1 = com.index(self.url1list[18])
                    c2 = com.index(self.url2list[18])
                    if com[c1] > com[c2]:
                        for x in com[c2:c1+1]:
                            g3.append(x)
                    else:
                        for x in com[c1:c2+1]:
                            g3.append(x)
                    for l in com:
                        g4.append(l)
                        g5.append(l)
                        g6.append(l)
                #========================================================================
            else:
                b1 = com.index(self.url1list[17])
                b2 = com.index(self.url2list[17])
                if com[b1] > com[b2]:
                    for x in com[b2:b1+1]:
                        g2.append(x)
                else:
                    for x in com[b1:b2+1]:
                        g2.append(x)
                for l in com:
                    g3.append(l)
                    g4.append(l)
                    g5.append(l)
                    g6.append(l)
            #============================================================================
        else:
            a1 = com.index(self.url1list[16])
            a2 = com.index(self.url2list[16])
            if com[a1] > com[a2]:
                for x in com[a2:a1+1]:
                    g1.append(x)
            else:
                for x in com[a1:a2+1]:
                    g1.append(x)
            for l in com:
                g2.append(l)
                g3.append(l)
                g4.append(l)
                g5.append(l)
                g6.append(l)

        
        #================================================================================

        for q in g1:
            for w in g2:
                for e in g3:
                    for r in g4:
                        for t in g5:
                            for y in g6:
                                variants.append(str(q+w+e+r+t+y))

        self.label1.destroy()
        self.url1.destroy()
        self.label2.destroy()
        self.url2.destroy()
        self.searchbtn.destroy()

        for x in variants:
            nomera.append('https://prnt.sc/' + x)
        self.imgget(0)
        
    def nextimg(self, indx):
        '''Кнопка для перехода к следующему изображению'''
        try:
            indx = indx+1
            self.imgget(indx)
        except IndexError:
            self.imgget(indx)

    def previmg(self, indx):
        '''Кнопка для перехода к предыдущему изображению'''
        try:
            indx = indx-1
            self.imgget(indx)
        except IndexError:
            self.imgget(indx)

    def buildwindow(self, imgcontent, indx):
        '''Функция для отображения результата работы программы'''
        self.canvas = tk.Canvas(self.root, width=1200,height=600, bg = 'grey')
        self.canvas.grid(row = 0, column = 0, columnspan = 3, )
        self.img1 = Image.open(BytesIO(imgcontent))
        self.img1.thumbnail((700,600), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img1)
        self.canvas.create_image(600, 300, image=self.img)
        self.btns(indx)
        self.save = tk.Button(text = "save", command = lambda: self.downloadimg(imgcontent, indx), bg = "green", fg = "white", width = 10)
        self.save.grid(row = 1, column = 1, sticky = tk.W, padx = 10, pady = 10)
        self.savall = tk.Button(text = "SAVE_ALL", command = lambda: self.saveall(), bg = "green", fg = "white", width = 10)
        self.savall.grid(row = 2, column = 2, sticky = tk.E, padx = 10, pady = 10)

    def btns(self, indx):
        '''Корректное отображение кнопок'''
        try:
            self.btnnext.destroy()
            self.btnprev.destroy()
        except AttributeError:
            self.btnnext = tk.Button(text = ">", command = lambda: self.nextimg(indx), bg = "silver")
            self.btnprev = tk.Button(text = "<", command = lambda: self.previmg(indx), bg = "silver")
            self.lbl = tk.Label(text = nomera[indx], fg = "grey")
            self.btnnext.grid(row = 1, column = 2, sticky = tk.E, padx = 10, pady = 10)
            self.btnprev.grid(row = 1, column = 0, sticky = tk.W, padx = 10, pady = 10)
            self.lbl.grid(row = 2, column = 0, sticky = tk.W, padx = 10, pady = 10)
            try:
                o = nomera[indx + 1]
            except IndexError:
                self.btnnext.destroy()
            try:
                o = nomera[indx - len(nomera) - 1]
            except IndexError:
                self.btnprev.destroy()
        else:
            self.btnnext = tk.Button(text = ">", command = lambda: self.nextimg(indx), bg = "silver")
            self.btnprev = tk.Button(text = "<", command = lambda: self.previmg(indx), bg = "silver")
            self.lbl = tk.Label(text = nomera[indx], fg = "grey")
            self.btnnext.grid(row = 1, column = 2, sticky = tk.E, padx = 10, pady = 10)
            self.btnprev.grid(row = 1, column = 0, sticky = tk.W, padx = 10, pady = 10)
            self.lbl.grid(row = 2, column = 0, sticky = tk.W, padx = 10 ,pady = 10)
            try:
                o = nomera[indx + 1]
            except IndexError:
                self.btnnext.destroy()
            try:
                o = nomera[indx - 1]
            except IndexError:
                self.btnprev.destroy()

    def imgget(self, indx):
        '''Захват кода картинки'''
        r = requests.get(nomera[indx], headers = headers)                          
        text = r.text                                                           
        p = re.compile(r'image/.{22}.png')                                       
        patternimg = re.search(p, text)                                          
        if patternimg != None:                                                   
            u = 'https://image.prntscr.com/'+str(patternimg)[44:76]                     
            v = requests.get(u, headers = headers)                              
            if v.status_code == 200:                                            
                imgcontent = v.content
                self.buildwindow(imgcontent, indx)
        if patternimg == None:
            indx = indx + 1
            self.imgget(indx)

    def downloadimg(self, content, indx):
        '''Сохранение картинки'''      
        path = 'saved_prnt.sc_Helper\\' + 'session ' + session +'\\' 

        with open(path + variants[indx] + '.png', 'wb') as f:     
                f.write(content)

    def saveall(self):
        print(nomera)
        for x in nomera:
            r = requests.get(x, headers = headers)                          
            text = r.text                                                           
            p = re.compile(r'image/.{22}.png')                                       
            patternimg = re.search(p, text)                                          
            if patternimg != None:                                                   
                u = 'https://image.prntscr.com/'+str(patternimg)[44:76]                     
                v = requests.get(u, headers = headers) 
                imgcontent = v.content
                self.alldownload(imgcontent, x[16:22])
        print('finished')   

    def alldownload(self, imgcontent, x):
        path = 'saved_prnt.sc_Helper\\' + 'session ' + session +'\\' 
        with open(path + x + '.png', 'wb') as f:     
            f.write(imgcontent)

    def mainLoop(self):
        self.root.mainloop()

wu = wk()

wu.mainLoop()