from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("BMI Calculator")
window.config(padx=50, pady=50)

# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file="D:/VS_Code Programs/Python/BMI Calculator/BMI-Calculator.png")
# canvas.create_image(width= 100, height= 100, image=logo_img)
# canvas.grid(row=0, column=1)

# Label

name_label= Label(text= "Enter Your Name...")
name_label.grid(row= 1, column= 0)
weight_label = Label(text= "Enter your Weight...")
weight_label.grid(row= 2, column= 0)
height_label = Label(text= "Enter your age...")
height_label.grid(row= 3, column= 0)

# Entry

Name_entry = Entry()
Name_entry.grid(row= 1, column=1)
weight_entry= Entry()
weight_entry.grid(row= 2, column= 1)
height_entry= Entry()
height_entry.grid(row= 3, column= 1)

# Logic function

def Calculate_BMI():
    user_name = Name_entry.get()
    user_weight = float(weight_entry.get())
    user_height = float(height_entry.get())

    BMI= round(user_weight/(user_height * user_height), 1)

    if BMI <= 18.5:
        messagebox.showinfo(title="Underweight", message=f"Hello {user_name}, \n Your Body Mass Index is {BMI}, \n You must focus on your body, Increase it by having some good and healthy meal everyday.")
    elif BMI <= 24.9:
        messagebox.showinfo(title="Healthy", message=f"Hello {user_name}, \n Your Body Mass Index is {BMI}, \n You are Healthy, Have good and healthy meals everyday.")
    elif BMI <= 29.9:
        messagebox.showinfo(title="Overweight", message=f"Hello {user_name}, \n Your Body Mass Index is {BMI}, \n You must focus on your body, Control with care")
    elif BMI > 30:
        messagebox.showinfo(title="Obese", message=f"Hello {user_name}, \n Your Body Mass Index is {BMI}, \n You must focus on your body, It needs extreme care you are on the door of diseases.")

#Buttons

calc_bmi = Button(text= " Calculate BMI", command= Calculate_BMI)
calc_bmi.grid(row= 4, column= 1)

window.mainloop()