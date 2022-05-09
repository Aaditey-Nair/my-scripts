This github repo contains all my scripts. The scripts are written in Python and Bash. Feel free to download any or all of them. Consider creating aliases for the scripts in the .zshrc or .bashrc files

greet.sh
A fun little script which greets you and gives the current user, directory, time, public and private ip address and weather in your city. Change the location variable to your city of choice

todo.py
A CLI based todo app, complete with add, delete, finish and clear features. Run ```python ./todo.py help``` after downloading the script. By default it will create a new todo_file.txt in your user's home directory.

mkflask.sh
Sets up a Flask project. Automatically creates the usual directories and adds some basic code for a minimal setup. Works only on windows. For Mac and Linux, inside the mkflash.sh, change line number 5 to ```source venv/bin/activate```.

mkscript.sh
Automating automation. Creates a shell script with the name you supply as a param, i.e. ```./mkscript.sh <file_name_no_extention>``` and makes it an excecutable. Adds a simple ```echo``` statement and opens it in the nano text editor. By default looks for a zsh shell in ```#!/usr/bin/zsh```.
