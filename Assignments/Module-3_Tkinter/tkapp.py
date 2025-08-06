import tkinter
from tkinter import ttk

window=tkinter.Tk()
window.title("MyApp")
window.geometry("500x600")
window.config(bg="lightblue")

"""tkinter.Label(text="Firstname:").pack()
tkinter.Label(text="Lastname:").pack()"""


"""tkinter.Label(text="Firstname:",bg='lightblue', fg='purple', font='Fixedsys 18 bold').place(x=0,y=0)
tkinter.Label(text="Lastname:",bg='lightblue', fg='purple', font='Fixedsys 18 bold').place(x=0,y=30)"""

"""tkinter.Label(text="Firstname:",bg='lightblue', fg='purple', font='Fixedsys 18 bold').place(x=0,y=0)
tkinter.Label(text="Lastname:",bg='lightblue', fg='purple', font='Fixedsys 18 bold').place(x=0,y=30)"""

tkinter.Label(text="Firstname:",bg='lightblue', fg='purple', font='Constantia 18 bold').grid(row=0,column=0,sticky='w')
tkinter.Label(text="Lastname:",bg='lightblue', fg='purple', font='Constantia 18 bold').grid(row=1,column=0,sticky='w')

fnm=tkinter.Entry(font='Constantia 12 bold')
fnm.grid(row=0,column=1,sticky='w')
lnm=tkinter.Entry(font='Constantia 12 bold')
lnm.grid(row=1,column=1,sticky='w')

tkinter.Radiobutton(value=0,text="Male",bg='lightblue', fg='purple', font='Constantia 18 bold').grid(row=2,column=0,sticky='w')
tkinter.Radiobutton(value=1,text="Female",bg='lightblue', fg='purple', font='Constantia 18 bold').grid(row=2,column=1,sticky='w')
tkinter.Radiobutton(value=2,text="Other",bg='lightblue', fg='purple', font='Constantia 18 bold').grid(row=2,column=2,sticky='w')

tkinter.Checkbutton(text="Gujarati",bg='lightblue', fg='purple', font='Constantia 18 bold').grid(row=3,column=0,sticky='w')
tkinter.Checkbutton(text="Hindi",bg='lightblue', fg='purple', font='Constantia 18 bold').grid(row=4,column=0,sticky='w')
tkinter.Checkbutton(text="English",bg='lightblue', fg='purple', font='Constantia 18 bold').grid(row=5,column=0,sticky='w')

city=["Rajkot","Ahmedabad","Surat","Baroda","Jamnagar"]

ttk.Combobox(values=city).grid(row=6,column=0)

def btnClick():
    #print("Button Clicked!")
    print("Firstname:",fnm.get())
    print("Lastname:",lnm.get())

tkinter.Button(text="Submit",font='Constantia 18 bold',command=btnClick).place(x=190,y=290)

window.mainloop()


