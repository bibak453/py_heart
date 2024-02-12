### HollowLeaf presents: TO HEART "Parser thingy"

Hello.

This project aims to completely understand how does the **To Heart** game functions and try to build a modern version on top of Ren'py Visual Novel Engine.

If I don't finish this project you may use what you find here to continue the journey. This will also serve as a sort of wikipedia on how does every function should be implemented based on the original game.

For understanding how the game is implemented I am using an open source implementation for linux operating systems called [xlvns](https://github.com/catmirrors/xlvns).

It is designed for 3 games in mind - kizuato, shizuku and to heart.
The project If my research is right was called LeafBSD. 

This codebase provides a lot to this project as I don't actually have to play the game while reading the scenario files to understand what is happening. 

This obviously doesn't help me with more sophisticated systems (I am looking at you VariableChoice Command) that I still don't really understand, but I'll be fine. Probably.

#TODO: maybe when setting the flags for variablechoice command in the command itself are just filenames to jump to based on what was inserted into the previous flags. so we display whats in the flags and then jump to label with the number...

For decompiling the game script I am using [this](https://github.com/Her-Saki/toheart-tools).

The person that maintains this repo is also translating the game. You can check the progress [here](https://discord.gg/G9nd22F).

My project focuses on machine translation and other (un)necessary functions that I will probably (not) implement:
* AI generated voice acting rather than ripping audio from the PSE edition - as the second point says we need a function to determine who is speaking to even attempt on generating AI voices, but if we flag properly every say statement then by providing voice samples and some prompts on how does the voice should sound like (by emotion I mean) then it could be a nice addition.
* Non nvl mode for whatever reason purely based on logic by looking at what character was currently displayed on the screen. Very stupid idea. This would require additional parsing logic for inserting statements into the original script. It could be done, but for now I want to go with the path of least resistance so I can enjoy talking with 2D girls on my 4:3 LCD. Look at point 1.
* A mash-up of the original with the PSE edition just for fun. They say that the PSE edition contains some better story telling and better expanded scenario or whatever else, so it would be nice to create such an abomination.
* Implementing the mini games that I don't even know what they are... Nevermind, this won't happen anyway.

If quality matters to you I advise to wait for Saki's translation to finish.

It will be 200% better than machine translated. If I still have time in the future I'll support his translation into this project. Something like "English, but better" option in the options menu with a huge credit.

For the graphic and sfx assets I am using [this](https://github.com/vn-tools/arc_unpacker).

This tool is so useful for a lot of visual projects. I recommend it will all my heart even if its not actively developed right now.

The BGM is kinda complicated because the songs are embedded onto the disk itself. For this solution we will need to rip the audio track from the original CD.

If I find a cross-platform solution that could be run from python (or at least provide support for 3 operating systems with various cd riper software) then this process will also be automated.
That's the plan.

In the ideal future any dependency will be added or preferably coded into the main script in this repository so the user would just need to download it and run it.

The plan includes to have a gpt4all model of sorts that's comfortable to run on a low end machine (under 4GB of RAM).
The entire purpose of this project is to ship an automatic solution for a nice machine translation project. I believe with some proper prompting, we can create somehow accurate translation that would not stick out that bad, but I'd still recommend to wait for a human translation.

If the To Heart turns to be a success by my standards I will maybe try the same with Kizuato and Shizuku. They run on (almost) same engine so I don't think it will be difficult to accomplish.

# WIKIPEDIA

**Here are some random stuff that don't fit everywhere and don't need to remain here for ever...**

Scenario are split into TEXT files and DATA files.
The DATA files contain the flow of the TEXT files.

EndTextBlk serves as the end of a block. Basically a return command in renpy.

in renpy converted files i think the best way to keep the same scheme would be to use global and local labels.

A global label would hold local labels based on the DATA files.


tohear_op.c - (opdata[]) contains the opening intro. #TODO: analyze

Choices i think work like this:
Choice 22 03 23 00 24 08 25 10
22 is the asking block and we specify how many choices we can have. 3 in this situation
23, 24, 25 are the text blocks that will be the choices. It always a one liner.
I am not sure on what the secondary value is for. (00,08,10)
in toheart.c when calling for a choice there is a SetSavePoint function

After calling Choice there are 3 Nazo6B and with my logic it would probably mean is that each statement after Nazo6B is included in that choice Selection. #TODO: Verify


When multiplying a 8bit value by 8bits will shift it into a 16bit value. Magic.


KNOWN FACTS:
- LvnsEtc.c - in LvnsInitSavePoint the scn and blk is set to 0 and 1 which indicated that the game will start on that specific file and block.
- Nazo6B is used as a marked for where the choice maker should jump based on the choice...
- in 00F2.SCN.DATA it appears that either the programmers cut of a piece of programming or that is a parsing error - an End20 is repeated twice in the same block. Should add a parameter to only accept this code if the next line is empty.

- It appears that akari has a hairstyle change event and only she is evaluated for displaying her character. (toheart_etc.c) The same goes for CG

# Naming convention

```python
sep = "_"
def label_name(t, f, blk):
    return (t + sep + file + sep + blk).upper()

#t="SCN", f=0005, blk=04 => "SCN_0005_04"
#t="TXT", f=00a0, blk=01 => "TXT_00A0_01"
#TODO: Change to original number shifting stuff

def scn_filename(f):
    return ("SCN" + sep + f).upper() + ".rpy"

#f=0012 => "SCN_0012.rpy"
```


**SCN** and **TXT** labels with the same filename will be places under one file for ease of use.

Functions name will be as closely to the original.

All files decompressed from the **LVNS3DAT.PAK** file will retain it's original naming.

#### FOLDER structure:
IMG
* BG  - Background Images
* CG  - Special FullScreen Images
* HV  - HVisuals
* CHR - Character Sprites
* OPD - Op Data
* CLK - Clock Animation
* CAL - Calendar Animation

AUDIO
* BGM - Background Music
* SFX - Special Sound Effects
* VOC - Used eventually for AI voice acting

FONTS
... # font files

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

Handling "DateSettingNoCalendar" Command

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

Handling "TimeSetting" Command

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

Handling "DateSetting" Command

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

These commands are used in the TXT files.

```
Text "　よく見れば、やっぱり理緒ちゃんだ。"
```

The **Text** command is used to display dialogue to the screen.

```
Wait 2f
```

The **Wait** command is used for halting script flow for specified amount. This probably is tied to frame count.

```
WaitKey
```

The **WaitKey** is used as a pause statement that is skipped when the user clicks on the screen to progress.

```
WaitPage
```

The **WaitPage** is used as a pause statement that is skipped when the user clicks on the screen to progress. After that it it will clear the screen.

```
NewLine
```

The **NewLine** will put the cursor of the text engine at the start of the new line.

```
EndTextBlk
```

The **EndTextBlk** command is used to mark the end of the Text block. It works like a return statement.

# Jumping Commands

These commands are used in the SCN files.

```
Jump 02 23 01
```

**Jump** will "jump" to the new specified context without returning.

```
JumpBlk 0f
```

**JumpBlk** will "jump" to a specific SCN block in the file that the command was invoked.

```
SameBlkJump 04
```

**SameBlkJump** will "jump" to a incremented SCN block in the file that the command was invoked. If we are in the block 05 then with the example we will jump to block 9.

```
DisplayMessage 01
```

**DisplayMessage** is a call statement to the TXT block of the same filename. After calling it we return to the previous point of execution.

**Implementation (func.rpy):**
```renpy
label DisplayMessage(txt_blk, clear = False):
    call expression "txt_blk" #TODO: Check syntax

    if clear:
        nvl clear
    return
```

This function will handle both the **DisplayMessage** and the **DisplayMessageAndClear**.

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

Implementation:
For this simple choice management I think the best way would be to include the asking question block before the menu statement to invoke specific options. In the menu statement it should always involve jumping to diffrent blocks so that's not a problem.
The hard part would be to correctly parse all the options. It would appear that most of the times a choice block only contain 1 Text statement. #TODO: Write a testcase for checking if that is true.

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

```
StartBMG 02
```

**StartBGM** starts to play the song without a FadeIn or a FadeOut. The song will loop on auto when invoking this function. The parameter provided is the number of the song.

```
FadeBGM
```

**FadeBGM** will imidietly fade the current playing song. It seems that fading In and Out time is set by default.

```
WaitForFadeBGM
```

**WaitForFadeBGM** will block any interaction while the song is Fading Out. 

```
PauseBGM
```

**PauseBGM** will stop the BGM without a delay. The game does not allow resuming the song.

```
FadeBGM
WaitForFadeBGM
PauseBGM
```
These functions are always used together to FadeOut and block user interaction.

```
FadeInBGM 06
```

**FadeInBGM** will play the song with a FadeIn and FadeOut.

```
SetNextBgm 03
```

**SetNextBgm** is putting a next song into the list. With that in mind if we have one song playing and we add the second one then the first will stop looping and then will play the second one but looping and effectively deleting the fisrt one from the list.

When chaging the song the current song will stop looping and the next will continue to loop.

Implementation:
I will write a custom class for managing the song playing. It will contain two files references. The first one if present it's supposed to be looping. If we add the second file when the song reached the end it will evaluate if it still needs to be loping. If no then we take the second file and put it into the first one, we set the second one to None and with that a new loop starts again with a new song. The Fade Out command will act as a on demand stop function. When the function was called with the FadeIn it will also aply a FadeOut and still be looping.

```python
LoadPCM 05
# Filename = "TH_VD%02d.P16"
```

**LoadPCM** will save the filename into the memory of what song should be loaded. It also stops any sound that is currently playing.

```
StartPCM 01 00
```

**StartPCM** will start the saved sound effect. The provided parameter is the looping count. When the first parameter is zero then the sound is looping. If it's anything else then it repeats x times. The second parameter seems irrelevant.

```
StopPCM
```

This command is relevant when the repeat count was not specified. It will stop the sound.


```
WaitPCM
```

This function will wait until the sound would stop playing. Only relevant when the repeat count was provided as when the sound is set on loop this will wait for infinite ammount of time.

Implementation:
In renpy I will implement a class for controlling and playing sound effects based on these commands.

# Graphic Related Commands

```
LoadCharacter 02 04 03
```

**LoadCharacter** is used to load a character sprite.

This action does not hide the nvl window during loading the character.

The first parameter is the position - 0 is left, 1 is center, 2 is right.

The filename is generated by this expression:

"C" + (( parameter 2 << 8 ) | parameter 3)

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

```
ChangeCharacter 02 04 03
```

**ChangeCharacter** takes the same parameters as the **LoadCharacter**, but it also:
1. Hide the nvl window
2. Use the **LoadCharacter** function effectively changing the displayed character.
3. Shows the nvl window again

NOTE: **LoadCharacterC2** seems to do basically the same thing as the **ChangeCharacter**. It's invoked only once in the whole game (0530.SCN.TEXT).

```
ClearCharacter 03
```

**ClearCharacter** will clear the character on the specified position. If a 3 is passed as a parameter then it will clear every character. It does not affect the nvl window.

```
ClearAndLoadCharacter 01 00 0A
```

In this function:
1. We hide the nvl window
2. We use the ClearCharacter with parameter 3 - clears every character
3. Displays the character with the parameters passed like in the LoadCharacter
4. Shows again the nvl window

```
LoadCharacterAndBg 02 1e 09 14 0b 00
```

In this function:
1. We hide the nvl window
2. We clear the screen (to black) with the fifth parameter
3. We load the BG with the forth parameter
4. We load the character with position as first parameter and the computed file name with second and third parameter
5. We transition to the computed screen with the sixth parameter.

```
LoadThreeCharacters 00 1c 01 02 ff ff 01 ff ff
```

In this function:
1. We hide the nvl window.
2. We load the first character with first parameter as position and second and third to compute the filename.
3. We load the second character with forth parameter as position and fifth and sixth to compute the filename.
4. We load the third character with seventh parameter as position and eight and ninth to compute the filename.
5. All the loading should be done one after another. #TODO: Check
5. We show the nvl window.

"LoadBG" and "LoadBg2"

```c
void
ToHeartLoadBG(Lvns *lvns, int no)
{
    static u_char haikeiflag[] = { 'D', 'E', 'N', 'X', };
    static char name[20] = "S%02dD.LF2";

    lvns->bg_type = LVNS_BACKGROUND;
    lvns->bg_no   = no;

    if (no == 0) {
        lvnsimage_clear(lvns->background);
    } else if (no == 254) {
		char pal[] = {255,255,255};
		lvnsimage_set_palette(lvns->background, pal, 1);
        lvnsimage_clear_index(lvns->background, 0);
    } else {
        name[5] = haikeiflag[no / 50];
        LvnsLoadBackground(lvns, name, no % 50);
    }
    ToHeartClearCharacter(lvns, 3);
}
```

```
LoadBG 02
Effect 05
```
The LoadBG takes one parameter and is accompanied by the Effect Command.

This is probably used to transition to the new BG from the current one without going to black. This set of command can also be found a Nazo23 with some values like:

* 0x1E - 030
* 0x32 - 050
* 0x64 - 100
* 0xC8 - 200

I assume it's used as a non standard transition time. Probably expressed in frame count. #TODO: Check

In this function:
1. We create the filename "S" + parameter in hex + ".LF2"
2. There are two weird statements that I will omit (point 3).
3. on the fifth position of the filename we put a new character based on the haikeiflag[] = { 'D', 'E', 'N', 'X', }; => haikeiflag[no / 50].
4. We call the LvnsLoadBackground (filename, number_from_filename % 50)
5. Then we also call the ClearCharacter with the parameter 3.

Basically we would need to first clear the characters before transitioning to a new location. We don't hide or show the nvl window.

```
LoadBG2 15 00 00
```

This function have a similar actions, but in this function:
1. We hide the nvl window.
2. We clear the screen with effect with parameter 2.
3. We load the bg into the memory with the parameter 1.
4. We use the parameter 3 to transition the bg.

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

IMPORTANT NOTE: I think the LoadBG and LoadBG2 even if they do basically the same they are actually used to load from one bg to black and back to new (LoadBG2) while the LoadBG will not go to black.

The same goes for LoadVisual and LoadVisualScene


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