# Discord-Emoji-Collection


## Usage of the Browser GUI
1. paste a link into the input field, press "Add Emoji" and your emoji is ready to be used.
2. press "Browse", search your system for a suitable .json file, select it and press "Import" to load all your saved emojis into the GUI.
3. press "Export" to export your emojis currently displayed in the GUI to a json file so that you can import them again later. Important, because after closing the Browser all unsaved emojis are irrevocably lost.


## How to get the emoji links
1. go to Discord and enable the Developer mode
2. then right click on an emoji (it should be single in a message)
3. press "Copy Link" - NOT "Copy Message Link"
4. paste the link into the GUI, a .txt file (which you then simply have to convert) or into a .json file - note the corresponding formatting rules!


## Sense of the individual files

### index.html
The main file that represents your Browser GUI.

### urls.txt
A file  you can copy your emoji links in (each link on a separate line) to have them quickly available for the future

### jsoner.py
A Python script that converts your nice urls.txt into a .json file that can be used by index.html. Just import it via Browser GUI to use your emojis

### urls.json
The file the jsoner.py would spit out

### emojis.txt
Just a bunch of emoji links.

### emoji-examples.json
A json file you can import directly.