# Image-Renaming-Randomizer
 - [Prerequisites](prerequisites)   
 - [Instructions](instrutions)
 - [Troubleshooting](troubleshooting)
      
      
**_Please make a backup of your images before you run this program. Do not run it twice on the same data, or the answer key will be overwritten_**  
  
## Prerequisites 
 - 🐍 Have the most recent version of Python installed
 - 🪟 Windows 10 or 11 
 - 📁 Set up your data so there is 1 folder that contains many other folders. Each of the folders within the first one contain the images you need. For example, the folder "Set 1" contains all the "Control" and "PFOS" folders in it, where each of the "Control" and "PFOS" folders contain the images themselves. THe folders do not have to match the names in this example, just the structure.
 - 🖼️ Make a backup !
  
  
## **Instructions:**

1. To download the code, click ```<>Code``` in the top right, then ```Download ZIP```. You'll have to unzip the folder once it is downloaded.
2. BACKUP ALL IMAGES. This script works, but everyone's has their computer set up a little different, and we don't want to lose any data. Copy the folder that has the folders of images, and put it somewhere safe in a new "Backup" folder. Should something go wrong, this will allow you to still do the randomization by hand.
3. Download  ```image_rename.py``` from this repository
4. Open your downloads folder, right click ```image_rename.py``` and ```copy file path```
5. Open a ```Terminal``` or ```Command pPrompt``` window by pressing the windows key and typing "terminal" or "command prompt"
6. Type ```Python PATH_YOU_COPIED``` where ```PATH_YOU_COPIED``` is the filepath you copied. You can paste it using ```ctrl + v``` or  ```ctrl + shift + v```. **Press enter to run the program.**
7. The program will start to run. Open ```File explorer``` and navigate to the folder that contains the other folders which hold the images. **NOTE:** [See prerequisites to make sure your folders are set up correctly](prerequisites)
8. Click the bar at the top of ```file explorer``` that tells you which folder you are in. This will expand it to the full filepath, and highlight it. Copy this path.
9. Paste this new filepath into the Python program, and hit enter.
10. Barring any errors Python spat at you, everything has been succesfully renamed! See the answer key in the same directory the main folder (that holds everything else) was kept.
 

## **Troubleshooting:**
1. ``` Python : The term 'Python' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.```
  
  Make sure you have Python installed. If you do, this likely means you need to add Python to your path variable (you don't need to insall anything new if you already have Python)
  instructions can be found here: https://datatofish.com/add-python-to-windows-path/
  
2. **Where is my answer key?**    

  It should be in the same directory as the "main folder" (the folder that holds everything). If you can't find it, search your computer for the ```ANSWER_KEY.txt" file.
  
3. **I can't paste anything in the terminal!**  

 Try using ```ctrl + shift + v```
 
 
 
 
 🐟 🐟 🐟
