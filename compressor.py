#!/usr/bin/python

from PIL import Image #Importing the Pillow library
import os #Importing os library to access folders


downloads_folder_path= "C:\\Users\\diego\\Downloads\\"


if __name__ == "__main__": #Checking if we running the program

	for filename in os.listdir(downloads_folder_path): #Iterating through files in dir

		name, extension = os.path.splitext(downloads_folder_path + filename) #Saving name and extesion

		if extension in [".jpeg", ".png", ".jpg",".JPEG", ".PNG", ".JPG"]: #Looking if is an image
			picture= Image.open(downloads_folder_path + filename) #Opening it as an Image obj
			picture.save(downloads_folder_path + "compressed_" + filename, optimize=True, quality=55)
			#Saved picture with lower quality to save space

			os.remove(downloads_folder_path + filename)
			print(name + ":", extension)
