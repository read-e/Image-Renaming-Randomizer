#Liam Reidy - liamreidy.com
#created 6/9/2023
#updated 6/10/2023

#import libraries we need
import os
import random

#renaming function
def rename(pathName):
    #getting the absolute filepath of the directory you input in, and creating the answer key
    answerFilePath = os.path.join(pathName, "..\\", "ANSWER_KEY.txt")
    print(answerFilePath + "\n")
    f = open(answerFilePath, "w")

    #for each folder in the current folder...
    for directory in os.listdir(pathName):
        #generate a random number (really it's 2 that are being added together for more randomness)
        randomNum1 = random.randint(0, 10000)
        randomNum1 += random.randint(0,10000)
        #the new folder name will be this number in string format
        newDirName = str(randomNum1)
        #write the change to the answer key
        f.write(repr(directory) + " was renamed to " + newDirName + ".txt\n")
        dirPath = os.path.join(pathName, directory)
        newDirPath = os.path.join(pathName, newDirName)
        #rename the current directory path to the new directory path
        os.rename(dirPath, newDirPath)

        #for each file WITHIN each of the folders...
        for file in os.listdir(newDirPath):
            #make another random number that will be the new image name, same process as above
            randomNum2 = random.randint(0, 10000)
            randomNum2 = random.randint(0, 10000)
            newImgName = str(randomNum2)
            #filepath is the absolute filepath of the old name
            filePath = os.path.join(newDirPath, file)
            #get the extension so that we are not converting any images to different file types
            extension = os.path.splitext(file)[1]  # Get the file extension
            #put it all together !
            newImgPath = os.path.join(newDirPath, newImgName + extension)
            os.rename(filePath, newImgPath)
            #write the change to the answer key, then format with newlines
            f.write("->" + repr(file) + " was renamed to " + repr(newImgName + extension) + "\n")
        f.write("\n\n")
    print("\n\n")
    print("The folders and images have been successfully renamed. Please check your desktop for the answer key.\n")

#
#
# Program start
#
#
#take the filename and make sure it exists before passing it into the rename function
print("\n******************\n\nEnter the EXACT name of the filepath which contains the folders of the controls:\n")
pathName = input()
print("\n" + pathName + "\n")
if not os.path.exists(pathName):
    print("Path does not exist, exiting...\n\n")
    exit(-1)
else:
    print("Path exists, renaming...\n\ncreating...\n")

rename(pathName)
