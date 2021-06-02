from email.mime import image
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders as Encoders
from dotenv import load_dotenv
import os
from csv import reader
from jinja2 import Environment, FileSystemLoader

''' template rendering from jinja '''
env = Environment(loader=FileSystemLoader('%s/templates/'%os.path.dirname(os.path.abspath(__file__))))

def renderhtml(reciever):
    return env.get_template('draft.html').render(reciever=reciever)


''' coverting csv to dict '''
def row_to_dict(row):
    return {'name':row[0], 'email':row[1]}

''' initial setup '''
load_dotenv()
sender_mail=os.getenv("EMAIL")
sender_pwd=os.getenv("PASSWD")

print(sender_pwd + sender_mail)

''' reading csv file '''
recievers = []
with open('test.csv','r') as csv_file:
    data = reader(csv_file, delimiter=',')

    isHeading = True
    for row in data:
        if not isHeading:
            recievers.append(row_to_dict(row))
        isHeading = False


''' attaching photo and files '''
photo = 'templates/images/image1.png'
photofile = open(photo, 'rb').read()
photoimg = MIMEImage(photofile)
photoimg.add_header('Content-ID', '<photo>')

photo = 'templates/images/image2.png'
photofile = open(photo, 'rb').read()
fbimg = MIMEImage(photofile)
fbimg.add_header('Content-ID', '<facebook>')

photo = 'templates/images/image3.png'
photofile = open(photo, 'rb').read()
linkedinimg = MIMEImage(photofile)
linkedinimg.add_header('Content-ID', '<linkedin>')

photo = 'templates/images/image4.png'
photofile = open(photo, 'rb').read()
instaimg = MIMEImage(photofile)
instaimg.add_header('Content-ID', '<instagram>')

prospectus = MIMEBase('application', "octet-stream")
prospectus.set_payload(open("Prospectus.pdf", "rb").read())
Encoders.encode_base64(prospectus)
prospectus.add_header('Content-Disposition', 'attachment; filename="Prospectus.pdf"')

proposal = MIMEBase('application', "octet-stream")
proposal.set_payload(open("Sponsorship Proposal.pdf", "rb").read())
Encoders.encode_base64(proposal)
proposal.add_header('Content-Disposition', 'attachment; filename="Sponsorship Proposal.pdf"')

# video = MIMEBase('application', "octet-stream")
# video.set_payload(open("video.mp4", "rb").read())
# Encoders.encode_base64(video)
# video.add_header('Content-Disposition', 'attachment; filename="video.mp4"')

''' main mail sending, lol '''
server = SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_mail, sender_pwd)

for reciever in recievers:
    subject = "Request for collaboration between " + reciever['name'] + " and Vee studio"

    msg = MIMEMultipart()
    msg['From'] = sender_mail
    msg['To'] = reciever['email']
    msg['Subject'] = subject

    body = str(renderhtml(reciever['name']))
    msg.attach(MIMEText(body, 'html'))
    
    msg.attach(photoimg)
    msg.attach(fbimg)
    msg.attach(linkedinimg)
    msg.attach(instaimg)
    msg.attach(prospectus)
    msg.attach(proposal)
    # msg.attach(video)


    server.sendmail(reciever['name'], reciever['email'], msg.as_string())

    print("Successful, sent to " + reciever['name'])
    continue

server.quit()


    
    





