# Termux Android Geocoords


## Usage

1. Open the termux app.
2. Go to the base directory for this project.
3. Edit you user information:
* ```cp conf/.env.example conf/.env```
* ```nano conf/.env```
* 
4. Run the following:
* ```python main.py```

## Installing Termux and python setup
 1. Go to PlayStore and download: Termux and Termux-API.
 2. Open the Termux app.
 3. Run the following:

* ```apt update```
* ```apt upgrade```
* ```apt install termux-api```
* ```termux-setup-storage```
* ```pkg install git```
* ```pkg install curl```

4. Configure git.

* ```git config --global user.name "YourName"```
* ```git config --global user.email your@email.com```

5. Install python.

* ```pkg install python```
* ```apt install python-dev```
* ```pip install --upgrade pip```

6. Install advanced python libs.

* ```curl -L https://its-pointless.github.io/setup-pointless-repo.sh | sh```
* ```pkg install scipy```

7. Install other python dependencies.

* ```pip install -U python-dotenv```
* ```pip install requests==2.3```

8. Clone this repo.

* ```git clone https://github.com/rhdzmota/termux-android-geocoords.git```


9. Optional (recommended).

* ```pkg install vim```
* ```apt install nano```