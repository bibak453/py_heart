Scenario are split into TEXT files and DATA files.
The DATA files contain the flow of the TEXT files.

In the DATA files we are defining scenarios like this:
-- *01
-- DisplayMessage 00
-- DisplayMessage 01
-- DisplayMessage 02
-- ...
-- DisplayMessage 44
-- DisplayMessage 45
-- IfLe 15 2e 04
-- Jump 02 22 01
-- Jump 02 23 01
-- End20

DisplayMessage invoked the text block from the TEXT file.
End20 probably serves as a return function or end funtion. Need to check.

In TEXT files there are TextBlocks that are defined:
-- *00
-- ...
-- ...
-- EndTextBlk

EndTextBlk serves as the end of a block. Basically a return command in renpy.

in renpy converted files i think the best way to keep the same scheme would be to use global and local labels.

A global label would hold local labels based on the DATA files.

---------------------------------------------------------------------------

-- Text "{Message}"
-- WaitKey
-- NewLine

This block will display a text - game doesn't display who is speaking

Example:
-- Text "「わーってるよ！」"
-- WaitKey
-- NewLine

WaitPage - this is probablt the equivelent of nvl clear in renpy - it will display every line until a new page should be shown where it should be cleared.
WaitKey - This probably waits for key input - in renpy this wont be parsed
Wait - this is a function to wait until the specified ammount. in the lvns it probably is tied to gramerate.
NewLine probably is an explicit command to print the characters in a new line and if not added it will print characters in the last cursor position. Need to check.

----------------------------------------------------------------------------------------

-- Text "「ふぅ、ふぅ…。"
-- WaitKey
-- SayNameD8
-- SayNameD9
-- SayNameDA
-- SayNameDB
-- SayNameDC
-- SayNameDD
-- Text "ちゃん、お願いだから、寝坊しないで」"
-- WaitKey

SayNameD{NUMBER} - Probably prints a name
----------------------------------------------------------------------------------------



----------------------------------------------------------------------------------------



----------------------------------------------------------------------------------------



----------------------------------------------------------------------------------------



----------------------------------------------------------------------------------------
BGM specific commands
StartBGM - Play a bgm music
FadeBGM - I assume this would FadeOut the music
FadeInBGM - This is a setting for FadeIn music
PauseBGM - Causes the bgm to stop.
WaitForFadeBGM - Waits until the bgm is Faded (to value 0)
SetNextBGM - When a song is playing and looping it will set the next song to be played also in a loop. That's how I assume it works.

SFX specific commands
LoadPCM - Loads the sound into the memory. With renpy this isn't nedded.
StopPCM - As the name suggest it stops the sound, but I am not sure for what. The sounds are small and don't appear to be looping.
StartPCM - Plays the sound.
WaitPCM - Waits for the sound to complete. This probably is useful for playing specific landmark sounds that shouldnt be skipped.

Renpy Sound Implementation:
-- play music "mozart.ogg" => StartBGM
-- play sound "woof.mp3" => StartPCM
-- stop music fadeout 1.0 => FadeBGM + WaitForFadeBGM + PauseBGM
-- stop sound => StopPCM
-- #TODO: Add renpy specific wait function for music completion. Preferably with a modal screen so the user can't skip interaction.

BGM and SFX will be hardcoded for the purpose of code integrity.

FLAG SYSTEM:

In renpy i will make it into a dictionary where a hex name will have an int value to manipulate

FlagAdd (and FlagAdd62) - Add specified ammount to the selected flag.
FlagSub                 - Substract specified ammount to the selected flag.
SetFlag                 - Sets the flag to the value
FlagSetBit              - #TODO

it seems that if statements are used as multiple check
When an if statement is followed by an if statement then they should be evaluated together (&)
Any command that folows an if statement is the command that should be executed if the statement is true
it doesnt appear to have else statements so after executing the if statement if true then it will go to the next command unless a jump command was used.

#TODO: Jump command is confussing. In most of the times it looks like a simple jump but also like it actually returns like calling a label in renpy


