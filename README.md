# Personal Book Manager

![Python](https://img.shields.io/badge/Python-3.13-blue?logoColor=white)

## Project Structure

```text
Personal_Book_Manager/
│   .env
│   .env.example
│   .gitignore
│   app.log
│   books.json
│   books.py
│   debug.log
│   error.log
│   main.py
│   README.md
│   requirements.txt
│
├───gifs
│       demo.gif
│
├───screenshots
│       image.png
```
## File Description

| File                 | Description                                             |
| -------------------- | ------------------------------------------------------- |
| `main.py`            | Main file used to run the quiz game                     |
| `books.py`        | Stores questions and answers                            |
| `requirements.txt`   | Lists the Python packages needed for the project        |
| `.env.example`       | Shows the environment variables needed by the project   |
| `.gitignore`         | Tells Git which files and folders should not be tracked |
| `README.md`          | Contains the project documentation                      |
| `screenshots/`          | Stores project screenshots                              |
| `gifs/`              | Stores demo GIF files                                   |

## Features
- add multiple tasks
- save tasks
- load save tasks
- admin mode

## Requirements
- python
- python-dotenv

## Installation 
Install the require packages

```bash

python -m pip install -r requirements.txt

```

## Envoirment setup
Create a `.env` file in the project folder

Use `.env.example` file as a template

Add your admin password 

```env
ADMIN_PASSWORD = "YOUR_PASSWORD_HERE"
```
Replace `YOUR_PASSWORD_HERE` with your own addmin password

## Run the program

Run the main file: 
```bash
python main.py
```

## How It Works

1. The program asks for your name.
2. It welcomes you.
3. It asks if you want to use Admin Mode.
4. If you choose yes, it asks for your password.
5. It loads previously saved books.
6. You enter the number of books.
7. You enter the book names.
8. The program displays and saves your books.


## Screenshot
![run project](screenshots\image.png)

## Demo
![](gifs\demo.gif)

## Troubleshooting
### FileNotFoundError
1. **What does it mean?**
The program cannot find the required file.

2. **Why might it happen?**
The program may be running from the wrong directory, or a required file may be missing.

3. **What should I check first?**

I check the project folder and make sure I am running the program from the correct location.

### JSONDecodeError
1. **What does it mean?**
The program cannot read the JSON data correctly.

2. **Why might it happen?**
The `books.json` file may be empty or contain invalid JSON data.
3. **What should I check first?**
I check whether `books.json` contains valid JSON data.

### ModuleNotFoundError: No module named 'dotenv'
1. **What does it mean?**
Python cannot find the `python-dotenv` package.

2. **Why might it happen?**
The required package has not been installed in the current Python environment.

3. **What should I check first?**
I check the installed packages and make sure `python-dotenv` is installed.

### Admin Password Not Working
1. **What does it mean?**
The program cannot read or verify the Admin Mode password.

2. **Why might it happen?**
The `.env` file may be missing, the variable name may be incorrect, or the password may not match.

3. **What should I check first?**
I check that the `.env` file exists and contains the correct variable:
`BOOK_MANAGER_ADMIN_PASSWORD`
I also check that the password is correct and `load_dotenv()` is called in the program.