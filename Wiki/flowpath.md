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

**05** is the amount of bytes to skip if we pick option A.

**04** is the text block of the second question.


```python
*04
SetTextOffset 06
CharacterDrawSpeed 00
Text "Ｂ、行かない。"           # "B, I won't go."
NewLine
EndTextBlk
```

**00** is the amount of bytes to skip if we pick option B

I think the **Nazo6B** are used either as file padding or Choice Jump Checking. Anyway they are helpful for debugging even if they do nothing.

Implementation:
For this simple choice management I think the best way would be to include the asking question block before the menu statement to invoke specific options. In the menu statement it should always involve jumping to different blocks so that's not a problem.
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
