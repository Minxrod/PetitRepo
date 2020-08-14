# PetitRepo
PetitRepo is a repository for Petit Computer programs and files.

## Formats
Sets of programs and other files (referred to as "projects," akin to later versions of SmileBASIC) are given respective titles, and are available in three formats:

### PTC
Exported versions of the programs and files, given a 36-byte header with important metadata.

### Raw
The format the programs and files are stored in Petit Computer's save file.

### QR
The data of programs and files divided across several QR codes.

## How to Import Files into Petit Computer
There are several ways to import files from the repository into Petit Computer.

### Method 1: PetitImport (3DS, CFW Required)
The easiest way to import files directly into Petit Computer's save file is using PetitImport, a GodMode9 script.
On your PC:
* Make sure you have [the latest version of GodMode9](https://github.com/d0k3/GodMode9/releases/latest).
* Make sure you have [the latest version of PetitImport](https://github.com/HTV04/PTCImport/releases/latest).
* Make sure you have your 3DS's (micro)SD card inserted into your computer, or can transfer files via other means (such as through FTP or microSD management).
* Download the latest offline release of the repository (WIP)
* Navigate to your project of choice, and copy the "raw" folder to the "PetitImport" folder on your 3DS's (micro)SD card. If given a prompt about merging folders, merge them.
* Open GodMode9, and when on the root menu (with the list of mounted drives), press the HOME button.
* Choose "Scripts..."
* Choose "PetitImport."
* If any non-error prompts appear on screen (such as one about making a backup of your save file), press A to continue (if you get an error, [make an issue](https://github.com/HTV04/PTCImport/issues/new/choose) describing the error).
* When on the menu screen, choose "Quick Import."
* A warning will appear on-screen mentioning trusted files. Press A to continue.
* When the process is finished, exit out of the menu, relock permissions, and when you're back on the root menu, press START to reboot.
* Open Petit Computer.
Your imported files should be present!

### Method 2: QR Codes
This method doesn't require a 3DS or CFW, but it takes much, much longer. If you have Petit Computer installed on your 3DS and it has CFW, consider using PetitImport instead.
On your PC:
* On the repository (either online or via the offline package), navigate to your project of choice and open the "qr" folder.
* Open the "qr" folder.
On your DSi/3DS:
* Open Petit Computer.
* WIP
Repeat this process for each file in the "qr" folder:
* On your PC, open the PNG for the file, which contains the QR codes you need to scan.
* On your DSi/3DS, scan each QR code until the file is fully downloaded.
Your imported files should be present!
