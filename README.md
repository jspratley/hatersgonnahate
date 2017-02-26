##Overview

Web application that allows the user to block a person from multiple social media websites at the same time.  We originally created this project for Boilermake 2017, but didn't come close to finishing it there.  Instead, after leaving it for almost a month, we picked it up again at HackIllinois 2017, this time actually completing it.

##Tech Stack

This application runs primarily on Python, using Flask.  On the front end, we use Jinja2 and JQuery.


##Instructions for Running

Windows: either open the project in PyCharm, right-click on the 'main.py' file, and click 'Run', or navigate to the root directory of the project and double-click on the 'main' file.  

NOTE: in order for searching and blocking to work, you need to have a config.py file.  That config needs four things, in this format:

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

You can generate these for your own Twitter account by registering your web application with Twitter.

##Contributing

A guide on how to contribute can be found here: https://github.com/jspratley/hatersgonnahate/blob/master/Contributing.md
