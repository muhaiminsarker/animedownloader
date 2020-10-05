"""
Anime List XML extractor
Author: Muhaimin Sarker
Started: September 30, 2020
Date:
"""
from bs4 import BeautifulSoup
#Next update: No need to input name of file into code; chooses the one XML file should be there
infile = open("animelist.xml", "r") 
#Set the variable contents to the XML file being read
contents= infile.read()
#uses BeautifulSoup module to categorize the contents read as an XML file
soup = BeautifulSoup(contents,'xml')

def animeEpisodeList():
    """
    Returns an list of episodes
    """
    episodes= soup.find_all("series_episodes")
    episodeList= []
    for episode in episodes:
        episodeList.append(episode.get_text())
    return episodeList

def animeNameList():
    """
    Returns an list of anime names
    """
    titles= soup.find_all("series_title")
    titleList = []
    for title in titles:
        titleList.append(title.get_text())
    return titleList