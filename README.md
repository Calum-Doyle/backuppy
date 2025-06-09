# BACKUPPY
A simple backup management system

## Description
This program was created to keep track of backups and to aid with the automation of backups. The author is the only intended user of this software, and its main purpose in being written was to practice writing a program with a real-world function.  
This program works by storing pairs of directories for where data to be backed up is held and where it is to be backed up to.  
Groups can be backed up individually or all together.

## Dependencies
- Python  
- Rsync  

## Installation
The program comes packaged with an installer shell script. The script is configured for installing on Linux, so some changes to variables may be required for other systems.

## Usage
Before specifying any backups, a group must first be made by passing `addgroup` as an argument into the program, followed by the name of the group.  
After this, use `iaddtem` followed by the name of the group, the directory to be backed up, and the directory to back up to.

To run a full backup, pass `run` into the program, or to back up just one group, follow this up with `--group` followed by the name of the group.  
To restore backups, do the same as for `run`, but with `restore`.

## To Do
- Implement a notification system
