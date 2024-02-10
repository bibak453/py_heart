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
End20 probably serves as a return function or end function. Need to check.

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


# Ease of use and steps to reproduce
1. Be rich.
2. Import **To Heart** from Japan or already possess a copy of the game.
3. Proceed only if your copy of the game is legal and it's compatible. This will only work for the release of 1996 for Windows PC.
4. Rip audio files using a CD reaper tool:
* Windows
    -a
    -b
    -c
* Linux
    -a
    -b
    -c
* MacOs
    - I'm sorry I can't really help here and test If I don't have a mac machine. If someone want's to provide steps and software please let me know so I can include it here.
5. Place the audio files under **ASSETS/BGM**
6. If you skip step 4 and 5 then game will not have music.If you want to do this process manually then you need to name the songs from zero to the last number written in hex values. The files should be placed in **game/AUDIO/BGM/**
7. If you missplaced the order of the songs before running the main script then the BGM music will not be accurate to the original (it could play a happy song when there is a tragic flashback). So to prevent that ensure that the list of songs are exactly in the same order as on the cd.
6. Find files: **LVNS3DAT.PAK** and **LVNS3SCN.PAK** and place them into **ASSETS/**

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


-**SCN** and **TXT** labels with the same filename will be places under one file for ease of use.

-Functions name will be as closely to the original, example

-All files decompressed from the **LVNS3DAT.PAK** file will retain it's original naming.

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
*DisplayMessage
*DisplayMessageAndClear
*LoadVisual

*IfBitOff
*IfBitOn
*IfEq
*IfGt
*IfGte
*IfLe
*IfLte
*IfNe

*Jump
*JumpBlk
*Push2D
*Push2F
*Return2D
*Return2F
*SameBlkJump

*LoadBG
*LoadCharacter

*TimeSetting
*DateSettingNoCalendar

Effect

End20
EndFF

FadeBGM

FlagAdd
FlagAdd62
FlagSetBit
FlagSub

GameOver

LoadPCM

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
SetFlag
SetNextBGM
StartBGM
StartEnding
StartPCM
StopPCM
Text        #For some unknown reason this is present in one of the DATA files (00F1, 00F2, 00F3)

TitleDisplay
VariableChoice
WaitForFadeBGM
WaitPCM
WhiteIn
```

# TEXT blocks commands

if a command has **\*** then it means it is explained in this doc.

```
*Text
CharacterDrawSpeed
*WaitKey
*WaitPage
*NewLine
Wait
EndTextBlk

*LoadCharacter
*LoadCharacterC2
*LoadCharacterAndBg
*LoadThreeCharacters
*ChangeCharacter
*ClearAndLoadCharacter
*ClearCharacter

*LoadBG
*LoadBG2
*LoadVisual
*LoadVisualScene
*LoadHVisualScene

*DateSetting

Effect
SpecialEffect
SepiaEffect

Brighten
WhiteIn
WhiteOut

Vibrato

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

SayNameD1
...
SayNameF2

SetTextOffset

StartBGM
PauseBGM
FadeBGM
FadeInBGM
WaitForFadeBGM

StartPCM
LoadPCM
StopPCM
WaitPCM

UnknownOpcode   #TODO: need to investigate 0610.SCN.TEXT, 0793.SCN.TEXT
```

# Calendar Related Commands

# Handling "DateSettingNoCalendar" Command

```c
    case 0x32: /* 日付を設定する */
        dprintf((stderr, "[日付設定(カレンダー無)(%02x)]\n", c[1]));
        if (c[1] == 0xf0) {
            state->flag[TOHEART_FLAG_DATE] = 3; /* 日付初期化 */
        } else {
            state->flag[TOHEART_FLAG_DATE] ++;  /* 一日追加 */
        }       
        state->flag[TOHEART_FLAG_WEEKDAY] = 
            (state->flag[TOHEART_FLAG_DATE] + 5) % 7;
        c+=2;   
        break;
