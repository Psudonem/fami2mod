# modmaker II
# with GUIDENCE from https://github.com/NardJ/ModTrack-for-Python/blob/master/modtrack/loadmod.py


import sys 


if(len(sys.argv)>1):
    filename = sys.argv[1]
else:
    filename="template.txt"

# the comments here are unfinished, but I DID really want this program to become availible to others.
# psudo 8/9/2020


















f = open(filename, "r")

file = f.read()
f.close()

f= file.split("\n")

# first order of biddness - open the damn thing.
# we open the text file and store it in the f variable



out = bytearray()
for i in range(0,7000):
    out.extend(b"\0")

# next we create an empty array that's 7228 bytes long. I chose
# we'll use this to store data into. if we go over that, we'll deal with it later!!! :sparkles:



# SIGNAL TO PLAYER THAT THIS IS
# A 4 CHANNEL SONG
out[1080]=ord('M')
out[1081]=ord('.')
out[1082]=ord('K')
out[1083]=ord('.')



# ooh now THIS part is vital! The M.K. tells the GBT that we're operating in protracker mode
# AKA... 4 tracks!











# this next part tells the program the order the patterns are gonna play in.
# As of August 8, 2020, there is no reordering of patterns
# this means that
#       first there's pattern 1
#       then comes pattern 2
#       then comes pattern 3
#       then comes pattern 4
#       then comes pattern 5
#       ETC!!!

# in famitracker, this translates to your pattern screen looking something like this:
#   00 | 00 00  00  00  00
#   01 | 01 01  01  01  01
#   02 | 02 02  02  02  02
#   03 | 03 03  03  03  03
#    . |  .  .   .   .   .
#    . |  .  .   .   .   .
#    . |  .  .   .   .   .
#          ETC!!!






# to accOMplish this goal, we gotta find the line in the FAMTIRACKER text file.

# those lines starts with the words "ORDER "!

# we will find these lines....
# store them in the orders array
# and then grab the largest number from the last entry!

orders=[] # that's the array! :0

for x in range(0,len(f)):
    if("ORDER " in f[x]):
        orders.append(f[x]) # storing the ORDERS in the ARRAY 0.0


songsize = orders[len(orders)-1][6:8] # grabbing the last entry... but there's a problem !!!!
                                      # the songsize is still a string.. we can't do shit with that.


                                 #                                 .
                                 #
                                 #                            .
                                 #                                .
                                 #                             .
songsize = int("0x"+songsize,16) #      integer IS NOW a string \o/
                                 #                               |
                                 #                              / \ let's fuckin gooooooooooooooooooooooooooooooooooo



pattern_order_address = 952     # position 952 is where the pattern order information starts! :eyes:
                                




#                               Now we are actually going to write this pattern order information into the modfile

for x in range(1, songsize+2):      # this basically generates numbers 1-songlength
    out[pattern_order_address]=x    # literally writes the number to that position
    pattern_order_address+=1        # go to the next position







#                                   -  -==-
# now this next part gets into the > >>MEAT<< < of the operation
#                                      -==-  -






# this is the nintendo power guidebook of the program, the lookup table!
# basically ~ instead of NOTES signalling pitch changes,
#             the mod format, and GBT by extension, utilize PERIODS!
#             periods are the word of god.


lookup  =[
    ['C-0',1712],['C#0',1616],
    ['D-0',1525],['D#0',1440],
    ['E-0',1357],['F-0',1281],
    ['F#0',1209],['G-0',1141],  # 0 G!!!!
    ['G#0',1077],['A-0',1017],
    ['A#0',961],['B-0',907],
    ['C-1',856],['C#1',808],
    ['D-1',762],['D#1',720],
    ['E-1',678],['F-1',640],
    ['F#1',604],['G-1',570],
    ['G#1',538],['A-1',508],
    ['A#1',480],['B-1',453],
    ['C-2',428],['C#2',404],
    ['D-2',381],['D#2',360],
    ['E-2',339],['F-2',320],
    ['F#2',302],['G-2',285],
    ['G#2',269],['A-2',254],
    ['A#2',240],['B-2',226],
    ['C-3',214],['C#3',202],
    ['D-3',190],['D#3',180],
    ['E-3',170],['F-3',160],
    ['F#3',151],['G-3',143],
    ['G#3',135],['A-3',127],
    ['A#3',120],['B-3',113],
    ['C-4',107],['C#4',101],
    ['D-4',95],['D#4',90],
    ['E-4',85],['F-4',80],
    ['F#4',76],['G-4',71],
    ['G#4',67],['A-4',64],
    ['A#4',60],['B-4',57]]


def findNoteStringbyPeriod(p):
    for x in range(len(lookup)):
        if(p == lookup[x][1]):
            return lookup[x][0]

def findNotePeriodbyString(s):
    for x in range(len(lookup)):
        if(s == lookup[x][0]):
            return lookup[x][1]
    return 0

# because computers are theStupid.exe,
# we need to teach this bwah a lesson...
# basically we have two functions
#   -one takes a note string ("G-3") and converts it to a period value (143)
#   -one finds the period value (143) and converts it to a note string ("G-3")



# 



# This turns an INTEGER into a 12 bit binary value.
# Parts of the data such as the period value and effect information are stored in 12 bit chunks.

def makePeriod12bitsFromInt(period):
    b=bin(period)[2:] #get the binary version of the period int 
    zeroes=12-len(b)
    b=("0"*zeroes)+b #pad with zeroes
    return b





