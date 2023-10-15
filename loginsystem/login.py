import customtkinter

customtkinter.set_appearance_mode("dark")#available modes are dark and light
customtkinter.set_default_color_theme("green")#available colors are blue,green and darkblue


root=customtkinter.CTk()#customtkinter.CTk() is a subclass of tkinter.Tk()
root.title("Login System") 
root.geometry("500x500")

def login():
    print("You have been logged in")


frame=customtkinter.CTkFrame(master=root)#
frame.pack(pady=20,padx=60,fill="both",expand=True)#pady and padx are padding in y and x direction respectively

label=customtkinter.CTkLabel(master=frame,text="LoginSystem",font=("Arial",20))	
label.pack(pady=20)#pady and padx are padding in y and x direction respectively

entry1=customtkinter.CTkEntry(frame,placeholder_text="Username")
entry1.pack(pady=10,padx=12)

entry2=customtkinter.CTkEntry(frame,placeholder_text="Password",show="*")
entry2.pack(pady=10,padx=12)

button=customtkinter.CTkButton(frame,text="Login",command=login)
button.pack(pady=20,padx=12)

checkbox=customtkinter.CTkCheckBox(frame,text="Remember me")
checkbox.pack(pady=10,padx=12)

root.mainloop()

