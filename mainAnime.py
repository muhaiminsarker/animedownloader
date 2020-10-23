"""
Main file for the Anime Downloader

Author: Muhaimin Sarker
Started: September 30, 2020
"""

import animeSeriesURLDownloader
import multiURLopener
import os
import string

print("Welcome to the Anime Downloader! Here are 3 things you need to use the Anime Downloader:")
print("1. An AnimePahe link of ANY episode of the anime" + "\n" + 
"2. The episode you want to start the download with" + "\n" + "3. The episode you want to end with"+ "\n")

paheURL= input("What is a episode URL for this anime in AnimePahe? ")

episodeURLlist= animeSeriesURLDownloader.pageFinder(paheURL)

episodeInput = False
while episodeInput == False:
    try:
        startEpisode= int(input("Which episode would you like to start from? "))
        assert startEpisode <= len(episodeURLlist) and startEpisode >= 0
        endEpisode = int(input("Which episode would you like to end with? "))
        assert endEpisode <= len(episodeURLlist) and endEpisode >= 0 and endEpisode >= startEpisode
        episodeInput = True
    except: 
        print("That is not a correct episode NUMBER")

fileNameInput = False
invalidFileName = ["CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9"
, "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"]

while fileNameInput == False:
    try:
        fileName = input("What would you like the name of your file to start with? " + "\n")
        assert fileName not in invalidFileName
        fileNameInput = True
    except: 
        print("That is not a valid file name to start with")
        
animeSeriesURLDownloader.selectedDownloadURLs(startEpisode, endEpisode, episodeURLlist, fileName)

print("Put all download links for your anime", "into a .txt file called", fileName + ".txt")

openAll = input("Would you like to open all of them? Y or N ")  

if openAll == "Y" or openAll == "y":
    multiURLopener.multiURLopener(fileName + ".txt")

deleteFile = input("Would you like to delete the file? Y or N ")

if deleteFile == "Y" or "y":
    os.remove(fileName + ".txt")

print("\n" + "Have a nice day!")