```

This command is used at init of the game with the F0 passed as the parameter. It calculated what day it is. Nice

# Handling "TimeSetting" Command

```c
 case 0x33: /* 時刻を設定する */
        dprintf((stderr, "[時刻設定(%02x)]\n", c[1]));

        /* 行動フラグ初期化。ここで良いのかどうかは不明 */
        state->flag[TOHEART_FLAG_EVENT_DONE] = 0;
        state->flag[TOHEART_FLAG_IDOU] = 0;

        if (c[1] >= 0xf0) {  
            /* 表示無し更新 */
            state->flag[TOHEART_FLAG_TIME] = c[1] - 0xf0;
        } else {  
            /* 表示有り更新 */
            int i;
            int start;
            
            if (state->fast_clock) {
                start = c[1];
            } else {
                start = state->flag[TOHEART_FLAG_TIME];
            }
            
            state->flag[TOHEART_FLAG_TIME] = c[1];
            for (i=start; i<c[1]+1;i++) {
                clock_anim[i].type = LVNS_ANIM_IMAGE_ADD;
            }
            clock_anim[i].type = LVNS_ANIM_NONE;
            LvnsAnimation(lvns, clock_anim + start);
        }

        c += 2;
        break;
```

In this command we set the time of the clock to a specific time.
When the command is invoked it will also show a clock animation from the current point to the end point. We also save the flags because they are relevant.

# Handling "DateSetting" Command

```c
case 0xf5:
        dprintf((stderr, "[日付更新(カレンダー有)(%02x/%02x)]\n", c[1],
                 state->flag[TOHEART_FLAG_DATE]));
		if (!history_mode) {
			int effect_state;
			if (state->fast_calendar) {
				effect_state = 16;
			} else {
				effect_state = 0;
			}

			if (c[1] > state->flag[TOHEART_FLAG_DATE]) {
				state->calendar_day = c[1];
				init_calendar(lvns);
				set_calendar(lvns, state->flag[TOHEART_FLAG_DATE]++, 209);
				set_calendar(lvns, state->flag[TOHEART_FLAG_DATE], 211);
				LvnsAnimation(lvns,  calendar_anim);
				while (!calendar(lvns, &effect_state));
			}
		}
		c += 2;
		break;
```

Here is the same situation. We have some flags set for the current date that it should be and we create an animation with the callendar.

# Narrative Commands

```
Text "　よく見れば、やっぱり理緒ちゃんだ。"
```

The **Text** command is used to display dialogue to the screen.
In renpy the equivalent of say.
We will only need the narrator class as the nvl kind.

The text is enclosed with double quotes.

Together with this command we also use other commands:

```
Wait 2f
```

The **Wait** command is used for halting user interraction for specified ammount. This probably is tied to frame count.

```
WaitKey
```

The **WaitKey** command is used as the user interaction method.
In renpy the say statement already does that funtion.

```
WaitPage
```

The **WaitPage** command is used as the user interaction method that also resets the current screen.
In renpy this would be nvl clear. As it will clear the "page".

```
NewLine
```

The **NewLine** command is used to start at a new line.
Renpy say statement already always start in a new line. This is useful when we want to write multiple lines in one paragraph continuisly.

```
EndTextBlk
```

The **EndTextBlk** command is used to mark the end of the Text block. It works like a return statement.



# Jumping Commands

```
Jump 02 23 01
```

**Jump** is a simple jump statement.
The first two parameters are combined into a text file and the third parameter is the Scene block to execute.
Jump does not return.

**Implementation:**
When parsing this command will be made into a simple jump statement with the correct block to jump to depending on the conditions.

```
JumpBlk 0f
```

**JumpBlk** is a jump statement for jumping to a specific Scene block in the same file.

**Implementation:**
When parsing this command will be made into a simple jump statement with the correct block to jump to depending on the conditions.


```
SameBlkJump 04
```

**SameBlkJump** is a command that will jump to the incremented block. If we are in the block 05 then with the example we will jump to block 9.

**Implementation:**
When parsing this command will be made into a simple jump statement with the correct block to jump to depending on the conditions.

```
DisplayMessage 01
```

**DisplayMessage** is a call statement to the text block of the same filename.
After calling it we return to the previous point of execution.

**Implementation (func.rpy):**
```renpy
label DisplayMessage(txt_blk, clear = False):
    call expression "txt_blk" #TODO: Check syntax

    if clear:
        nvl clear
    return
