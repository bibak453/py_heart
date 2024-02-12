## Label Naming Convention

We use two main label types: **SCN** and **TXT**, representing script files within the game.

The `label_name` function constructs label names using the following components:
- `filetype`: Type of the label (e.g., "SCN", "TXT").
- `filename`: Name of the file.
- `block`: Block identifier.

```python
separator = "_"

def label_name(filetype, filename, block):
    return (filetype + separator + filename + separator + block).upper()
```

Both `SCN` and `TXT` labels with the same filename will be placed in the same file.

## File Naming Convention

The `scn_filename` function generates filenames for script files in the format: "SCN_filename.rpy".

```python
def scn_filename(filename):
    return ("SCN" + separator + filename).upper() + ".rpy"
```

## Folder Structure

Our project follows a structured folder hierarchy to organize different types of files:

### img Folder
- **bgs**: Background Images
- **cgs**: Special FullScreen Images
- **hcg**: HVisuals
- **chr**: Character Sprites
- **opd**: Op Data
- **clk**: Clock Animation
- **cal**: Calendar Animation

### snd Folder
- **bgm**: Background Music
- **sfx**: Special Sound Effects
- **voc**: Reserved for future AI voice acting

### fnt Folder
- Contains font files used in the project.

### tl Folder
- Contains translation files.