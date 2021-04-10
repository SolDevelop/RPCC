# what is RPCC
RPCC is a python&php program that allow you to control your pc using shortcuts
# Updates 
Linux load.key is about to be done
-
# Coming Soon
You Can Run the selected Commands in your Windows soon
RPCC Customizer Coming Soon
-
If You Want to donate go to [PayPal](https://www.paypal.me/soldeveloperm)

OS Support List:

Windows Support (✅)

Mac Support (✅)

Linux Support (❌)

BSD Support (❌)

Jailbroken IDevices Support (❌)

# How To Setup It?
First You Need to have php & python in Your PATH variable

Next Clone RPCC next Unzip RPCC

Next Open cmd then type this to install the requirements ( pip install requirements.txt )

Next type in the already opened cmd ( python [main.py](https://main.py) \-setup ) then wait 5 to 10 seconds

Next Open The load.key file change or put things example:

{"chrome": "C:\\\\Program Files (x86)\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe", "mems": "C:\\\\Program Files (x86)\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe"}

you can put firefox or  anything but we will be putting firefox to teach you! then it will be like this

{"Windows": [{"chrome": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe", "mems": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"}, "firefox": " C:\\\\Program Files (x86)\\\\Mozilla Firefox\\\\firefox.exe"],"Darwin": [{"safari": "//Applications//Safari.app"}]}

Next Type in already opened cmd ( python [main.py](https://main.py) \-run ) it will ask you about the ip that the server will be running on You Can Choose from [127.1.1.0](https://127.1.1.0) or your local ip \[Recommended\] or your internet ip after that the server will be running! (the server will not be closed after you close cmd you need to open task manager then kill php.exe yourself)

Here is a shortcut example:  [https://www.icloud.com/shortcuts/7244c1caabb149b4aa07dc40264b8abf](https://www.icloud.com/shortcuts/7244c1caabb149b4aa07dc40264b8abf)

And Its Done!

Demo Video:

[Click to watch](https://youtu.be/Cv01ASTEgQk)


&#x200B;

How It Work (IMPORTANT):

First after you setup it it will open the 80 port

Next when you use -run it launch the php server buitl-in!

When You Try To Open the website you should put this url:

http://\[the-ip-you-choosed-in-the-run\]/index.php?run=\[launching point\]

the lanuching point will run the program/app you want in windows remotely !

the launching point is the program path thats stored in load.key you need to change it or keep it as i made it

load.key should look like this

{"Windows": [{"chrome": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe", "mems": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"}],"Darwin": [{"safari": "//Applications//Safari.app"}]}
change everything but make sure the json is working

# Credits
Sol aka Soldevelop & Soldeveloper

# the main subreddit for this program is r/RPCC

# This Project Is Under GPLv3 License 
