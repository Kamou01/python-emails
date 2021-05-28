import smtplib


s = smtplib.SMTP('smtp.gmail.com', 587)
sender_email_id = 'kamogelomkonto01@gmail.com'
receiver_email_id = 'zakjardien23@gmail.com'
password = input("Enter senders email password")

s.starttls()

s.login(sender_email_id, password)

message = "hi guys how are you. i am doing fine\n"
message = message + "How was your task yesterday"

s.sendmail(sender_email_id, receiver_email_id, message)

s.quit()
