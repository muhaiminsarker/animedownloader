"""
Anime Series URL Downloader
Author: Muhaimin Sarker
Started: October 2, 2020
"""
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

driver_path = os.path.dirname(os.path.realpath("chromedriver.exe") + "\chromedriver.exe")
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

def pageFinder(link):
    """
    Returns a list with all episode URLs of a specific anime (NOT THE DOWNLOAD LINK)
    
    Parameter link: the episode link 
    Precondition: link must be a valid episode link and a STRING
    """
    quote_page= link
    page = requests.get(quote_page)
    soup = BeautifulSoup(page.content, "html.parser")

    pages= []
    aTagData= soup.find("div", id= "scrollArea")    
    for links in aTagData.find_all('a'):
        pages.append("http://animepahe.com" + links.get('href'))
    return pages

def downloadURL(start, end, links):
    """
    Returns the list with all download links for specific episode range 
    using a list of episode links

    Parameter start: episode to start from
    Precondition: start must be an INT that is >= 0

    Parameter end: episode to end with 
    Precondition: end must be an INT that is >= start

    Parameter links: list of episode links
    Precondition: links must be a list that has a >= length than start and end

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
    Returns text file name

    Parameter start: episode to start from
    Precondition: start must be an INT that is >= 0

    Parameter end: episode to end with 
    Precondition: end must be an INT that is >= start

    Parameter episodeURLList: list of episode links
    Precondition: links must be a list that has a >= length than start and end

    Parameter name: name of file to write to
    Precondition: name must be a STRING with NO special characters

    """
    f= open(name + ".txt", "w")
    allDownloads = downloadURL(start, end, episodeURLList)
    for i in allDownloads:
        f.write(i + "\n")