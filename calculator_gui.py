from Tkinter import*




#function for about menu 
def about():
    win2=Tk()
    win2.wm_title("About")
    l=Label(win2,text=" CAL-C ver 1.0 \n Developer. \n Mohd Sanad",padx=5,pady=40)
    l.pack(fill="both")
st=""
plus=0
val=0.0
sub=0
divp=0
mulp=0


win=Tk()#creating window
win.title("Calculator")#changing window title
win.option_add("*background", "white")
#Initiliazing about menu button
menubar=Menu(win,bg="brown")
menubar.add_command(label="About",command=about)
win.config(menu=menubar)
#TextField
v=StringVar()
e=Entry(win,textvariable=v)
e.grid(row=0,column=0,columnspan=3,sticky=W+E)

def but1():
    global st
    st=st+"1"
    v.set(st)
def but2():
    global st
    st=st+"2"
    v.set(st)
def but3():
    global st
    st=st+"3"
    v.set(st)
def but4():
    global st
    st=st+"4"
    v.set(st)
def but5():
    global st
    st=st+"5"
    v.set(st)
def but6():
    global st
    st=st+"6"
    v.set(st)
def but7():
    global st
    st=st+"7"
    v.set(st)
def but8():
    global st
    st=st+"8"
    v.set(st)
def but9():
    global st
    st=st+"9"
    v.set(st)
def but10():
    global st
    st=st+"0"
    v.set(st)
def bc():
    global st
    v.set("")
    st=""
def bdec1():
    global st
    st=st+"."
    v.set(st)
    
def beql1():
    
    val2=0.0
    global st
    global val
    st1=""
     
    val2=float(st)
    st=""
    if plus==1:
        
         y=val+val2
         st=st+repr(y)
         v.set(st)
    if sub==1:
         y1=val-val2
         st=st+repr(y1)
         v.set(st)
    
    if mulp==1:
         st=""
         y2=val*val2
         st=st+repr(y2)
         v.set(st)
    
    if divp==1:
        if val2==0:
            v.set("MATHS ERROR")
        if val2!=0:
            
            y3=val/val2
            st=st+repr(y3)
            v.set(st)
    st=""
    
   
    
def badd1():
    global st
    global plus
    global val
    val=float(st)    
    st=""
    plus=1
def bsub1():
    global st
    global sub
    global val
    val=float(st)    
    st=""
    sub=1
def bmul1():
    global st
    global mulp
    global val
    val=float(st)    
    st=""
    mulp=1
def bdiv1():
    global st
    global divp
    global val
    val=float(st)    
    st=""
    divp=1



    
    


#Initializing buttons
b1=Button(win,text="1",bg="red")
b2=Button(win,text="2",bg="red")
b3=Button(win,text="3",bg="red")
b4=Button(win,text="4",bg="red")
b5=Button(win,text="5",bg="red")
b6=Button(win,text="6",bg="red")
b7=Button(win,text="7",bg="red")
b8=Button(win,text="8",bg="red")
b9=Button(win,text="9",bg="red")
b10=Button(win,text="0",bg="red")
bdec=Button(win,text=".",bg="orange")
badd=Button(win,text="+",bg="yellow")
bsub=Button(win,text="-",bg="yellow")
bmul=Button(win,text="x",bg="yellow")
bdiv=Button(win,text="/",bg="yellow")
bclear=Button(win,text="CS",bg="blue")
beql=Button(win,text="=",bg="orange")
#Positioning Buttons

b1.grid(row=1,column=0,sticky=W+E)
b2.grid(row=1,column=1,sticky=W+E)
b3.grid(row=1,column=2,sticky=W+E)
b4.grid(row=2,column=0,sticky=W+E)
b5.grid(row=2,column=1,sticky=W+E)
b6.grid(row=2,column=2,sticky=W+E)
b7.grid(row=3,column=0,sticky=W+E)
b8.grid(row=3,column=1,sticky=W+E)
b9.grid(row=3,column=2,sticky=W+E)
b10.grid(row=4,column=0,sticky=W+E)
bdec.grid(row=4,column=1,sticky=W+E)
badd.grid(row=1,column=3,sticky=W+E)
bsub.grid(row=2,column=3,sticky=W+E)
bmul.grid(row=3,column=3,sticky=W+E)
bdiv.grid(row=4,column=3,sticky=W+E)
bclear.grid(row=0,column=3,sticky=W+E)
beql.grid(row=4,column=2,sticky=W+E)
#configuring button behaviour
b1.config(command=but1)
b2.config(command=but2)
b3.config(command=but3)
b4.config(command=but4)
b5.config(command=but5)
b6.config(command=but6)
b7.config(command=but7)
b8.config(command=but8)
b9.config(command=but9)
b10.config(command=but10)
bclear.config(command=bc)
beql.config(command=beql1)
badd.config(command=badd1)
bdec.config(command=bdec1)
bsub.config(command=bsub1)
bmul.config(command=bmul1)
bdiv.config(command=bdiv1)





win.mainloop()
            
            

