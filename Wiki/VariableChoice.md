```
*02
IfGte ae 13 08
TimeSetting 13
LoadBG 02
Effect 05
DisplayMessage 01
ChoiceSetup
SetFlag b1 04 # "Walk upstairs."
SetFlag b2 05 # "Walk downstairs."
SetFlag b3 06 # "Leave the school."
SetFlag b4 07 # "Go to the club."
SetFlag b5 08 # "Go home."
SetFlag b6 03 # "Go to the promised place."
SetFlag bd 00
SetFlag be 01
SetFlag bf 02 # "Well, what should I do now?"
SetFlag c0 03 # "Go to the promised place."
SetFlag c1 04 # "Walk upstairs."
SetFlag c2 05 # "Walk downstairs."

IfBitOn 0c 06 03
SetFlag b6 00 # CANT "Go to the promised place."
IfNe 18 00 03
SetFlag b4 00 # CANT "Go to the club."
IfBitOff 05 02 03
SetFlag b4 00 # CANT "Go to the club."

VariableChoice 04 "02" # "Well, what should I do now?"
"03" # "Alright, let's walk upstairs."
"05" # "Alright, let's walk downstairs."
"0f" # "Alright, let's leave the school."
"09" # "Alright, it's club time." / "Alright, let's go to the club." "Alright, let's go hit the club."
"0b" # "Maybe I'll just go home today."
"14" # "Come to think of it, I promised Shihō to go to karaoke." / "She'll nag me if I ditch her later." / "Alright, let's go to karaoke."
End20
```

```
*02
IfGte ae 13 08
TimeSetting 13
LoadBG 02
Effect 05
DisplayMessage 01

ChoiceSetup

SetFlag b1 04 # "Walk upstairs."
SetFlag b2 05 # "Walk downstairs."
SetFlag b3 06 # "Leave the school."
SetFlag b4 07 # "Go to the club."
SetFlag b5 08 # "Go home."
SetFlag b6 03 # "Go to the promised place."

SetFlag bd 00
SetFlag be 01 # "After school."... not one statement
SetFlag bf 02 # "Well, what should I do now?"
SetFlag c0 03 # "Go to the promised place."
SetFlag c1 04 # "Walk upstairs."
SetFlag c2 05 # "Walk downstairs."

IfBitOn 0c 03 03
SetFlag b6 00

IfNe 18 00 03
SetFlag b4 00

VariableChoice 04 "02"
"03" # "Alright, let's walk upstairs."
"05" # "Alright, let's walk downstairs."
"0f" # "Alright, let's leave the school."
"09" # "Yeah, maybe I'll go to Aoi-chan's place."
"0b" # "Maybe I'll just go home for today."
"14" # "Come to think of it, I had promised to go to the arcade with Shiho."
End20
```