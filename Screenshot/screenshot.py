import pyautogui
import time
name=input("Enter the name of the screenshot: ")
print("You have 7 seconds to open the window you want to take a screenshot of"	)	
def screenshot(name):
    time.sleep(7)
    pic=pyautogui.screenshot()#pip install pillow
    pic.save(f"C:/Users/freef/OneDrive/Desktop/Rw projects/Screenshot/{name}.png")
    print("Screenshot saved")
    pic.show()
    
screenshot(name)