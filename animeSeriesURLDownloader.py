"""
Anime Series URL Downloader
Author: Muhaimin Sarker
Started: October 2, 2020
"""
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver_path = "C:/Users/sarke/Desktop/Programming/Projects/Anime Downloader/chromedriver.exe"
#For my use, I use Brave Browser as my default browser and make it work using that. 
#Brave Browser is best because ads and other things are removed automatically from webpages 
##This allows me to web scrape a lot more easier
brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path

#Adds a headless feature so that Chrome can run in background
option.add_argument("--headless")
#Makes sure that error messages don't pop up unless they are fatal
option.add_argument('log-level=3')

# Create new Instance of Chrome
def pageFinder(link):
    """
    Returns a list with all episode URLs of a specific anime (NOT THE DOWNLOAD LINK)
    """
    quote_page= link
    page = requests.get(quote_page)
    soup = BeautifulSoup(page.content, "html.parser")

    pages= []
    aTagData= soup.find("div", id= "scrollArea")    
    for links in aTagData.find_all('a'):
        pages.append("http://animepahe.com" + links.get('href'))
    return pages


# Working function as other one doesn't work for EVERY SINGLE ANIME
# One link at a time
# def downloadURL(link):
#     """
#     Returns the string with the download link for the specific episode using a singular episode link
#     """
#     browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
#     browser.get(link)
#     browser.add_cookie({"name": "res", "value": "1080"})
#     browser.get(link)
    
#     soup = BeautifulSoup(browser.page_source, "html.parser")
#     soup = soup.prettify()

#     urlLocation= soup.find("kwik.cx/e")
#     urlEndLocation= soup.find('";', urlLocation)
#     return soup[urlLocation:urlEndLocation].replace("/e/", "/f/")

def downloadURL(start, end, links):
    """
    Returns the list with all download links for the specific episode using a singular episode link
    """
    allDownload = []
    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
    browser.get(links[start-1])
    browser.add_cookie({"name": "res", "value": "1080"})
    browser.get(links[start-1])

    soup = BeautifulSoup(browser.page_source, "html.parser")
    soup = soup.prettify()

    urlLocation= soup.find("kwik.cx/e")
    urlEndLocation= soup.find('";', urlLocation)
    allDownload.append(soup[urlLocation:urlEndLocation].replace("/e/", "/f/"))
    

    for i in range(start, end):
        browser.get(links[i])
        soup = BeautifulSoup(browser.page_source, "html.parser")
        soup = soup.prettify()

        urlLocation= soup.find("kwik.cx/e")
        urlEndLocation= soup.find('";', urlLocation)
        allDownload.append(soup[urlLocation:urlEndLocation].replace("/e/", "/f/"))
    return allDownload

def selectedDownloadURLs(start, end, episodeURLList, name):
    """
    Write selected episode(s)' download links to a text file. 
    Return text file name
    """
    f= open(name + " Episodes " + str(start) + " - " + str(end) + ".txt", "w")
    allDownloads = downloadURL(start, end, episodeURLList)
    for i in allDownloads:
        f.write(i + "\n")
    return name + " Episodes " + str(start) + " - " + str(end) + ".txt"