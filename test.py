from bs4 import BeautifulSoup as bs                 
from selenium import webdriver
from tkinter import *
import smtplib

ethereum_threshold = 4300

gmail_user = 'gharish15@gmail.com'
gmail_password = 'bicijnjnjraaacpu'

sent_from = gmail_user
to = ['gharish15@gmail.com']
subject = 'Ethereum price target reached <EOM>'
body = ''

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

#Driver path for firefox geckodriver
DRIVER_PATH = '/home/harish/geckodriver'
#command to open firefox
driver = webdriver.Firefox(executable_path = DRIVER_PATH)
#opening webpage for crypto price
response = driver.get("https://crypto.com/price")
#Infinite Loop for checking ethereum price
while(1):
	def scrap():
		flag = 0
		html = driver.page_source
		soup = bs(html,'lxml')
		#Obtaining all crypto price
		crypto = soup.find_all('div', attrs={'class' : 'css-b1ilzc'})
		#index associated with ethereum
		ethereum_text = crypto[1].text
		#Removing symbols and convering to float
		ethereum_text = ethereum_text.replace(",", "")
		ethereum_text = ethereum_text.replace("$", "")
		ethereum =float(ethereum_text)
		#condition to check if threshold price is reached
		if (ethereum > ethereum_threshold):
			flag = 1
		return flag
	
	value = scrap()
	if(value == 1):
		"""
		root = Tk()
		root.geometry("400x200")
		label = Label(root, text = "Target reached", relief = RAISED).pack()
		root.mainloop()
		"""
		smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		smtp_server.ehlo()
		smtp_server.login(gmail_user, gmail_password)
		smtp_server.sendmail(sent_from, to, email_text)
		smtp_server.close()  
		break
