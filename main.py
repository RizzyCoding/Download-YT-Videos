#IMPORTING UNDER
import os
from pytube import YouTube
#CODE UNDER
link = str(input("Enter the YT video link you want to download: ")) #defines "link" as the yt video link you enter!
os.system('cls') #Clears the terminal (makes it look nice)
yt = YouTube(link) #Gets the YT vid into a video
print("Downloading.. 50%") #Prints its 50% done
stream = yt.streams.get_highest_resolution() #Gets the YT vids highest res
os.system('cls') #Clears the terminal (makes it look nice)
print("Downloading... 75%") #Prints its 75% done
stream.download() #Downloads the video.
os.system('cls') #Clears the terminal (makes it look nice)
print("100% Downloaded!") #Prints that its finished
x = input("Press any ket to exit... ") #Stops the terminal from instant closing