DisplayMessage - this is used as calling a label because we expect to get back to that point of execution. It will return with EndTextBlk
JumpBlk - This command is used to jump inside the DATA file. It will return based on End20.
Jump - is used to jump between DATA files and DATA block. We specify the 2 hex value (0a 87 => filename) and the third is the block to execute. It also returns of End20.
SameBlkJump - thats a very weird jump... It will jump into an incremented scenario in DATA file. So when the current scenario would be 2 and the command has 10 as a parrametter then the jump would go to the 12 block inside the DATA file. Why? But this does not work with some scenario files... Maybe it introduces some shifting in the current block? like adding just jumping a line ahead. It is only used in DATA files so it's confusing. For the most uses that exists it matches the idea of jumping to a scenario block. Only one doesn't match as a scenarion block doesnt exist with the specified number...
#TODO: I will have to create a json tree for explaining every command and path that is possible with the scripts.

Example:
*0a
IfNe ad 06 01
Return2D
IfNe ab 3d 08
IfNe 24 06 04
Jump 07 55 01
IfNe ab 3e 08
IfNe 24 08 04
Jump 07 5a 01
Return2D
End20

#TODO: Nazo messages
Nazo23 0x23
Nazo26 0x26
Nazo27 0x27
Nazo40 0x40
Nazo44 0x44
Nazo50 0x50
Nazo6B 0x6b
Nazo6C 0x6c
Nazo70 0x70
Nazo71 0x71
Nazo72 0x72
Nazo74 0x74
Nazo75 0x75
Nazo76 0x76
Nazo79 0x79
Nazo7A 0x7a
NazoPCMA6 0xa6
NazoPCMA7 0xa7
NazoPCMA8 0xa8
NazoB4 0xb4
NazoB8 0xb8
NazoBA 0xba
NazoBE 0xbe
NazoC7 0xc7
NazoC9 0xc9
NazoCC 0xcc
NazoCF 0xcf
NazoF8 0xf8

tohear_op.c - (opdata[]) contains the opening intro. #TODO: analyze

Choices i think work like this:
Choice 22 03 23 00 24 08 25 10
22 is the asking block and we specify how many choices we can have. 3 in this situation
23, 24, 25 are the text blocks that will be the choices. It always a one liner.
I am not sure on what the secondary value is for. (00,08,10)
in toheart.c when calling for a choice there is a SetSavePoint function

After calling Choice there are 3 Nazo6B and with my logic it would probaly mean is that each statement after Nazo6B is included in that choice Selection. #TODO: Verify

Push2D and Return2D are a very veird way of jumping.
Push2D takes 3 parameters (00 01 03) look at this like 0001.SCN blk 03
This commands saves this to the memory and when the Return 2D is used then it calculates a new position to jump into like this:
ToHeartLoadScenario(lvns, state->flag[TOHEART_FLAG_2D_SCN] * 256 +state->flag[TOHEART_FLAG_2D_SCN+1],state->flag[TOHEART_FLAG_2D_BLK]);
the calculated values in this example would be (scn = 00*256 + 01 | blk 03) Why?
now I know why. Because multiplying a 8bit value by 8bits will shift it into a 16bit value. Magic. Still don't know how Return2D works when Push2D wasn't called at all.

#TODO: Some commands are used in a specific way. Need to analyze each of them

KNOWN FACTS:
- LvnsEtc.c - in LvnsInitSavePoint the scn and blk is set to 0 and 1 which indicated that the game will start on that specific file and block.
- Nazo6B is used as a marked for where the choice maker should jump based on the choice...
- Push2D and Push2F are used to save a specific rollback point so when Return2D or Return2F is called then the program can easily go back to the "savepoint". It is still unknown what should the script do if the the savepoint wasnt specified.
- in 00F2.SCN.DATA it appears that either the programmers cut of a piece of programming or that is a parsing error - an End20 is repeated twice in the same block. Should add a parameter to only accept this code if the next line is empty.
- There are instances of using the Text commands in DATA files where it does not make sense. Also there is Text statement that is normal. (00F1.SCN.DATA - Text "号善店父雷嵐義管浦善謡")
- It appears that akari has a hairstyle change event and only she is evaluated for displaying her character. (toheart_etc.c) The same goes for CG

