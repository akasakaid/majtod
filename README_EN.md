
# MajTod

Automation script bot for Maj*r

# Table of Contents

- [MajTod](#majtod)
- [Table of Contents](#table-of-contents)
- [Registration](#registration)
- [Features](#features)
- [Support Me](#support-me)
- [How to Use](#how-to-use)
  - [Command Line Options / Command Line Arguments](#command-line-options--command-line-arguments)
  - [About Proxies](#about-proxies)
  - [Windows](#windows)
  - [Linux](#linux)
  - [Termux](#termux)
- [How to Update](#how-to-update)
- [JavaScript Code to Get Data in Telegram Desktop Application](#javascript-code-to-get-data-in-telegram-desktop-application)
- [Thank You](#thank-you)
 
# Registration
Follow this link to register: https://t.me/major/start?startapp=629438076

# Features

- [x] Daily Attendance
- [x] Automatic Game Playing
- [x] Automatic Task Completion (not all)
- [x] Proxy Support
- [x] Random User-Agent Usage
- [x] Total Balance Report for All Accounts

# Support Me

If you like my work, you can support me through the links below:

- [Indonesia] https://s.id/nusanqr (QRIS)
- [Indonesia] https://trakteer.id/fawwazthoerif/tip
- [Global] https://sociabuzz.com/fawwazthoerif/tribe
- If you want to send support in another form, you can contact me via Telegram.

# How to Use

## Command Line Options / Command Line Arguments

This script/program supports several argument parameters that can be used. Here's an explanation of the arguments:

`--data` / `-D` can be used when you have a different file name for storing account data. By default, the file name used by this script/program to store account data is `data.txt`. For example, if you have a file named `query.txt` as the file that stores account data, just run `bot.py` by adding the `--data` / `-D` argument. Example: `python bot.py --data query.txt`

`--proxy` / `-P` can be used when you have a different file name for storing the proxy list. The file name used by this script/program to store the proxy list is `proxies.txt`. For example, if you have a file named `prox.txt` as the file that stores the proxy list, you just need to add the `--proxy` / `-P` argument parameter to use your proxy file. Example: `python bot.py --proxy prox.txt`

`--worker` / `-W` this argument is used to customize the number of threads/workers used when this bot script runs. By default, this script/software uses (total CPU cores / 2) workers. For example, if your CPU has 6 cores, the number of workers used is 3. You can customize the number of workers using this argument. For example, if you want to set the number of workers to 100, run `bot.py` with this argument: `python bot.py --worker 100`. And if you don't like using workers/threads/multiprocessing, you can customize the worker to 1, example: `python bot.py --worker 1`.

`--action` / `-A` this argument is used to directly enter the desired menu. For example, if this bot script has 5 menus and you don't want to input manually, you can use this argument to directly enter the desired menu. Example: `python bot.py --action 5` means you will directly enter menu number 5. This argument is useful if you use docker/pm2 to run the bot script in the background process.

## About Proxies

Register on the following website to get free proxies: [Here](https://www.webshare.io/?referral_code=dwj0m9cdi4mp)

Website with the cheapest proxy price $1/GB [Here](https://dataimpulse.com/?aff=48082)

You can add the proxy list in the `proxies.txt` file and the proxy format is as follows:

If there is authentication:

Format:

```
protocol://user:password@hostname:port
```

Example:

```
http://admin:admin@69.69.69.69:6969
```

If there is no authentication:

Format:

```
protocol://hostname:port
```

Example:

```
http://69.69.69.69:6969
```

Please pay close attention to whether the proxy you are using requires authentication or not, as many people DM me asking how to use proxies.

Here's how to use it on several operating systems:

## Windows

1. Make sure your computer has Python and Git installed. If not, you can install them first.

   Recommended Python version is 3.10

   Download Python: [https://python.org](https://python.org)

   Download Git: [https://git-scm.com](https://git-scm.com/)

2. Open Terminal / CMD

3. Clone this repository
   ```shell
   git clone https://github.com/akasakaid/majtod.git
   ```

4. Enter the majtod folder
   ```shell
   cd majtod
   ```

5. Install the required libraries
   ```shell
   python -m pip install -r requirements.txt
   ```

6. Edit/modify the `data.txt` file, fill the `data.txt` file with your account data. You can get your account data by using the JavaScript code I have provided below.

7. Run/execute the main file
   ```shell
   python bot.py
   ```

## Linux

1. Make sure your computer has Python and Git installed. If not, you can install them first.

   Linux command to install Python and Git:

   ```shell
   sudo apt install python3 python3-venv python3-pip git -y
   ```

2. Clone this repository
   ```shell
   git clone https://github.com/akasakaid/majtod.git
   ```

3. Enter the majtod folder
   ```shell
   cd majtod
   ```

4. Create a virtual environment and activate it.
   
   ```shell
   python3 -m venv env && source env/bin/activate
   ```

5. Install the required libraries
   ```shell
   python -m pip install -r requirements.txt
   ```

6. Edit/modify the `data.txt` file, fill the `data.txt` file with your account data. You can get your account data by using the JavaScript code I have provided below.

7. Run/execute the main file
   ```shell
   python bot.py
   ```

## Termux

1. Make sure Python and Git are installed in your Termux application. If not, you can install them first.
   
   ```shell
   pkg update -y && pkg upgrade -y && pkg install python git -y
   ```

2. Clone this repository
   ```shell
   git clone https://github.com/akasakaid/majtod.git
   ```

3. Enter the majtod folder
   ```shell
   cd majtod
   ```

4. Install the required libraries
   ```shell
   python -m pip install -r requirements.txt
   ```

5. Edit/modify the `data.txt` file, fill the `data.txt` file with your account data. You can get your account data by using the JavaScript code I have provided below.

6. Run/execute the main file
   ```shell
   python bot.py
   ```

# How to Update

First, delete the `database.sqlite3` file. You can use the terminal command below (adjust according to your operating system)

Windows CMD / Windows PowerShell

```shell
del database.sqlite3
```

Linux/Termux/Unix/MacOS

```shell
rm database.sqlite3
```

You can update simply by using the `git pull` command if you initially cloned the repository with git.
If you didn't clone the repository with git, you can force an update with the command below (adjust according to your operating system).

Windows powershell : 
```shell
Invoke-WebRequest https://raw.githubusercontent.com/akasakaid/majtod/refs/heads/main/bot.py -OutFile bot.py; Invoke-WebRequest https://raw.githubusercontent.com/akasakaid/majtod/refs/heads/main/models.py -OutFile models.py; Invoke-WebRequest https://raw.githubusercontent.com/akasakaid/majtod/refs/heads/main/requirements.txt -OutFile requirements.txt
```

Linux/Termux/Unix/Windows CMD/MacOS: 

```shell
curl https://raw.githubusercontent.com/akasakaid/majtod/refs/heads/main/bot.py -o bot.py && curl https://raw.githubusercontent.com/akasakaid/majtod/refs/heads/main/models.py -o models.py && curl https://raw.githubusercontent.com/akasakaid/majtod/refs/heads/main/requirements.txt -o requirements.txt
```

# JavaScript Code to Get Data in Telegram Desktop Application

Here are some JavaScript codes you can try to get data through the Telegram desktop application.

After you execute the code, try pasting it. If it doesn't appear, try another JavaScript code.

```javascript
copy(Telegram.WebApp.initData)
```

```javascript
copy(JSON.parse(sessionStorage.__telegram__initParams).tgWebAppData)
```

# Thank You