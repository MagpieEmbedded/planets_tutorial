# Planets Tutorial

This is intended to be a clear step by step project for how to make an accurate animation of the planets in our solar system, in python.
Hopefully, it will also include good practice for programming which will work beyond this project.

# Getting started
Make sure that you are using Python 3.7. This is the latest version of python. 
If for some reason you are using python 2, please stop. 
It won't be supported from 2020 and just isn't as good as the latest version.
Find out more about python and how to install it [here](https://www.python.org).

Clone the repository from [the Github repository](https://github.com/MagpieEmbedded/planets_tutorial.git):
```bash
git clone https://github.com/MagpieEmbedded/planets_tutorial.git
```

In a command terminal, navigate to the cloned directory ([Windows](https://www.digitalcitizen.life/command-prompt-how-use-basic-commands), [Linux](https://www.digitalocean.com/community/tutorials/basic-linux-navigation-and-file-management)) and set up a new virtual environment with a clear name e.g planet_venv:
```bash
python -m venv planet_venv
```
Activate the virtual environment:
```bash
# Unix:
source planet_venv/bin/activate
# Windows:
planet_venv\Scripts\activate
```
There should now be *(planet_venv)* or similar at the start of the command line.

Install the dependencies for the project based on the requirements listed in requirements.txt
```bash
pip install -r requirements.txt
```
Note that because of the virtual environment being used, this should not affect other python scripts running on your computer.
It is quite common to create a new virtual environment for each new project to prevent problems related to dependencies. If this is news, read more about virtual environments and the good they can do [here](https://realpython.com/python-virtual-environments-a-primer/).

Finally, run the final script to see what the final script will look like:
```bash
cd scripts
python moving_planet.py
```

## What now?
The tutorials start from the very beginning and gradually get more complex.
Read up until the point where boredom becomes interest and go from there!
