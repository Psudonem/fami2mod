# fami2mod


Welcome to fami2mod. This is a python script that converts famitracker text exported files into mod files to be used in GBstudio projects.

# notice

This project is very much a work in progress.


## How to use
0. *Install the programs.* This tutorial requires Famitracker, OpenMPT, Python 3, and GB Studio.
1. *Prepare your song.* Normal famitracker songs cannot be used with this program. The file structure must follow these guidelines:
    
    - 64 rows
    
    - the frame number and the pattern numbers in that frame must be the same. (If you are in frame 0, the patterns must all be pattern 0)
    
    - the instrument number in famitracker is ONE LESS than the instrument numbers of GB studio. (If you want to use game boy instrument 2, your famitracker instrument must be instrument 1)
    
    - the effects column will be ignored (see next bullet). I have 	not programmed support for effects, however you may use the volume control column as you please
    
    - optional: ~~because game boy tempos do not really match up with famitracker tempos well, I have programmed in ONE effects command just so things sound exact between platforms.
      In the noise channel, if you place a **lone** tempo command (a tempo command with no notes, volume, or other effects) set at speed 6, it will translate to the game boy equivalent.
      If you can edit in OpenMPT, you can actually ignore this step.~~ nvm this doesn't work
      
     - every note in famitracker will automatically be transposed THREE OCTAVES UP in the mod format. So if you put down a C-3, it will play a C-6. 
      For the first two channels, the sound is not so drastic on the game boy, however one can easily see how troublesome it might be.
      You can easily transpose your notes up and down an octave in OpenMPT by pressing Shift-Control-Q (transpose up) and Shift-Control-A (transpose down). https://wiki.openmpt.org/Manual:_Keyboard_Actions
      
      
      
2. *Exporting to text.* After completing your song in Famitracker, click file>>export text. Enter a name and save this text file outside of your project directory.

3. *Running the script.* Next, bring modmakerII.py into the same folder where you stored the text file. Drag the text file onto modmakerII.py. This should run the script and generate a modfile.

4. *Applying the magic.* Open this modfile with OpenMPT and click save (or use the control-s shortcut). After you save it the file size should be significantly smaller. We do this because openMPT has some computer magic that makes the modfile work in GB studio that I don't know how to do in python. *any new edits to the song should be done in OpenMPT or Milkytracker.*

5. Copy the new modfile into your project assets folder and you're good to go!

##Updates:
    - 8/9/2020: version 1 released.

# Sources

I reverse engineered some of this code https://github.com/NardJ/ModTrack-for-Python/blob/master/modtrack/loadmod.py to generate the period lookup table and to learn the file structure. I also used/read:

    - http://www.fileformat.info/format/mod/corion.htm
    
    - http://elektronika.kvalitne.cz/ATMEL/MODplayer3/doc/MOD-FORM.TXT
    
    - https://www.eblong.com/zarf/blorb/mod-spec.txt
    
    - ftp://ftp.modland.com/pub/documents/format_documentation/FireLight%20MOD%20Player%20Tutorial.txt
    
    - And of course, https://github.com/AntonioND/gbt-player

