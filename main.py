from tkinter import *


def save():
    website = input1.get()
    email = input2.get()
    password = input3.get()
    with open("file.txt","a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        input1.delete(0,END)
        input3.delete(0, END)

window=Tk()
# window.minsize(height=400,width=600)
window.title("Password Manager")
window.config(pady=20,padx=20)

canvas=Canvas(width=300,height=200,bg="white")
image=PhotoImage(file="img.png")

canvas.create_image(150,100,image=image)
canvas.grid( row=0,column=1)

input1=Entry(width=35)
input1.grid(row=1,column=0,columnspan=2)
input1.focus()

website=Label(text="Website:")
website.grid(row=1,column=0)




email=Label(text="Email/address : ")
email.grid(row=2,column=0)
input2=Entry(width=35)
input2.insert(0,"www.com")
input2.grid(row=2,column=0,columnspan=2)

password=Label(text="Password:")
password.grid(row=3,column=0)

input3=Entry(width=35)
input3.grid(row=3,column=1)


#Buttons

generate_button=Button(text="Generate Password")
generate_button.grid(column=2,row=3)

add_button=Button(text="Add",width=35,command=save)
add_button.grid(row=4,column=0,columnspan=2)

window.mainloop()