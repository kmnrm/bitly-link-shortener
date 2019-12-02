# Bitly url shorterer
Bitly url shorterer is a program, that lets you shorten long URLs by [BITLY URL shorten service](https://bit.ly) via console commands. This program also counts clicks on a user's short bit.ly link.

### How to install
1. Sign up on [bit.ly](https://bit.ly) and then sign in.
2. Go to [edit profile](https://bitly.com/a/oauth_apps) in your menu and get a Generic Access Token by confirming your account password.
This is a generic oauth token that is needed for interacting with the Bitly API. 
A generic token may look like `12c34e61ad592301996ca1234567ddff00231ad8`.

3. Create a `.env` file in `main.py` file directory and add your token in `BITLY_GENERIC_ACCESS_TOKEN_1={your_token}` format without any parenthesis, quotation marks or spaces. Here's an example of an `.env` file:
```
BITLY_GENERIC_ACCESS_TOKEN_1=12c34e61ad592301996ca1234567ddff00231ad8
```

Preinstall Python3 to use this program.
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Getting started
A user link is required as a positional argument:
```
C:\Users\User\bitshortener> python main.py -h
usage: main.py [-h] userlink

Bitly url shorterer is a program that lets you shorten long urls by BITLY URL
shorten service via console commands. This program also counts clicks on
user's short bit.ly links.

positional arguments:
  userlink    User URL

optional arguments:
  -h, --help  show this help message and exit
```

Start with opening the command line interpreter. Then insert your link with or without `http://`:
```
C:\Users\User\bitshortener> python main.py dvmn.org
Here's your bitlink, gringo: bit.ly/2P4hRWf
```
```
C:\Users\User\bitshortener> python main.py http://dvmn.org
Here's your bitlink, gringo: bit.ly/2P4hRWf
```

If user's link is already bit-shortened, the program counts link clicks and makes it an output:
```
C:\Users\User\bitshortener> python main.py bit.ly/2P4hRWf
Total clicks: 1
```
```
C:\Users\User\bitshortener> python main.py http://bit.ly/340L4HF
Total clicks: 3
```

### Project Goals
The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
