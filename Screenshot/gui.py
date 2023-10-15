# import pyautogui
# import time
# import tkinter as tk

# def screenshot():
#     # used time module to generate unique name for each screenshot
#     name=time.time()
#     name=f"C:/Users/freef/OneDrive/Desktop/Rw projects/Screenshot/{name}.png"
#     # time.sleep(5)# time to open the window
#     image=pyautogui.screenshot()# pip install pillow 
#     # pillow is a dependency of pyautogui
#     image.save(name)
#     image.show()
    
# root=tk.Tk()
# frame=tk.Frame(root)
# frame.pack()

# button=tk.Button(frame,text='Take screenshot',command=screenshot)
# button.pack(side=tk.Left)


# close=tk.Button(frame,text='close',command=quit)
# close.pack(side=tk.LEFT)

# root.mainloop()


import pyautogui
import time
import tkinter as tk
from tkinter import messagebox


def screenshot():
    try:
        # Generate a unique name for each screenshot using the current timestamp
        name = time.time()
        name = f"C:/Users/freef/OneDrive/Desktop/Rw projects/Screenshot/{name}.png"
        
        # Capture a screenshot
        image = pyautogui.screenshot()
        
        # Save the screenshot to the specified path
        image.save(name)
        
        # Show a success message
        messagebox.showinfo("Screenshot", f"Screenshot saved as {name}")
    except Exception as e:
        # Handle any exceptions that may occur during the screenshot process
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text='Take screenshot', command=screenshot)
button.pack(side=tk.LEFT)

close = tk.Button(frame, text='Close', command=quit)
close.pack(side=tk.LEFT)

root.mainloop()


