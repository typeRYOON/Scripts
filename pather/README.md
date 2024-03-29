# Pather : : A Quick Directory Changer
Pather is a command line utility program that quickly cd's the user to a menu specified directory.  
Pather was designed to work on Windows machines, if there's an issue on UNIX machines, please contact me.  

You can add and delete entries easily with simple commands.  
This program has a paging system incase you have many directories added to your pather directory list.  
> Example usage:
> 
> ![](/images/pather/pather-2.jpg)

## Prerequisites
Please make sure you have the following prerequisites:
* Python 3.7+  
* Colorama installed **: : `pip install colorama`**

## Downloading the source code
Clone the repository:
```
git clone https://github.com/typeRYOON/Scripts
cd Scripts
```
> Move the `Pather` folder to where you'd like for the internal program to subsist.  
> I suggest moving it to a folder without heightened permissions as Pather writes to its own internal files.  
> Delete the bundled `README.md` file if you'd like.

### Running setup.py
Run setup.py **: : `py setup.py`**   
> You will be prompted to enter where the `Pather` folder is ( folder with source code ).  
> Simply enter the current working directory.
> 
> ![](/images/pather/pather-1.jpg)

Move the `pather.bat` file to a folder that's accessible via your system's `PATH` variable.
* For Windows, this [guide](https://stackoverflow.com/a/44272417) may help.
* For UNIX, this [guide](https://www.cs.purdue.edu/homes/bb/cs348/www-S08/unix_path.html) may help.

You should now be able to run the command `pather` from anywhere in your system.

## Getting Started
> Tip : : You can shorten the commands to `a`, `d`, and `l` if you'd like, simply edit `menu.py`  
> Tip : : These commands are not case sensitive. ( directory paths are if your machine is UNIX based )
### Jump command
To move to your specified directories simply enter the number next to the menu string:
```
 >> NUMBER
```
### Add command
To add entries to your Pather directory list, the syntax of the add command is like so:
```
 >> add "TITLE" "PATH"
```
Where `PATH` is the actual directory to jump to and `TITLE` is the string to show in the menu.  
You can type cwd 
Spaces are allowed as long as the string is within the quotes.  

### Del command
To delete entries from your Pather directory list, the syntax of the del command is like so:
```
 >> del NUMBER
```
Where `NUMBER` is the number next to your menu string.

### Last command
To quickly jump to the last directory you opened Pather from, the syntax of the last command is like so:
```
 >> last
```
