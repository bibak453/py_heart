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