```

In the place of **DisplayMessage** we'll put this funtion using the call method so we can return to the current context.
As there is also a command that clears the screen after the interaction (DisplayMessageAndClear) we can add a parameter **clear** for this purpose.

```
Push2F 00 3a 02
Push2D 00 20 01
```
**Push2F** and **Push2D** are functions that saves pointers to Scene blocks.

```
Return2F
Return2D
```
**Return2D** and **Return2F** are functions to **Jump** to the saved pointer location.

**Implementation:**
This solution is quite custom so in renpy I will implement a class to hold the specific label that we need to jump to and the Return functions will invoke the jumping method based on what's saved in the pointer class.

# Logic Resolution

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

If an **If** statement turns to be true, then we skip the specified ammount of bytes in the file.

**IfNe** 00 06 01:
- **00** - adress the value resides
- **06** - value to compare to
- **01** - number of bytes to skip

```
IfEq        - if its equal                 x == y  
IfNe        - if its not equal             x != y  
IfGt        - if its greater               x > y   
IfLe        - if its lower                 x < y   
IfGte       - if its greater or equal      x >= y  
IfLte       - if its smaller or equal      x =< y  
IfBitOn     - #TODO
IfBitOff    - #TODO

x = current value | y = second value to compare
```


# Simple Choice resolution

```
Choice 01 02 03 05 04 00
Nazo6B
Jump 01 ae 01
Nazo6B
SetFlag a6 01
FlagAdd 14 00
Jump 01 ad 01
End20
```

In this example this Choice takes 6 parameters:

**01** is the question contained in the Text block.

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

**02** is the number of choices available.

**03** is the text block of the first question.

```python
*03
SetTextOffset 06
CharacterDrawSpeed 00
Text "Ａ、行く。"               # "A, I'll go."
NewLine
EndTextBlk
```

**05** is the ammount of bytes to skip if we pick option A.

**04** is the text block of the second question.


```python
*04
SetTextOffset 06
CharacterDrawSpeed 00
Text "Ｂ、行かない。"           # "B, I won't go."
NewLine
EndTextBlk
```

**00** is the ammount of bytes to skip if we pick option B

I think the **Nazo6B** are used either as file padding or Choice Jump Checking. Anyway they are helpful for debugging even if they do nothing.

# Handling "VariableChoice" Command

(#TODO: Don't know how is this working yet.)

This command resets 12 values:

toheart.c
```c
case 0x2c:
		dprintf((stderr, "[選択肢前位置()]\n"));
        {
            int i;
            LvnsSetSavePoint(lvns, &lvns->selectpoint);
            memcpy(state->flag_select, state->flag, sizeof state->flag);
            for (i=0; i<12; i++)
                state->flag[TOHEART_FLAG_VSELECT_MSG + i] = 0;
        }
        c++;
        break;
```
This is used with the **VariableChoice** command.

# Music Related commands

NOTE:This game uses the CDROM to read song data that is written to the CD.
The legit way would be to rip them from the original CD if you own it.
In a perfect world this is possible, but I think in the end I will create a simple script for aquairing the OST from internet.

# Handling "StartBGM" Command

The **StartBGM** takes one argument that is the number of the song and starts it will full volume without fading in. It loops.

FadeBGM - Fades the song out right after calling it.

WaitForFadeBGM - This function will wait until the song has stopped playing while fading out.

PauseBGM - Pause the BGM without a delay.

you use these free commands together:

```
FadeBGM
WaitForFadeBGM
PauseBGM
```
I will turn it into one function.

FadeInBGM - Takes one parameter that is the number of the song. It fades the song up and its looping.

SetNextBgm

In standard the song is always looping.

When chaging the song the current song will stop looping and the next will continue to loop.

# Handling "StartPCM" Command

LoadPCM - Loads the sound into the memory in renpy this is not needed. Takes one parameter

```c
    case 0xa0:		/* PCMスタート? */
        dprintf((stderr, "[A0 PCM読み込み(%02d)]\n", c[1]));
		if (!history_mode)
			LvnsLoadSound(lvns, "TH_VD%02d.P16", c[1]);
        c += 2;
        break;
