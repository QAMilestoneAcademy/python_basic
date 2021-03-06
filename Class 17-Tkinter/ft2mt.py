from tkinter import Tk, Button, Label,DoubleVar,Entry

window=Tk()
window.title('Feet to Meter Conversion')
window.configure(background="light blue"
                            "")
window.geometry("320x220")
window.resizable(width=False,height=False)

def convert():
    value=float(ft_entry.get())
    meter=value*0.3048
    mt_value.set(round(meter,4))

def clear():
    ft_value.set("")
    mt_value.set("")


#Lable A widget used to display text on the screen
ft_lbl=Label(window,text="Feet",bg="blue",fg="yellow",width=14)
ft_lbl.grid(column=0,row=0,padx=15,pady=15)

#DoubleVar type value allows float
ft_value=DoubleVar()
#Entry -A text entry widget that allows only a single line of text
ft_entry=Entry(window,textvariable=ft_value,width=14)
ft_entry.grid(column=1,row=0)
#clearing the screen before start
ft_entry.delete(0,'end')

mt_lbl=Label(window,text="Meter",bg="blue",fg="yellow",width=14)
mt_lbl.grid(column=0,row=1,padx=15,pady=15)



#DoubleVar type value allows float
mt_value=DoubleVar()
#Entry -A text entry widget that allows only a single line of text
mt_entry=Entry(window,textvariable=mt_value,width=14)
mt_entry.grid(column=1,row=1)
#clearing the screen before start
mt_entry.delete(0,'end')

convert_btn=Button(window,text="Convert",bg="black",fg="white",width=14,command=convert)
convert_btn.grid(column=0,row=3,padx=15)
clear_btn=Button(window,text="Clear",bg="Dark Grey",fg="white",width=14,command=clear)
clear_btn.grid(column=1,row=3,padx=15)

window.mainloop()