NEW FILE

##### HollowLeaf presents: TO HEART "Parser thingy"

It is supposed to be a tool for decompiling the original TO HEART files into a .rpy script file for enjoying the game on a modern system without the use of a old Windows machine or a virtual machine with a jappanese local enabled.

Parsing instructions:
1. For the script data to remain as similar to the original all non standard commands will be made into python functions. For example:
- Managing the BGM
- Managing the SFX execution
- Managing the visual particle system (#TODO: There apears to be a sakura leafs particle and rain particles. Need to check.)
- Managing the internal callendar for events execution
- Custom animations (for example clock)
- Managing the BG / CG / HVisuals
- Managing the characters position and expressions
- Managing calling and jumping scenarios - Commands like Jump SameBlkJump DisplayMessage Return2D and Return2F all are acting as a comand that either uses it's own position location or returns to the previous statement. #TODO: need to be careful how to implement this

2. The original script won't be translated as this project wants to focus first on the accesibility feautures of playing the TO HEART game on modern systems without the need to emulate or simulate an old windows system.
- I want to support every game that uses the same scenario formats so it can be a very nice tool for enjoying the Visual Novel Series from Leaf (That would probably mean Shizuki and Kizuato i think both of them are supported by the same scenario scripting langauge #TODO: check)
- The game UI will remain in english for accesibility.
- #TODO: I want to add voice acting in a form of AI generated voices but that would require the user to launch a seperate script. This will be only a secondary solution. The user would need to provide voice samples for specific characters. The main problem in that solution is that the game doesnt explicitly define who is speaking as the whole game runs in nvl mode. That would add a lot of work on my side to ensure adding a landmark function to process the current say statement and play the apropriate sound file only if the speaker is defined as who actually is speaking. This could be done by just analyzing what character sprite is present at the moment and adding such statement, but I will experiment with this idea only when I will have at least a machine translated version of the game.
- In the setting panel I will add a python function to always add a translation switch button based on what folders are present in the 'tl' folder of the game.
- The game itself can only be played when the user has access to a legal copy of the game. By providing to the 'game' folder the apropriate files (LVNS3SCN.PAK and LVNS3DAT.PAK) the game will attempt to decrypt the packages and based on specific intructions of the parser I will build it will create a structured version of the gamme saved in UTF-8 encoding as '.rpy' files.
- The game as intended by the 2. point it will contain the jappannese version as default and no human translation will be provided. But there will be either AI translation service run in python or a use of a python packages that are able to translate jappannese to english. #TODO: When the simple parsing is already inplemented I will need to test for accuracy between diffrent types of translation. I want to avoid using online services as there can be a request limit that would not work the best for the future user.
- The scope of the project would be nice to widen in the future by including the PSE version of the game. This game already possess voice acting so that could help but the main problem would be merging the old script with the new one as the PSE version has new scenarios included and removed the +18 stuff. #TODO: If I ever have time to acomplish more for this project I will create a specific version of this to include the minigames, new scenarios and also merge the old scenarios. I think i could use AI tools for image generation to create additional CG of HVisuals for the characters that are included in the PSE version, but that's really a stretch.

# Naming convention

```python
sep = "_"
def label_name(t, f, blk):
    return (t + sep + file + sep + blk).upper()

#t="SCN", f=0005, blk=04 => "SCN_0005_04"
#t="TXT", f=00a0, blk=01 => "TXT_00A0_01"

def scn_filename(f):
    return ("SCN" + sep + f).upper() + ".rpy"

#f=0012 => "SCN_0012.rpy"
```


-**"SCN"** and **"TXT"** labels with the same filename will be places under one file for ease of use.

-Functions name will be as closely to the original, example

-All files decompressed from the **"LVNS3DAT.PAK"** file will retain it's original naming.

#### FOLDER structure:
IMG
* BG  - Used for all Background images
* CG  - Used for all special full screen images
* HV  - Used for all HVisuals
* CHR - Used for all character sprites
* OPD - Used for the opening scenario
* CLK - Used for the clock animation
* CAL - used for the callendar animation

AUDIO
* BGM - Used for all background music #TODO: Needs to be ripped from the CD with python
* SFX - Used for all special sound effects
* VOC - Used eventually for AI voice acting

FONTS



# DATA blocks commands

If a command has **\*** then it means it is explained in this doc.

```
*Choice
*ChoiceSetup
DateSettingNoCalendar
*DisplayMessage
*DisplayMessageAndClear
Effect
End20
EndFF
FadeBGM
FlagAdd
FlagAdd62
FlagSetBit
FlagSub
GameOver
*IfBitOff
*IfBitOn
*IfEq
*IfGt
*IfGte
*IfLe
*IfLte
*IfNe
Jump
JumpBlk
LoadBG
LoadCharacter
LoadPCM
LoadVisual
Nazo23
Nazo26
Nazo40
Nazo44
*Nazo6B
Nazo6C
Nazo70
Nazo79
Nazo7A
NazoPCMA6
PauseBGM
*Push2D
*Push2F
*Return2D
*Return2F
SameBlkJump
SetFlag
SetNextBGM
StartBGM
StartEnding
StartPCM
StopPCM
Text        #For some unknown reason this is present in one of the DATA files (00F1, 00F2, 00F3)
TimeSetting
TitleDisplay
VariableChoice
WaitForFadeBGM
WaitPCM
WhiteIn
```

# TEXT blocks commands

if a command has **\*** then it means it is explained in this doc.

```
Brighten
ChangeCharacter
CharacterDrawSpeed
ClearAndLoadCharacter
ClearCharacter
DateSetting
Effect
EndTextBlk
FadeBGM
FadeInBGM
LoadBG
LoadBG2
LoadCharacter
LoadCharacterAndBg
LoadCharacterC2
LoadHVisualScene
LoadPCM
LoadThreeCharacters
LoadVisual
LoadVisualScene
Nazo40
Nazo44
Nazo70
Nazo71
Nazo72
Nazo74
Nazo75
Nazo76
Nazo79
Nazo7A
NazoB4
NazoB8
NazoBA
NazoBE
NazoC7
NazoC9
NazoCC
NazoCF
NazoF8
NazoPCMA6
NazoPCMA7
NazoPCMA8
NewLine
PauseBGM
SayNameD1
SayNameD2
SayNameD3
SayNameD4
SayNameD5
SayNameD6
SayNameD8
SayNameD9
SayNameDA
SayNameDB
SayNameDC
SayNameDD
SayNameDF
SayNameE0
SayNameE1
SayNameE2
SayNameE3
SayNameE4
SayNameE6
SayNameE7
SayNameE8
SayNameE9
SayNameEA
SayNameEB
SayNameED
SayNameEE
SayNameEF
SayNameF0
SayNameF1
SayNameF2
SepiaEffect
SetTextOffset
SpecialEffect
StartBGM
StartPCM
StopPCM
Text
UnknownOpcode   # TODO: need to investigate 0610.SCN.TEXT, 0793.SCN.TEXT
Vibrato
Wait
WaitForFadeBGM
WaitKey
WaitPCM
WaitPage
WhiteIn
WhiteOut
```

# Handling "Push2F", "Push2D", "Return2F" and "Return2D"

The "Push" part of these commands are basically a dynamic jumping solution:

003A.SCN.DATA
```
*00
Push2F 00 3a 02
IfNe a6 01 04
Jump 00 20 01
Push2D 00 20 01
Jump 00 a4 01
End20
```

In this SCN block we basically save:

```
2F: "003A.SCN.DATA" SCN_BLK "02"
2D: "0020.SCN.DATA" SCN_BLK "01"
```

And when **Return2D** or **Return2F** are used they will jump back to the place of memory.

This commands is only permited in the DATA files.

# Handling "If" statements

If an **"If"** statement turns to be true, then we skip the specified ammount of bytes in the file.

**IfNe** 00 06 01:
- **00** - adress the value resides
- **06** - value to compare to
- **01** - number of bytes to skip

Example:
```
*0a
IfNe ad 06 01   # if true---
Return2D                   |
IfNe ab 3d 08           <--- # if true---
IfNe 24 06 04                            |
Jump 07 55 01                            |
IfNe ab 3e 08                         <---# if true---
IfNe 24 08 04                                         |
Jump 07 5a 01                                         |
Return2D                    <-------------------------
End20
```


```
x = current value | y = second value to compare
IfEq        - if its equal                 x == y  
IfNe        - if its not equal             x != y  
IfGt        - if its greater               x > y   
IfLe        - if its lower                 x < y   
IfGte       - if its greater or equal      x >= y  
IfLte       - if its smaller or equal      x =< y  
IfBitOn     - #TODO
IfBitOff    - #TODO
```

# Handling "DisplayMessage" Command

**"DisplayMessage"** Command is basically calling the text and expecting to return to the previous point of execution.

RENPY IMPLEMENTATION (func.rpy):
```renpy
label DisplayMessage(txt_blk, clear = False):
    call expression "txt_blk"

    if clear:
        nvl clear
    return
```

The **"clear"** boolean is for handling **"DisplayMessageAndClear"** command.
When clear is True then we clear the screen after returning from the **"txt_blk"**.


```renpy
label SCN_0005_DAT_01: 
    call DisplayMessage("SCN_0005_TXT_01")
```


```
*01
DisplayMessage 00
DisplayMessage 01
DisplayMessage 02
...
DisplayMessage 3e
DisplayMessage 3f
DisplayMessage 40
Return2D
End20
```

# Handling "Choice" Command

02C8.SCN.DATA
```
Choice 01 02 02 05 03 00
Nazo6B
Jump 01 ae 01
Nazo6B
SetFlag a6 01
FlagAdd 14 00
Jump 01 ad 01
End20
```

In this example this Choice takes 6 parameters:

Choice **01** 02 02 05 03 00 | is used as displaying the leading txt_blk containing the question for the choice.

02C8.SCN.TEXT
```python
*01
Text "「……」"
WaitKey
...
Text "…えっ、部室に来て欲しいって？"             # "...Huh, you want me to come to the club room?"
WaitKey
Text "　うーん、そうだなあ──」"                 # "Hmm, let's see..."
NewLine
EndTextBlk
```

Choice 01 **02** 02 05 03 00 | is declaring how many choices we have

Choice 01 02 **02** 05 03 00 | is pointing at the first choice expressed with a txt_block.

02C8.SCN.TEXT

```python
*02
SetTextOffset 06
CharacterDrawSpeed 00
Text "Ａ、行く。"               # "A, I'll go."
NewLine
EndTextBlk
```

Choice 01 02 02 **05** 03 00 | is probably (#TODO: CHECK!!!) a count of many bytes we need to skip in the script. In this case:

02C8.SCN.DATA

```
Choice 01 02 02 05 03 00-----------
Nazo6B                            |
Jump 01 ae 01                     |
Nazo6B  <--------------------------
SetFlag a6 01
FlagAdd 14 00
Jump 01 ad 01
End20
```

We skip 5 bytes to the second **Nazo6B**. It is still unclear what is this command, but for now I will assume it's for error checking (#TODO: CHECK).

Choice 01 02 02 05 **03** 00 | is pointing at the second choice expressed with a txt_block.

02C8.SCN.TEXT

```python
*03
SetTextOffset 06
CharacterDrawSpeed 00
Text "Ｂ、行かない。"           # "B, I won't go."
NewLine
EndTextBlk
```

Choice 01 02 02 05 03 **00** | is probably (#TODO: CHECK!!!) a count of many bytes we need to skip in the script. In this case:

```
Choice 01 02 02 05 03 00-----------
Nazo6B             <---------------
Jump 01 ae 01
Nazo6B
SetFlag a6 01
FlagAdd 14 00
Jump 01 ad 01
End20
```

We skip 0 bytes to the first **Nazo6B**.

# Handling "VariableChoice" Command

# Handling "ChoiceSetup" Command