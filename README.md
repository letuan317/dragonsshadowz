# dragonsshadowz

## Requirements
Hi there, I wanted to create a python application designed to manage RPA (robotic process automation) bots. I'm not sure if you are familiar with RPA technology but the way it's used in the industry today ranges from data extraction to analytics.

The main issue with RPA technology is that it requires high admin privileges as well as access to hardcoded passwords which both are a high security risk. I was wondering if you are able to design a python program which is an all in one integrated solution to manage these RPA bots implementing the following 3 features:

1) Audit log management (Keeps track of the bot seeing which files have been accessed etc.)

2) Bot password manager (e.g use a central repository to store all passwords securely, perhaps use encryption for additional security or OTPs for the bots to use to mitigate the attack surface)

3) Bot status monitoring (Is the bot offline/online)

Please let me know if you're up to the task, thank you :)

***

So I've been trying to visualise things and see how everything will fit together. I was writing some notes earlier showing the order of process going on. Because this is a security tool we will need to be able to test it with a test bot as well as a database. These are necessary to demonstrate that the program can identify what the bot is accessing in particular as well as providing the secure token in order to gain access to the database.

***

So it would first retrieve the token from the encrypted password generator and try to login to the database
Then it would log all the changes made to the database
And then send the changes made to the program
This will allow the user to see logs of the database being changed
What time, date etc
or what files where accessed
So the bot isn't built yet i need you to make one in addition to the program. There is a framework for python that I'd recommend called robotframework. It includes everything you need in order to make your own bot and it has inbuilt functions which allow you to monitor the status of bots etc.
Here is the documentation 

https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html


It's up to you whatever you think is a more elegant solution to have the bot running locally or on web
I think the most secure method is to use sha256 hash function
I was thinking for the password manager we can make it even more secure by only allowing session based requests for the bot
So only when the bot needs access it will ask for a token
So each time it access the database it will be a different password
It's just a function to show record the logs then send to the admin

https://gist.github.com/amelieykw/115bbf45c4ac1272c4d72e1b47ab3f50

The main purpose here is we don't want to store clear text passwords anywhere in the program

