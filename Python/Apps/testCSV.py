from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import csv
# with open('f:\\temp\\pytest.csv', 'rt') as csvfile:
# data = csv.reader(csvfile)


def readcsv():
    reader = csv.DictReader(open("f:\\temp\\pytest.csv"))
    for row in reader:
        print(row)
        for a, b in row.items():
            print(a, b)


def sendmail():
    me = "xx@xxx.co.il"
    you = "xx@xxx.co.il"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "איגרת שכר"
    msg['From'] = me
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
    html = """\
    <html>
    <head></head>
    <body>
        <p>! גיא, שלום<br>
        How are you?<br>
        Here is the <a href="https://www.python.org">link</a> you wanted.
        </p>
    </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    s = smtplib.SMTP('172.20.1.76')
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(me, you, msg.as_string())
    s.quit()


# readcsv

reader = csv.DictReader(open("f:\\Temp\\report.csv"))
# print(list(reader))
#for _ in reader:
 #   print(_.keys())
    # for i in _.keys():
    #   print(i)
t1 = reader

print(t1['xxx@xxx.co.il'])



https://app.box.com/s/dgsen8bo7teq6qj84lvhbbf0u2bo00ma/file/930353773301?sb=/details


https://app.box.com/s/dgsen8bo7teq6qj84lvhbbf0u2bo00ma/folder/158256998235

https://app.box.com/s/dgsen8bo7teq6qj84lvhbbf0u2bo00ma/folder/158257734578


|Set-CASMailbox -owaenabled $false