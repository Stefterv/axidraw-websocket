# Axidraw Websocket

An attempt to create a websocket layer on top of the Axidraw CLI



## Installation

1.) Install python

Macs and linux boxes usually have python pre-installed.

If you are on Windows, you'll probably not already have this on your computer. 
Go to: https://www.python.org/download/



2.) Install pip

python versions 3.6 and newer come with pip pre-installed.

If you do not have pip, download and install it, following the instructions at:
https://pip.pypa.io/en/stable/installing/


3.) [Optional:] Use virtualenv to control versioning


Install virtualenv:

```
pip3 install virtualenv
```

Create a virtual python environment:

```
virtualenv -p $(which python3) venv
```

This creates a directory called `venv` which contains the files for the new environment.
Replace `python3` with the name of the python on your system you want to use, e.g.  `python3.5`, `python3.6`, etc.

Enter the environment:

```
source venv/bin/activate
```

Now your command prompt should be prefixed with "(venv)", indicating that you are now in the virtual environment you created.
You can now continue as normal.
More reading: https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv


4.) Install AxiDraw API/CLI 

```
pip install https://cdn.evilmadscientist.com/dl/ad/public/AxiDraw_API.zip
```