"""
Main file for the Anime Downloader

Author: Muhaimin Sarker
Started: September 30, 2020
"""

import animeSeriesURLDownloader
import multiURLopener

print("Welcome to the Anime Downloader! Here are 3 things you need to use the Anime Downloader:")
print("1. The episode you want to start the download with" + "\n" + "2. The episode you want to end with"
+ "\n" + "3. An AnimePahe link of ANY episode of the anime" + "\n")

startEpisode= int(input("Which episode would you like to start from? "))
endEpisode = int(input("Which episode would you like to end with? "))

paheURL= input("What is a episode URL for this anime in AnimePahe? ")

episodeURLlist= animeSeriesURLDownloader.pageFinder(paheURL)

fileName = input("What would you like the name of your file to start with ")
animeSeriesURLDownloader.selectedDownloadURLs(startEpisode, endEpisode, episodeURLlist, fileName)

print("Put all download links for your anime", "into a .txt file called", fileName)

openAll = input("Would you like to open all of them? Y or N ")  

if openAll == "Y" or openAll == "y":
    multiURLopener.multiURLopener(fileName + ".txt")
else:
    print("Have a nice day!")