def makeVolume12bitsFromString(s):
    # where s is a string in range
    try:
        newVolume=bin(int("0x"+s,16)*4)[2:] # this line turns the single byte volume information into
                                            # the volume effect that GBT reads by
                                            # 1. taking that number as a string
                                            # 2. interpreting it as a hex value and turning it an int
                                            # 3. multiplying the int by 4 (so that the volume data can
                                            #    be within GBT's 0x0-0x40 (or 0-64) volume range
                                            # 4. turing that new number into a binary value and
                                            #    shaving off that pesky "0b" at the beginning
                                            #    of the string
        zeroes=8-len(newVolume)
        
        b="1100"+("0"*zeroes)+newVolume #pad with zeroes
        
    except:
        
        b="000000000000"    
    return b

def makeInstrumentNumberFromString(n):   # turns the HEX instrument number into 2 nybbles of data
    # where n is a string "00"-"FF"
    try:
        n=int("0x"+n,16)+1
        n=hex(n)[2:]
        if(len(n)==1):
            n="0"+n
        upper = bin(int("0x"+n[0],16))[2:]
        zeroes=4-len(upper)
        upper =("0"*zeroes)+upper
        
        lower = bin(int("0x"+n[1],16))[2:]
        zeroes=4-len(lower)
        lower =("0"*zeroes)+lower
    except:
        upper='0000'
        lower='0000'
    return upper, lower




start=f.index('PATTERN 00') #find w

x=2108
y=0
for i in range(0,1):#4
    for z in range(start, len(f)):
        #print(f[z])
        if('ROW ' in f[z]):
            y+=1
            line = (f[z])
            line = line.split(" : ")[1:]



            # first channel
            periodBits = makePeriod12bitsFromInt(findNotePeriodbyString(line[0][:3]))
            upper,lower = makeInstrumentNumberFromString(line[0][4:6])
            volumeEffectBits = makeVolume12bitsFromString(line[0][7:8])
            chan1_4bytes = upper+periodBits+lower+volumeEffectBits
            
            chan1_byte1 = int("0b"+chan1_4bytes[:8],2)
            chan1_byte2 = int("0b"+chan1_4bytes[8:16],2)
            chan1_byte3 = int("0b"+chan1_4bytes[16:24],2)
            chan1_byte4 = int("0b"+chan1_4bytes[24:32],2)

            out[x] = chan1_byte1;x+=1
            out[x] = chan1_byte2;x+=1
            out[x] = chan1_byte3;x+=1
            out[x] = chan1_byte4;x+=1

            out.append(0)
            out.append(0)
            out.append(0)
            out.append(0)
            
            
            # second channel
            periodBits = makePeriod12bitsFromInt(findNotePeriodbyString(line[1][:3]))
            upper,lower = makeInstrumentNumberFromString(line[1][4:6])
            volumeEffectBits = makeVolume12bitsFromString(line[1][7:8])
            chan2_4bytes = upper+periodBits+lower+volumeEffectBits
            
            chan2_byte1 = int("0b"+chan2_4bytes[:8],2)
            chan2_byte2 = int("0b"+chan2_4bytes[8:16],2)
            chan2_byte3 = int("0b"+chan2_4bytes[16:24],2)
            chan2_byte4 = int("0b"+chan2_4bytes[24:32],2)

            out[x] = chan2_byte1;x+=1
            out[x] = chan2_byte2;x+=1
            out[x] = chan2_byte3;x+=1
            out[x] = chan2_byte4;x+=1
            

            

            out.append(0)
            out.append(0)
            out.append(0)
            out.append(0)
            
            
            # third channel
            periodBits = makePeriod12bitsFromInt(findNotePeriodbyString(line[2][:3]))
            upper,lower = makeInstrumentNumberFromString(line[2][4:6])
            volumeEffectBits = makeVolume12bitsFromString(line[2][7:8])
            chan2_4bytes = upper+periodBits+lower+volumeEffectBits
            
            chan2_byte1 = int("0b"+chan2_4bytes[:8],2)
            chan2_byte2 = int("0b"+chan2_4bytes[8:16],2)
            chan2_byte3 = int("0b"+chan2_4bytes[16:24],2)
            chan2_byte4 = int("0b"+chan2_4bytes[24:32],2)

            out[x] = chan2_byte1;x+=1
            out[x] = chan2_byte2;x+=1
            out[x] = chan2_byte3;x+=1
            out[x] = chan2_byte4;x+=1


            

            out.append(0)
            out.append(0)
            out.append(0)
            out.append(0)
            
            
            # fourth channel
            if("... .. . F06" in line[3]):
                chan2_4bytes="00000000000000000000101100000110"
            else:
                periodBits = makePeriod12bitsFromInt(findNotePeriodbyString(line[3][:3]))
                upper,lower = makeInstrumentNumberFromString(line[3][4:6])
                volumeEffectBits = makeVolume12bitsFromString(line[3][7:8])
                chan2_4bytes = upper+periodBits+lower+volumeEffectBits
            
            chan2_byte1 = int("0b"+chan2_4bytes[:8],2)
            chan2_byte2 = int("0b"+chan2_4bytes[8:16],2)
            chan2_byte3 = int("0b"+chan2_4bytes[24:32],2)
            chan2_byte4 = int("0b"+chan2_4bytes[24:32],2)

            out[x] = chan2_byte1;x+=1
            out[x] = chan2_byte2;x+=1
            out[x] = chan2_byte3;x+=1
            out[x] = chan2_byte4;x+=1
        #if(y==64): #only generate one pattern
        #    break #yeah

            
            

#print(x) 
  


# wwww xxxxxxxxxxxx WWWW eeee eeeeeeeee
# wwwwWWWW- upper and lower bits of sample number
# xxxxxxxxxxxx -  12 bit note period
# eeee eeee eeee - effect command (letter and numbers in 4 bit segments)


p=0










z= open((filename+'.mod'), 'w+b')
z.write(out)
z.close()
















