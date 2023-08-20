from tkinter import *
from tkinter import messagebox
import random
import pyperclip




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 
            'o', 'p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E',
            'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V',
            'W','X','Y','Z']
    symbols = ['!','<','>','@','#','$','&','%','^','*','(',')','-','_','~','=',
            '+','/']


    #EASY LEVEL
    """ password = ""
    for char in range(1, length_of_numbers + 1):
        password += random.choice(numbers)
        
    for char in range(1, length_of_letters + 1):
        password += random.choice(letters)
        
    for char in range(1, length_of_symbols + 1):
        password += random.choice(symbols)
        
    print(password) """

    #HARD LEVEL

    length_of_numbers = random.randint(8,10)
    length_of_letters = random.randint(2,4)
    length_of_symbols = random.randint(2,4)

    password_numbers = [random.choice(numbers) for _ in range(length_of_numbers)]
    #print(password_numbers)
    
    password_letters = [random.choice(letters) for _ in range(length_of_letters)]
    #print(password_letters)
      
    password_symbols = [random.choice(symbols) for _ in range(length_of_symbols)]
    #print(password_symbols)
  
    password_list = password_numbers + password_letters + password_symbols
    #print(password_list)
    random.shuffle(password_list)
    #print(password_list)
    
    #an alternative way using the join method
    #password = "".join(password_list)
    password = ""
    for char in password_list:
        password += char 
    password_entry.insert(0,password)
    pyperclip.copy(password)
    
    #print("Your password is: " + password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    with open("data.txt", "a") as f:
        website = website_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        if website == "" or email == "" or password == "":
            messagebox.showerror("Error","All fields are required")
        else:
            f.write(f"\n{website}|{email}|{password}")
            yes_save = messagebox.askokcancel(f"{website}",f"These are the details entered\nEmail:{email}\nPassword:{password}")
            if yes_save:
                messagebox.showinfo("Success", "Saved Successfully")
                website_entry.delete(0,END)
                #email_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.geometry("600x400")

canva = Canvas(window,width=200,height=200)
logo_img = PhotoImage(file="logo.png")
canva.create_image(100, 102, image = logo_img)
canva.grid(row=0,column=1)

website_label = Label(text="Website:",font=('ariel',15,'bold'))
website_label.grid(row=1,column=0)
website_entry = Entry(window,width=50)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:",font=('ariel',15,'bold'))
email_label.grid(row=2,column=0)
email_entry = Entry(window,width=50)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(END,"wungbrandon27@gmail.com")

password_label = Label(text="Password:",font=('ariel',15,'bold'))
password_label.grid(row=3,column=0)
password_entry = Entry(window,width=35)
password_entry.grid(row=3,column=1)

generate_btn = Button(window,text="Generate Password",command=generate_password)
generate_btn.grid(row=3,column=2,padx=10)

add_btn = Button(window,text="Add",width=40,command=save_password)
add_btn.grid(row=4,column=1,columnspan=2,pady=10)





window.mainloop()
