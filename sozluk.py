from tkinter import *
import requests
from bs4 import *
import json as js

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}


window = Tk()
window.title('SÖZLÜK')
Label(text="Kelime:").grid(row=1,column=1)

kelimeentryvar = StringVar()
kelimeentry = Entry(window,width=35,textvariable=kelimeentryvar)
kelimeentry.grid(row=1,column=2,pady=10,padx=0,sticky=W)

def ogren():
    kelime = kelimeentryvar.get()
    if kelime.strip() == "":
        return
    url  =f"https://sozluk.gov.tr/gts?ara={kelime}"
    cevap = requests.get(url,headers=header)
    content = cevap.content
    json = BeautifulSoup(content,"html.parser")
    json = str(json)
    while json[-1] != '}':
        json = json[:-1]
    while json[0] != '{':
        json = json[1:]
    object = js.loads(json)
    anlamlar = []
    for anlam in object["anlamlarListe"]:
        anlamlar.append(anlam["anlam"])
    anlamlarvar.set(anlamlar)
    
buton = Button(text="ÖĞREN",width=10,command=ogren)
buton.grid(row=1,column=3,pady=10,sticky=E)

x_scroll = Scrollbar(orient=HORIZONTAL)
y_scroll = Scrollbar()
anlamlarvar = StringVar()
Listboxanlamlar = Listbox(height=15,width=60,listvariable=anlamlarvar,xscrollcommand=x_scroll.set,yscrollcommand=y_scroll.set)
Listboxanlamlar.grid(row=2,column=1,columnspan=3,padx=(10,0))

x_scroll["command"] = Listboxanlamlar.xview
y_scroll["command"] = Listboxanlamlar.yview

y_scroll.grid(row=2,column=4,sticky=NS,padx=(0,10))
x_scroll.grid(row=3,column=1,sticky=EW,padx=(10,0),columnspan=3,pady=(0,10))

window.mainloop()