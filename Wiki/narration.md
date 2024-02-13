# Narration Commands
- **Text**: Display dialogue to the screen.  
  Example: `Text "　よく見れば、やっぱり理緒ちゃんだ。"`

- **Wait**: Halt script flow for a specified amount of time, likely tied to frame count.  
  Example: `Wait 2f`

- **WaitKey**: Pause statement that is skipped when the user clicks on the screen to progress.

- **WaitPage**: Pause statement that is skipped when the user clicks on the screen to progress. After that, it clears the screen. It seems that it also sets a rollback to the end of the page.

- **NewLine**: Move the cursor of the text engine to the start of a new line.

- **EndTextBlk**: Marks the end of the Text block, functioning like a return statement.

- **SayNameD%02x**: Is a function to input the name person that is playing.