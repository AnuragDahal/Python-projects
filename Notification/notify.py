import win10toast
#win10toast is a module that can be used to display windows 10 notifications
import datetime
WPARAM=42

data=datetime.datetime.now()
data=str(data)

toast=win10toast.ToastNotifier()	#creating an object of ToastNotifier class
toast.show_toast("Breaking NEws",f"{data}you are in danger the money you have kept in your bank has been robbed.",duration=10)