```

StopPCM
StartPCM
WaitPCM

# Graphic Related Commands

```c
void
LvnsUndispText(Lvns *lvns)
{
	LvnsFlip(lvns, True); // ����Ʊ���Τ����
	lvns->text_mode = False;
	if (lvns->skip) {
		lvns->latitude = 16;
		LvnsDispWindow(lvns);
	} else {
		LvnsLighten(lvns);
	}
}
```

This is called when wanting to show the characters. Basically a nvl hide window command

```
LoadCharacter 02 04 03
```

**LoadCharacter** is used to load a specific sprite onto 1 of 3 positions.

The first parameter is the position. 0 is left, 1 is center, 2 is right.

The file number is generated by shifting the second parameter by 8 bits to the left and performing a bitwise OR operation with the third parameter.
For character sprites we use "C" at the start of the file (C0A24.png).

If the resulted number is 0xFFFF then we clear the sprite on that position and return.

There is a special case for Akari sprites:

```c
void
ToHeartLoadCharacter(Lvns *lvns, int no, int pos)
{
    /* ... */
    if ((no >> 8) == 0)
    {
        if ((state->flag[TOHEART_FLAG_AKARI] & 0x01)) {
            no |= 0x80;
        }
        no |= 0x100;
    }
    /* ... */
}
```
Implemantation:
This specific function for loading characters onto the screen needs to be handled along with a class to keep track of what characters are currently displayed. #TODO: Write implementation


NOTE: This action does not hide the nvl window during loading the character. It does not seem to change the character that's already displayed, but this needs further code investigating.

```

```

**ChangeCharacter** takes the same parameters as the **LoadCharacter**, but it appears to also add more inbetween visual effects.

First the nvl windows is hidden. After that we use the LoadCharacter function to change the sprite. After than we show the nvl window. In the previous command we don't hide or show the nvl window.

NOTE: The **LoadCharacterC2** appears to basically the same thing as the **ChangeCharacter** do. This command is invoked only once in the whole game (0530.SCN.TEXT). Need to replace that probably and investigate more.

# Handling "ClearCharacter"

This function hides the character with the specified parameter on the screen 

# Handling "ClearAndLoadCharacter"

```c
    case 0xc3:
		dprintf((stderr, "[全消去後キャラ表示(%s, C%02x%02x.LF2)]\n", 
				 posstr[c[1]], c[2], c[3]));
		if (!history_mode) {
			LvnsUndispText(lvns);
			ToHeartClearCharacter(lvns, 3);
			ToHeartLoadCharacter(lvns, c[2]<<8|c[3], c[1]);
			LvnsDisp(lvns, LVNS_EFFECT_FADE_MASK);
		}
		c += 4;
        break;
```

Here we do basically the same thing as Load Character but with calling the ClearCharacter with parameter 3 so it will wipe any additional characters present. I guess it's only used when only one character needs to be in focus after a group or even changing position of the character.

# Handling "LoadCharacterAndBg"

```c
    case 0xc4:		/* 背景付き画面ロード */
		dprintf((stderr, 
				 "[背景付きキャラ変更(%s, C%02x%02x.LF2, S%02d?.LF2, %02x, %02x)]\n",
				 posstr[c[1]], c[2], c[3], c[4], c[5], c[6]));
		if (!history_mode) {
			LvnsUndispText(lvns);
			LvnsClear(lvns, text_effect(c[5]));
			ToHeartLoadBG(lvns, c[4]);
			ToHeartLoadCharacter(lvns, c[2]<<8|c[3], c[1]);
			LvnsDisp(lvns, text_effect(c[6]));
		}
		c += 7;
        break;
```

Here is almost the same story - We hide the nvl window we call a new scene and we display a character while also clearing the previous data - but with some text_effects that I didn't study yet. I will replicate it by looking at it visually rather than looking trhough the xlvns code base.
#TODO: implement text_effects if needed

In renpy when calling for a new scene we don't have to clear the sprites manually because they will just dissapear.
#TODO: To renpy implementation add the reset of the Character Positioning system config so it works like in the original.

This command takes a lot of parameters so let's break it down:

```
LoadCharacterAndBg  02      1e      09      14      0b      00
c[0]                c[1]    c[2]    c[3]    c[4]    c[5]    c[6]
```

```c
...
		if (!history_mode) {
			LvnsUndispText(lvns);                           
			LvnsClear(lvns, text_effect(c[5]));             // 0B
			ToHeartLoadBG(lvns, c[4]);                      // 14 
			ToHeartLoadCharacter(lvns, c[2]<<8|c[3], c[1]); // (1E<<8) | 02
			LvnsDisp(lvns, text_effect(c[6]));              // 00
		}
