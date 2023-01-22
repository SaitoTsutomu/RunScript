## Blender Add-on: RunScript

Execute the specified script file.

## Installation

- Download https://github.com/SaitoTsutomu/RunScript/archive/refs/heads/master.zip
- Start Blender.
- Edit menu -> Preferences
  - Select the "Add-ons" tab.
  - Press the "Install ...".
  - Select the downloaded ZIP file and press the button "Install Add-on".
  - Check the "Object: RunScript".

## Usage

- Show the sidebar and select the Edit tab.
- Specify a file name.
- Press "Run Script".

In Python console, execute as follows to reflect the global variables.

```
execfile = __import__("RunScript-master").execfile
execfile(<file name>, globals())
```
