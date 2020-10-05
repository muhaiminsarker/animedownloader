from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


driver_path = "C:/Users/sarke/Desktop/Programming/Projects/Anime Downloader/chromedriver.exe"
brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path
# option.add_argument("--incognito") OPTIONAL
#option.add_argument("--headless")

# Create new Instance of Chrome
browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
#browser = webdriver.PhantomJS()
browser.get("https://animepahe.com/play/8e7ec187-93b1-ea8b-5fed-61061b935c72/b711b7c44122de8828266f93a119911f3b635c6cbe7d019d480c2893520776ab")
browser.add_cookie({"name": "res", "value": "1080"})
browser.get("https://animepahe.com/play/8e7ec187-93b1-ea8b-5fed-61061b935c72/b711b7c44122de8828266f93a119911f3b635c6cbe7d019d480c2893520776ab")
soup = BeautifulSoup(browser.page_source, "html.parser")
browser.quit()
scriptData= soup.find_all("script")
urlScript= str(scriptData[5])
urlLocation= urlScript.find("kwik.cx/e")
urlEndLocation= urlScript.find('";')
print(urlScript[urlLocation:urlEndLocation].replace("/e/", "/f/"))