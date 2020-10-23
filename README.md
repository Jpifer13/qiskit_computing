This project is to test qiskit quantum computers and is used to learn how to use said computers as well as learn about quantum mechanics/computers.

First thing first is to create a free account on IBM Quantum Systems. Instructions to do so can be found here: https://qiskit.org/documentation/install.html
Once you have created an account you can install Qiskit and start creating circuits!

To run application a virtual environment needs to be made using whatever environment tool you use. I prefer Pythons default tool.

From the command line run: ```python -m venv venv```

After the environment is created you need to run it.
On windows run: ```./venv/Scripts/activate```
On linux run: ```source ./venv/bin/activate```

Next you need to install all dependencies which can be found in requirements.txt.\
Python:\
```pip install -r requirements.txt```\
Linux:\
```pip3 install -r requirements.txt```

Last thing you need to do before running this is add your client_token that you should have copied from your IBMQ account and set it as an environment variable. Personally I just edit the venv activation batch file so that everytime I launch the virtual environment my token is set. To do this on windows open up the file venv/Scripts/activate.bat and add this line to the bottom: ```set "QISKIT_TOKEN = your_token_string_here"```


Now that all dependencies are installed on your virtual environment and your token is set to an environment variable you can run this application by using the command:
```python ./app.py on windows or python3 ./app.py on linux.```