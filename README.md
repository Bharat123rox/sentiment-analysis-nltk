# Sentiment Analysis using NLTK
## Python Sentiment Analysis using NLTK
If you are on Ubuntu/Debian distros, python 3 (preferably Version 3.5 and above) must already be up and running on your machine, otherwise get python3 for Windows [here](https://www.python.org/downloads/windows/)

Check your python 3 version using:- 
```sh
python3 --version
```
At first, install pip using:- 
```sh
sudo apt install python3-pip
```
Or the corresponding commands such as ``` sudo pacman ``` or ```sudo yum ``` etc.
Then, the dependencies for this project must be installed using:- 
```sh
pip install -r requirements.txt
``` 
After which,this repository must be cloned usingth
```sh
git clone https://github.com/Bharat123rox/sentiment-analysis-nltk.git
```
and then a file named `secretkeys.py` must be created with the following:-
```python
consumer_key = 'zxcvzxcvzxcvzxcv'
consumer_secret = '1234123412341234'
access_token = 'qwerqwerqwerqwerqwer'
access_token_secret = 'asdfasdfasdfasdfasdf'
```
(These are just sample keys, these must be replaced with the actual user API keys on registering for a Twitter App)
Registering for a new Twitter App can be done [here](https://apps.twitter.com/app/new) on Twitter Developers, and on completion of registration, these keys will be generated.

After this, the code can be used and edited freely for any purpose.

This code is covered by GNU GPL v2.0 License.

Contributions and patches are definitely welcome.
