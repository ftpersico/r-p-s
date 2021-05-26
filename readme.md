# readme



## Installation

Fork this [remote repository](https://github.com/ftpersico/r-p-s.git) under your own control, then "clone" or download your remote copy onto your local computer.


Navigate to the root directory of this repo on your local computer. 

Use Anaconda to create and activate a new virtual environment. Replace 'your-env-name' with the name you choose for your environment:

```sh
conda create -n your-env-name python=3.8
conda activate your-env-name
```


After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

From within the virtual environment, run the Python script using the command:

```sh
python game.py
```

**Note:** The game will automatically pull your user name from the .env file in your local directory. If you'd like to change your user name you can do so in that file.

