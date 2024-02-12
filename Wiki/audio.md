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