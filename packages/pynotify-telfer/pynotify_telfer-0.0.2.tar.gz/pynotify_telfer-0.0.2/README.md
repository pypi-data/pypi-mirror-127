# PyNotify

Notify yourself when your python script (or other programs) are done.

## Usage
```
notify send "Complete" "Simulation x has finished"
```

or 

```
import pynotify
pynotify.send("Complete", "simulation x has finished")
```

## Setup 

### Create an Email Account to Send From

1. Create a new google account

2. Go into the account `settings > security` then allow `Less secure apps`

![image-20211113125642543](/home/andretelfer/.var/app/io.typora.Typora/config/Typora/typora-user-images/image-20211113125642543.png)

### Install 
Clone this repository and cd into it
```
pip install --user pynotify-telfer
```

### Configure

Save the bot information
```
notify sender update --email <bot email> --password <bot password>
```

Add your recipients

```
notify add <your email>
```