...
```

It seem's that this will be quite complex function depending on what animations are set. Probably the text_effect are the transitions. Not completly sure.

# Handling "LoadThreeCharacters" command

```
LoadThreeCharacters 00      1c      01      02      ff      ff      01      ff      ff
c[0]                c[1]    c[2]    c[3]    c[4]    c[5]    c[6]    c[7]    c[8]    c[9]
```

This also is a long command, but let's break it down:

```c
    case 0xc6:  /* 3枚ロード */
		dprintf((stderr, "3キャラ同時表示\n"));
		LvnsUndispText(lvns);
		if (!history_mode) {
			ToHeartLoadCharacter(lvns, c[2]<<8|c[3], c[1]); // 1C << 8 | 01 00
			ToHeartLoadCharacter(lvns, c[5]<<8|c[6], c[4]); // FF << 8 | FF 02
			ToHeartLoadCharacter(lvns, c[8]<<8|c[9], c[7]); // FF << 8 | FF 01
			LvnsDisp(lvns, LVNS_EFFECT_FADE_MASK);
		}
		c += 10;
        break;
```

Hides the nvl window and displays each character with the parameters one after another. Could also be 3 separate show screens. #TODO: Check how it works in the game.

# Handling "LoadBG" and "LoadBg2"

```
LoadBG 01
Effect 05
Nazo23 1e
```

LoadBG I think prepares an image to be loaded and using the Effect Command we apply a transition.
And again the Nazo23 a new finding - it also does nothing. At least that's what the xlvns says. I think it provides timing for the effect function. #TODO: Look into it for most part it takes value like 0x1e(30), 0x32(50), 0x64(100), 0xc8(200),  I assume thats frame time.

```c
    case 0xbd:		/* 背景ロードその2 */
		dprintf((stderr, "[背景ロード2 (%d/%d, %02x, %02x)]\n",
				 c[1]/50, c[1]%50, c[2], c[3]));
		if (!history_mode) {
			LvnsUndispText(lvns);
			LvnsClear(lvns, text_effect(c[2]));
			ToHeartLoadBG(lvns, c[1]);
			LvnsDisp(lvns, text_effect(c[3]));
		}
		c += 4;
        break;
```
Here is the code for handling the "LoadBg2". It seems they compressed 3 commands into one. Which is clever.

So we fade the nvl windows use an effect on the screen that is a transition then then load the BG into memory and transout with the specified transition. I guess the standard way would be to just fade to black with transitions. #TODO: need to check for behavior in game.


# Handling "LoadVisualScene" and "LoadHVisualScene" Command

This command takes one parameter that is the number of the visual in hex.

```c
void
ToHeartLoadVisual(Lvns *lvns, int no)
{
    ToHeartState *state = (ToHeartState *)lvns->system_state;
    lvns->bg_type = LVNS_VISUAL;
    lvns->bg_no   = no;
    if (no == 0) {
        lvnsimage_clear(lvns->background);
    } else {
        /* あかりの髪型処理… */
        if ((no == 0x11 || no == 0x13) && 
            (state->flag[TOHEART_FLAG_AKARI] & 0x01)) {
            no = 0x12;
        }
        /* レミィパンティ */
        if (no == 0x80) {
        }
        LvnsLoadBackground(lvns, "V%02x.LF2", no);
    }
    ToHeartClearCharacter(lvns, 3);
}
```
This code checks for special condition (Akari hair change) and calls the ClearCharacter function with the parameter 3 (to get read of every character). In renpy not necessary as calling a new scene will always clear the characters and other sprites.

**Implementation:**

```renpy
label LoadVisual(visual_type = True, num='00'):
    if visual_type:
        scene expression "V[num].png"
        with blinds
    else
        scene expression "H[num].png"
        with blinds

    return
```