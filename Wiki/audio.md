# BGM

`StartBGM 01`: Starts playing a song without a FadeIn or FadeOut. The song will loop automatically. The parameter provided is the number of the song.

`FadeBGM`: Immediately fades out the currently playing song. The FadeIn and FadeOut time is set by default.

`WaitForFadeBGM`: Blocks any interaction while the song is fading out.

`PauseBGM`: Stops the background music (BGM) without a delay. Resuming the song is not supported in the game.

`FadeBGM`, `WaitForFadeBGM`, `PauseBGM`: These functions are used together to FadeOut the current song and block user interaction until the fade-out is complete.

`FadeInBGM 01`: Plays the song with a FadeIn and FadeOut effect.

`SetNextBGM 01`: Sets the next song on the second position. If a song is already playing and another one is added, the current song stops looping, and the new song starts looping.

## Implementation

A custom class will be created for managing song playing, containing references to two files. The first file, if present, is supposed to be looping. If a second file is added while the first is still playing, the first one stops looping on end of the song, and the second one starts looping taking place in the first one.

# PCM

`LoadPCM`: Saves the filename into memory for the song to be loaded. It also stops any currently playing sound.

`StartPCM 01 00`: Starts the saved sound effect. The first parameter specifies the looping count. When set to zero, the sound loops indefinitely. If set to any other value, it repeats x times. The second parameter seems irrelevant.

`StopPCM`: Stops the sound. This command is relevant when the repeat count was not specified.

`WaitPCM`: Waits until the sound stops playing. Only relevant when the repeat count was provided, as when the sound is set on loop, this will wait indefinitely.

## Implementation

In Ren'Py, a class will be implemented for controlling and playing sound effects based on these commands.
