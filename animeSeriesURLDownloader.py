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
brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path

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


def downloadURL(link):
    """
    Returns the string with the download link for the specific episode using a singular episode link
    """
    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
    browser.get(link)
    browser.add_cookie({"name": "res", "value": "1080"})
    browser.get(link)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    browser.quit()

    scriptData= soup.find_all("script")
    urlScript= str(scriptData[5])
    urlLocation= urlScript.find("kwik.cx/e")
    urlEndLocation= urlScript.find('";')
    return urlScript[urlLocation:urlEndLocation].replace("/e/", "/f/")

def selectedDownloadURLs(start, end, episodeURLList, name):
    """
    Write selected episode(s)' download links to a text file. 
    Return text file name
    """
    f= open(name + " Episodes " + str(start) + " - " + str(end) + ".txt", "w")
    # firstStatement = "These are the download links for episodes " + str(start) + " to " + str(end) + " for " + name + "\n" 
    # f.write(firstStatement)
    for i in range(start-1, end):
        f.write(downloadURL(episodeURLList[i]) + "\n")
    return name + " Episodes " + str(start) + " - " + str(end) + ".txt"