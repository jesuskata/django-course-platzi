# Platzi Django Course

This is the README file to have a step by step to run the project in your local machine.

## Commands to start the project

### Virtualenvironment

Create a virtualenvironment with the library of your preference, in my case I used virtualenv, and the commands are:

```bash
virtualenv .venv
```

Once created, you will need to add the actual libraries to run the project:

```bash
# First of all, activate the virtualenv
source .venv/bin/activate
# Now run the pip command to install into the virtualenv the correct libraries
pip install -r requirements.txt
```

### Run the project in your local machine

Now you anly need to run the command:

```bash
./manane.py runserver
```

Now in your browser enter:

[localhost](http://localhost:8000)
