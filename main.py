# Try importation of modules and print an error otherwise

print("[+] Importing modules.....")
try:
	from selenium import webdriver
	from bs4 import BeautifulSoup
	import time
except Exception as e:
	print("[-] " + str(e))

# Configure the webdriver
print("[+] Starting Selenium.....")
try:
	driver = webdriver.Chrome()
except Exception as e:
	print("[-] " + str(e))

##################################### CITIZEN SCRAPPER ######################################
def CitizenScrapper():
	latest_news_link = [] 
	latest_news_title = []

	# Open the url to Citizen News page
	print("[+] Starting Scrapper  at Citizen.....")
	try:
		driver.get("https://citizentv.co.ke/") # get the url
	except Exception as e:
		print("[-] " + str(e))

	# extract the data
	content = driver.page_source
	soup = BeautifulSoup(content, features="html.parser")
	for div in soup.findAll('div', attrs={'class':'col-md-4 col-sm-6 col-xs-12 no-padding', 'class':'col-md-4 col-sm-6 col-xs-12 no-padding mobile-more-less-stories'}):
		news = div.find('a', href=True)
		link = news['href']
		title = news['title']
		latest_news_link.append(link)
		latest_news_title.append(title)

	for l in latest_news_link:
		print("[+] URL: " + str(l))
	for t in latest_news_title:
		print("[+] TITLE: " + str(t))

# Call the function to perform scrapping
CitizenScrapper()


######################################### KTN SCRAPPER ############################################
def KtnScrapper():
	# Initialize KTN news Title and Links
	ktn_news_links = []
	#ktn_news_titles = []

	# Open the url at KTN News page
	print("[+] Starting Scrapper at KTN..... ")
	try:
		driver.get("https://www.standardmedia.co.ke/ktnnews/") # get the url
	except Exception as e:
		print("[-] " + str(e))

	# Extract the data
	ktn_content = driver.page_source
	ktn_soup = BeautifulSoup(ktn_content, features="html.parser")
	for div in ktn_soup.findAll('div', attrs={'class':'card-body'}):
		ktn_news = div.find('a', href=True)
		ktn_news_link = ktn_news['href']
		ktn_news_links.append(ktn_news_link)

	for link in ktn_news_links:
		print("[+] URL " + str(link))
KtnScrapper()


########################################### NTV SCRAPPER ###################################

# Initialize NTV news Title and Links
def NtvScrapper():
	ntv_news_links = []


	# Open the url at NTV News page
	print("[+] Starting Scrapper at NTV..... ")
	try:
		driver.get("https://ntv.nation.co.ke/") # get the url
	except Exception as e:
		print("[-] " + str(e))

	# Extract the data
	ntv_content = driver.page_source
	ntv_soup = BeautifulSoup(ntv_content, features="html.parser")
	for div in ntv_soup.findAll('div', attrs={'class':'desc'}):
		ntv_news = div.find('a', href=True)
		ntv_news_link = ntv_news['href']
		ntv_news_links.append(ntv_news_link)


	for link in ntv_news_links:
		print("[+] URL " + str(link))
# Call the function to scrape NTV news
NtvScrapper()


	



