# what is RPCC
RPCC is a python&php program that allows you to control your pc using shortcuts
# Updates 
BSD in Work
-
# Coming Soon
RPCC Customizer Coming Soon
-

OS Support List:

Windows Support (✅)

Mac Support (✅)

Linux Support (✅)

BSD Support (❌)

Jailbroken IDevices Support (❌)

# New Features
Screenshot Support for windows

Linux Support

RUN COMMANDS In WINDOWS Using ?command="the command that you want"

Screenshot Shortcut: [Click here]("https://www.icloud.com/shortcuts/3f4992bcf485488cba010d4a0fd1f8a3")
# How To Setup RPCC?
First You Need to have php & python in Your PATH variable

Next Clone RPCC next Unzip RPCC

Next Open cmd then type this to install the requirements ( pip install -r requirements.txt )

Next type in the already opened cmd ( python main.py \-setup ) then wait 5 to 10 seconds

Next Open The load.key file change or put things example:

{"chrome": "C:\\\\Program Files (x86)\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe", "mems": "C:\\\\Program Files (x86)\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe"}

you can put firefox or  anything but we will be using firefox to teach you! now your load.key should look like this:

{"Windows": [{"chrome": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe", "mems": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"}, "firefox": " C:\\\\Program Files (x86)\\\\Mozilla Firefox\\\\firefox.exe"],"Darwin": [{"safari": "//Applications//Safari.app"}]}

Next Type in already opened cmd ( python main.py \-run ) it will ask you about the ip that the server will be running on You Can Choose from [127.1.1.0](https://127.1.1.0) or your local ip \[Recommended\] or your internet ip after that the server will be running! (the server will not be closed after you close cmd you need to open task manager then kill php.exe yourself)

Here is a shortcut example:  [https://www.icloud.com/shortcuts/7244c1caabb149b4aa07dc40264b8abf](https://www.icloud.com/shortcuts/7244c1caabb149b4aa07dc40264b8abf)

And Its Done!

Demo Video:

[Click to watch](https://youtu.be/Cv01ASTEgQk)

Screenshot Demo Video:

[Click Here to Watch](https://youtu.be/x-SCCDVFTz8)

&#x200B;

How does It Work (IMPORTANT):

First after you setup it it will open the 80 port

Next when you use -run it launches the php server that is built-in!

Url Structure:

http://\[the-ip-you-choosed-in-the-run\]/index.php?run=\[launching point\]

the lanuching point will run the program/app you want in windows remotely !

the launching point refers to the program path thats stored in load.key, you can change it to whatever you want

Default load.key File content:

{"Windows": [{"chrome": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe", "mems": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"}],"Darwin": [{"safari": "//Applications//Safari.app"}]}
change everything but make sure the json is working

# Credits
Sol aka Soldevelop & Soldeveloper


# This Project Is Under GPLv3 License 
