# fami2mod


Welcome to fami2mod. This is a python script that converts famitracker text exported files into mod files to be used in GBstudio projects.

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
      
     -every note in famitracker will automatically be transposed THREE OCTAVES UP in the mod format. So if you put down a C-3, it will play a C-6. 
      For the first two channels, the sound is not so drastic on the game boy, however one can easily see how troublesome it might be.
      You can easily transpose your notes up and down an octave in OpenMPT by pressing Shift-Control-Q (transpose up) and Shift-Control-A (transpose down). https://wiki.openmpt.org/Manual:_Keyboard_Actions
      
      
      
2. *Exporting to text.* After completing your song in Famitracker, click file>>export text. Enter a name and save this text file outside of your project directory.

3. *Running the script." Next, use Python IDLE to open 
