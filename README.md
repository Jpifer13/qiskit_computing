This project is to test qiskit quantum computers and is used to learn how to use said computers as well as learn about quantum mechanics/computers.

First thing first is to create a free account on IBM Quantum Systems. Instructions to do so can be found here: [link]https://qiskit.org/documentation/install.html. Make sure you get your qiskit token from your account page and copy if for later.
Once you have created an account you can install Qiskit and start creating circuits!

Now that you have an accound with IBMQ you need to create a directory locally where you want to clone this repo into. Once a directory is made use git clone to
pull this repo.

To run application a virtual environment needs to be made using whatever environment tool you use. I prefer Pythons default virtual environment tool.

From the command line run: ```python -m venv venv```

After the environment is created you need to run it.
On windows run: ```./venv/Scripts/activate```
On linux run: source ```./venv/bin/activate```

Next you need to install all dependencies which can be found in requirements.txt. 
Python:
```pip install -r requirements.txt```
Linux:
```pip3 install -r requirements.txt```

Now we want to use the Qiskit login token that you have from creating an IBMQ account. You need to assign this token string as an environment variable called "QISKIT_TOKEN". Personally I like to edit my virtual environment activation script to also create the environment variable to store this token. If you want to do this follow these instructions:

    On Windows:
        You will want to add this token to too places. One for each activation script. There is a .bat script and a .ps1 script for a command line activation or a powershell respectively. You can find these script in your venv directory. If you used pythons venv maker then they can be found here: /venv/Scripts/activate.bat and /venv/Scripts/Activate.ps1. At the bottom of the .bat file add this line:
            ```set "QISKIT_TOKEN = your_token_here"```
        and at the bottom of the .ps1 file add this line:
            ```$Env:QISKIT_TOKEN = "your_toke_here"```
        You add these to both files to cover both bases in case your IDE runs a powershell or cmd. Or you run one or the other.

    On Linux:
        *To be added at a later date, but it is much the same as above and you should only have to edit the activate file without a filetype.

Now that all dependencies are installed on your virtual environment you can run this application by using the command:
```python ./app.py``` on windows or ```python3 ./app.py``` on linux.
