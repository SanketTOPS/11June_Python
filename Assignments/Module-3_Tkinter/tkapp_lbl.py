import tkinter

tk=tkinter.Tk()
tk.title("MyApp")
tk.geometry("500x600")
tk.config(background="lightblue")

l1=tkinter.Label(text="Enter any:")
l1.grid(row=0,column=0)

v1=tkinter.Entry()
v1.grid(row=0,column=1)

resultLbl=tkinter.Label(text="Result:")
resultLbl.place(x=100,y=200)


def btn():
    rs=v1.get()
    resultLbl.config(text=f"My Name is {rs}")
bt=tkinter.Button(text="Submit",command=btn)
bt.grid(row=1,column=0)
tk.mainloop()