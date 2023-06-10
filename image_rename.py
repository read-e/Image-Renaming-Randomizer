import os
import random

def rename(pathName):
    answerFilePath = os.path.join(pathName, "..\\", "ANSWER_KEY.txt")
    print(answerFilePath + "\n")
    f = open(answerFilePath, "w")

    for directory in os.listdir(pathName):
        randomNum1 = random.randint(0, 1000)
        newDirName = str(randomNum1)
        f.write(repr(directory) + " was renamed to " + newDirName + ".txt\n")
        dirPath = os.path.join(pathName, directory)
        newDirPath = os.path.join(pathName, newDirName)
        os.rename(dirPath, newDirPath)

        for file in os.listdir(newDirPath):
            randomNum2 = random.randint(0, 10000)
            newImgName = str(randomNum2)
            filePath = os.path.join(newDirPath, file)
            extension = os.path.splitext(file)[1]  # Get the file extension
            newImgPath = os.path.join(newDirPath, newImgName + extension)
            os.rename(filePath, newImgPath)
            f.write("->" + repr(file) + " was renamed to " + repr(newImgName + extension) + "\n")
        f.write("\n\n")
    print("\n\n")
    print("The folders and images have been successfully renamed. Please check your desktop for the answer key.\n")

print("\n******************\n\nEnter the EXACT name of the filepath which contains the folders of the controls:\n")
pathName = input()
print("\n" + pathName + "\n")
if not os.path.exists(pathName):
    print("Path does not exist, exiting...\n\n")
    exit(-1)
else:
    print("Path exists, renaming...\n\ncreating...\n")

rename(pathName)
