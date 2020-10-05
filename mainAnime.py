"""
Main file for the Anime Downloader

Author: Muhaimin Sarker
Started: September 30, 2020
"""

import animeXMLextractor
import animeSeriesURLDownloader
import multiURLopener

episodeList= animeXMLextractor.animeEpisodeList()
nameList= animeXMLextractor.animeNameList()

animeQuery= input("What anime from your list would you like to download? ")

queryList= []
for name in nameList:
    if name.startswith(animeQuery) or name.lower().startswith(animeQuery) :
        queryList.append(name)

for i in range(len(queryList)):
    print(i, queryList[i])

specificAnimeQuery= int(input("Which number would you like to choose "))
print("You have chosen", queryList[specificAnimeQuery], "which has", episodeList[nameList.index(queryList[specificAnimeQuery])], "episode(s)")
startEpisode= int(input("Which episode would you like to start from? "))
endEpisode = int(input("Which episode would you like to end with? "))

paheURL= input("What is a episode URL for this anime in AnimePahe? ")

episodeURLlist= animeSeriesURLDownloader.pageFinder(paheURL)

fileName = animeSeriesURLDownloader.selectedDownloadURLs(startEpisode, endEpisode, episodeURLlist, queryList[specificAnimeQuery])

print("Put all download links for", queryList[specificAnimeQuery], "into a .txt file called", fileName)

openAll = input("Would you like to open all of them? Y or N ")  
if openAll == "Y" or openAll == "y":
    multiURLopener.multiURLopener(fileName)
else:
    print("Have a nice day!")
