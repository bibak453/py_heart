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