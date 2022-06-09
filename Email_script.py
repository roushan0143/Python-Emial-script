import smtplib as s

ob=s.SMTP("smtp.gmail.com",587)

#sender email login deatils
username = 'roushan.kumaar195'
password = 'xyz'

#subjects and body content
subject="Sending email using python"
body="This is tutorial of sending emial using python script in simple state"

#formating for subjects and body
message="Subject:{}\n\n{}".format(subject,body)

#reciver email 
listOfAddress=["ashu.himanshu978@gmail.com","roushan.kumar195@gmail.com"]


ob.starttls()

ob.login(username, password)

ob.sendmail(username , listOfAddress,message)

print("send successfully...")

ob.quit()