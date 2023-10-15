import smtplib  # built in module
# sender email is constant
receiver_email = input("Enter receiver email: ")
message = input("Enter your message: ")


def sendEmail(receiver_email, message):

    server = smtplib.SMTP('smtp.gmail.com', 587)  # 587 is port number
    server.starttls()  # tls is transport layer security
    server.login("sender_email", "sender_password")  # login to your email
    # send email,sender_email and receiver_email are string
    server.sendmail('sender_email', receiver_email, message)
    server.quit()  # close the server


sendEmail(receiver_email, message)  # call the function
