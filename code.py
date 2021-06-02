import smtplib  #This library is used to open gmail server n work with it
import base64  #Encoding of content is done using this library
from email.mime.text import MIMEText   #To work with text portion of mail 
from email.mime.multipart import MIMEMultipart  # To attach imagaes or pdf or anything else
from email.mime.base import MIMEBase  
from email.mime.image import MIMEImage
from email import encoders  # To encode

#from html_part import content
#from namelist import ids
from dotenv import load_dotenv
import os

with open('Namastesirmaam.html') as fopen:
    """load htm content"""
    content=fopen.read()
with open('namelist.txt')as fopen:
    """load namelist ids"""
    uids=list(set(fopen.read().splitlines()))


load_dotenv()
email_user = os.getenv("EMAIL") # The Id from which mail will be sent
email_password =os.getenv("PASSWD") #password of ID from which mail will be sent (It is only with u in ur IDE so safe to use totally)
print(email_user+email_password)
count=0
for id in uids:
    try:       
        email_send = id #Ask for entering E-mail address to whom mail to be sent
        
        #paragraph=input("Enter paragraph")  #Ask for paragarph which has to be added in the middle of mail format.
                                            #It can be copied and pasted from google docs or anything
        #Subject of mail
        subject = 'Deadline For Registration Of Cover-Songsters Is Over| Vee Studio'


        msg = MIMEMultipart()
        msg['From'] = email_user  #Takes email address of ur ID
        msg['To'] = email_send  # Take email address of whom it wll be sent
        msg['Subject'] = subject  #Takes Subject

        #Make a format of email in google Doc which can be text with bold words and some words with link in it 
        #and download it as html not pdf or any other file type which is maileformat_html.html in this folder
        #We will be sending html mail not text coz if text is sent no bold wrods or attached links woth words will be seen
        #After being sent the receiver's browser will convert that html to beautiful text as we do while making website
        #Here "Love is not life" is the sentence which will be reeplaced by our sentence or paragraph
        #mailformat_html.html conatins html code of google sheet or simply mail format 
        #Open it with Notepad and type ctr + f search for "Love is not life" and copy all html code before that sentence and paste it
        #in first string variable and copy another portion of html code after sentence"Love is not life" and paste it in second string variable
        
        # we will concatenate first,second and paragraph as they are still string and assign it to one variable text

        body = str(content)  #Convertion of text string again to string and assigning it to body variable
        msg.attach(MIMEText(body,'html'))  #Attaching this string as html script with message

        filename='images/image1.png'  # Name of atttachment to be sent.Must be in same folder as code
        attachment  =open(filename,'rb').read()      # open attachment and read  it

        image = MIMEImage(attachment)
        image.add_header('Content-ID', '<linkedin>')
        msg.attach(image)

        filename='images/image2.jpg'  # Name of atttachment to be sent.Must be in same folder as code
        attachment  =open(filename,'rb').read()      # open attachment and read  it

        image = MIMEImage(attachment, _subtype='jpeg')
        image.add_header('Content-ID', '<photo>')
        msg.attach(image)

        filename='images/image3.png'  # Name of atttachment to be sent.Must be in same folder as code
        attachment  =open(filename,'rb').read()      # open attachment and read  it

        image = MIMEImage(attachment)
        image.add_header('Content-ID', '<youtube>')
        msg.attach(image)

        filename='images/image4.png'  # Name of atttachment to be sent.Must be in same folder as code
        attachment  =open(filename,'rb').read()      # open attachment and read  it

        image = MIMEImage(attachment)
        image.add_header('Content-ID', '<facebook>')
        msg.attach(image)

        filename='images/image5.png'  # Name of atttachment to be sent.Must be in same folder as code
        attachment  =open(filename,'rb').read()      # open attachment and read  it

        image = MIMEImage(attachment)
        image.add_header('Content-ID', '<instagram>')
        msg.attach(image)



        # part = MIMEBase('application','octet-stream')  # As attachment is pdf "application" is used as content type
        # part.set_payload((attachment).read())
        # encoders.encode_base64(part)  #Encoded before being sent trough mail
        # part.add_header('Content-Disposition',"attachment; filename= "+filename)  # This part is sent as attachment

        #msg.attach(part)  # Attachment is attached with main body of mail
        # text = msg.as_string()  # Here the main thing happens where htl code is seen as clear formatted text in gmail inbox or   #simply  browser
        server = smtplib.SMTP('smtp.gmail.com',587)  #gmail server is selected and port number
        server.starttls()
        server.login(email_user,email_password)  # Login into your address is done
        server.sendmail(email_user,email_send,msg.as_string())  # mail is sent
        server.quit()  # server is closed
        print("Mail successfully sent")
        count=count+1
        continue
    except:
        print("Either email is wrong or something else")  #Diplay msg is=f recipents id is wrong or something problems happens
        continue
print(count)




