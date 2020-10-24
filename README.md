This project is to test qiskit quantum computers and is used to learn how to use said computers as well as learn about quantum mechanics/computers.

First thing first is to create a free account on IBM Quantum Systems. Instructions to do so can be found here: [link]https://qiskit.org/documentation/install.html
Once you have created an account you can install Qiskit and start creating circuits!

To run application a virtual environment needs to be made using whatever environment tool you use. I prefer Pythons default tool.

Now that you have an accound with IBMQ you need to create a directory locally where you want to clone this repo into. Once a directory is made use git clone to
pull this repo.

From the command line run: python -m venv venv

After the environment is created you need to run it.
On windows run: ./venv/Scripts/activate
On linux run: source ./venv/bin/activate

Next you need to install all dependencies which can be found in requirements.txt. 
Python:
pip install -r requirements.txt
Linux:
pip3 install -r requirements.txt

Now that all dependencies are installed on your virtual environment you can run this application by using the command:
python ./app.py on windows or python3 ./app.py on linux.