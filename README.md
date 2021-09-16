# ASL Learning Application

# 1. Install pip, python and virtualenv
* Make sure you already have pip and python installed in your computer<br />

### Checking pip if exists:
```
pip -V
```
### Checking python  if exists:
```
python --version
```
### If you already installed pip, please ignore this step:
```
python get-pip.py
```
* Then, verify Installation and check the Pip Version:
```
pip -V
```
### Install virtual environtment
* Install virtualenv
```
pip install virtualenv
```
* Create a directory to store env
```
mkdir environtments
cd environments
```
* Create a virtual environment
```
virtualenv asl_app
```
* Activate virtual environment
```
asl_app\Scripts\activate
```
# 2. Clone the project
* Make sure you have git installed by checking its version:
```
git --version 
```
* Otherwise, install it:

To install Git for Windows, point your browser at https://git-scm.com/download/win. A download of the Windows Git installer will begin automatically. Once complete, you can double-click the installer and follow the steps.<br />
* You can view your default Git configuration options with the following command:
```
git config -h
```
* Clone the project:
```
git clone https://github.com/phuongngo2904/ASL_Learning_Application.git
```
* Navigate to this project 
```
cd ASL_Learning_Application
```
# 3.  Install requirements
```
pip install -r requirements.txt
```
# 4. Run the real time recognition
```
cd code/gesture_regconition
python log_in_app.py
```
# Reference 
* Dataset: https://www.kaggle.com/grassknoted/asl-alphabet
