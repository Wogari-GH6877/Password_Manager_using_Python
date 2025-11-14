from tkinter import *
from tkinter import messagebox
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


password_list = []



password_letter=[random.choice(letters) for _ in range(random.randint(8, 10))]
password_symbols=[random.choice(symbols) for _ in range(random.randint(2, 4))]
password_numbers=[random.choice(numbers) for _ in range(random.randint(2, 4))]




password_list=password_letter + password_symbols + password_numbers

random.shuffle(password_list)

mypassword ="".join(password_list)



def save():
    website = input1.get()
    email = input2.get()
    password = input3.get()

    is_empty=(len(website)==0 or len(email)==0 or len(password)==0)

    if(is_empty):
        messagebox.showinfo(title="Oops",message="there is empty field fill it ")
    else:


        is_right=messagebox.askokcancel(title=website,message=f"this are the details \n Website: {website}\n Email: {email} \n Password: {password}")

        if is_right:
            with open("file.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                input1.delete(0,END)
                input3.delete(0, END)

def generate():
    input3.insert(0,mypassword)

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

generate_button=Button(text="Generate Password",command=generate)
generate_button.grid(column=2,row=3)

add_button=Button(text="Add",width=35,command=save)
add_button.grid(row=4,column=0,columnspan=2)

window.mainloop()