## QuackPass

An easy password system for text based adventure type games!

### Setup

```
pip install quackpass
```

You need to be using a version greater then 3.6 for this library to work. 

### Usage

**Easy:**

Code:

```py
import quackpass

login_sys = quackpass.SimpleLogin()

# add a user (Only run once)

login_sys.add_user("Admin", "Secret") # replace with <username> & <password> Respectively

# Login

user = login_sys.login()

print(f"Logged in as {user}")
```

Output:

```
Username: adfadfa
Password: adfasdf
Incorrect Password or Username!
Username: Admin
Password: Secret
Logged in as Admin
```

**Advanced:**

Code: 

```py
import quackpass

login_sys = quackpass.SimpleLogin(
	salt = "supersecretsalt",
	file = "mypasswords.txt", # if not set the system will automatically choose "password.txt" as it's file for storing passwords
)

login_sys.add_user("Admin", "SECRET_pass123!", overwrite=True) # we want to overwite becuase this is an admin account

user = login_sys.login(
	username_prompt="Gimme ya username: ",
	password_prompt="Now ya password: ",
)

print(f"Logged in as {user}")
```

Output:

```
Gimme ya username: Admin
Now Ya password: SECRET_pass123!
Logged in as Admin
```