import bs4 as bs
import urllib.request
import re
import datetime
import matplotlib.pyplot as plt
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import os

#Modify these variables for your own use before you run this script for the first time----------------------------------
fear_greed_index_dir = 'Drive:\PathTo\\fear_greed_index.pkl' #location where you save all the values for plotting
png_dir = 'Drive:PathTo\\fear_greed_index_daily.png' #location where you save the daily chart
sender_email = 'sender_email@outlook.com'
sender_password = 'sender email password'
recipient_email = 'recipient_email@outlook.com'
email_server_addr = 'smtp-mail.outlook.com' #this is the correct one for outlook
email_server_port = 587 #this is the correct one for outlook
#crawls the fear & greed index from cnn---------------------------------------------------------------------------------
sauce = urllib.request.urlopen('https://money.cnn.com/data/fear-and-greed/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')
body = soup.body
divs = soup.find_all('div', class_ = body)
line = divs[8].text
fear_greed_index = re.search('[0-9][0-9]', line).group()
#get today's date in YYYYMMDD format------------------------------------------------------------------------------------
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
#save the record--------------------------------------------------------------------------------------------------------
row_dict = {'date': date, 'fear_greed_index': fear_greed_index}
if (os.path.exists(fear_greed_index_dir)):
    df = pd.read_pickle(fear_greed_index_dir)
    df= df.append(row_dict, ignore_index = True)
else:
    df = pd.DataFrame(data=row_dict)
df.to_pickle(fear_greed_index_dir)
#make the plot and save-------------------------------------------------------------------------------------------------
plt.figure(figsize=(15,12))
plt.plot(df['date'], df['fear_greed_index'], marker = '.')
tick_range = range(0, 105, 5)
plt.xticks(rotation=25)
plt.yticks(tick_range)
ax = plt.axes()
ax.yaxis.grid()
plt.xlabel('Date')
plt.ylabel('Fear Greed Index')
plt.title('Line Chart of Fear Greed Index')
plt.savefig(png_dir)
#send to the email address----------------------------------------------------------------------------------------------
msg = MIMEMultipart()
msg['Subject'] = 'Fear Greed Index ' + date
msg['From'] = sender_email
msg['To'] = recipient
text = MIMEText("Today's fear greed index value is " + fear_greed_index + ".")
msg.attach(text)
img_data = open(png_dir, 'rb').read()
image = MIMEImage(img_data)
msg.attach(image)
SMPT = smtplib.SMTP(email_server_addr, email_server_port)
SMPT.starttls()
SMPT.login(sender_email, sender_password)
SMPT.sendmail(sender_email, recipient_email, msg.as_string())
SMPT.quit()