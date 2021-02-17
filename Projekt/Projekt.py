from tkinter import *

a=0
def klikker():
    #pass
    global a
    a+=1
    btn.config(text=a)

def klikker_(event):
    global a
    a-=1
    btn.config(text=a)

suurus=10
def klikker__(event):
    global suurus
    if event.num ==5 or event.delta==-120:
        suurus+=1
    else:
        suurus-=1
    lbl.configure(width=suurus,text=suurus)

def text_to_lbl(event):
    text=ent.get() #num=int(text),если нужны цифры
    lbl.configure(text=text)

aken=Tk()
aken.title("Tkinter_app") #заглавние
aken.geometry("600x600") #размер окна
aken.iconbitmap("kartul.ico") #иконка

btn=Button(aken,text="Vajuta siia",bg="green",fg="white",font="Arial 20",height=5,width=20,activebackground="blue",command=lambda:klikker()) #lkm po btn->klikker(), левая кнопка мыши
btn.bind("<Button-3>",klikker_) #правая кнопка мыши
btn.pack()

lbl=Label(aken,text="Nimetus",borderwidth=5,height=5,width=10,relief="groove") #raised, sunken, flat, solid
lbl.bind("<MouseWheel>",klikker__)
lbl.pack() #side=LEFT, RIGHT, BOTTOM, TOP

ent=Entry(aken,width=10,borderwidth=5,font="Arial 20")
ent.pack()
ent.bind("<Return>",text_to_lbl) #Enter

img=PhotoImage(file="kar.png").subsample(2)
lbl.img=Label(aken,image=img)
lbl.img.pack()

aken.mainloop() #окно открывается

