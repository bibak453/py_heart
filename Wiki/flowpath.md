## Jumping Commands

These commands are utilized in SCN files to navigate through the game's script:

- **Jump**: This command directs the script to a specified point without returning.
  - Example: `Jump 02 23 01`

- **JumpBlk**: Jumps to a specific SCN block within the file where the command is invoked.
  - Example: `JumpBlk 0f`

- **SameBlkJump**: Jumps to an incremented SCN block in the file where the command is invoked. For instance, if we are in block 05, then this command jumps to block 9.
  - Example: `SameBlkJump 04`

- **DisplayMessage**: Calls a statement from the TXT block of the same filename, then returns to the previous execution point.
  - Example: `DisplayMessage 01`

- **Push2F** and **Push2D**: Functions that save pointers to SCN blocks.
  - Example: `Push2F 00 3a 02`, `Push2D 00 20 01`

- **Return2F** and **Return2D**: Functions to jump to the saved pointer location.
  - Example: `Return2F`, `Return2D`

## Logic Resolution

In the script logic, **If** statements determine whether to skip a specified number of bytes if true.
In the script logic, **If** statements enable conditional branching based on various comparisons:

- `IfEq`: Skips bytes if equal to a specified value.
- `IfNe`: Skips bytes if not equal to a specified value.
- `IfGt`: Skips bytes if greater than a specified value.
- `IfLe`: Skips bytes if less than or equal to a specified value.
- `IfGte`: Skips bytes if greater than or equal to a specified value.
- `IfLte`: Skips bytes if less than or equal to a specified value.
- `IfBitOn`: Skips bytes if a bit is set to "on" in the specified value.
- `IfBitOff`: Skips bytes if a bit is set to "off" in the specified value.

```
*0a
IfNe ad 06 01   <--- # if true
Return2D                    |
IfNe ab 3d 08   <--- # if true
IfNe 24 06 04               |
Jump 07 55 01               |
IfNe ab 3e 08   <---# if true
IfNe 24 08 04               |
Jump 07 5a 01               |
Return2D        <------------
End20
```

## Simple Choice Resolution

The `Choice` command facilitates simple choices in the game script.

- It presents a question and options, each associated with a block of text.
- After selecting an option, the script jumps to the corresponding block of text.
- Example:
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

`01` is the asking TXT block

`02` is the number of options

`03` is the question A

`04` is the question B

`05` is the point of jump for question A

`00` us the point of jump for question B


## Handling "VariableChoice" Command

#TODO: Complete this

## Ending the game

`StartEnding 00` seems to just play the ending sequence that is just the same for every scenario. The parameter is useless. It was probably intended to have different endings sequence but it just didn't happen or it's not implemented in the `xlvns`. After each ending we save to the seen flag and when the last person is evaluated then we can access the last ending. I think.

NOTE: I think there is a secret ending sequence because the file where the `StartEnding 01` is it contains congratulations for completing all the routes.

`GameOver` is a useless I would say. It only breaks the loop but it's not usually at the end of the block. After it it's usually the `StartEnding` command. The only exception is in `0072.SCN.DATA`

