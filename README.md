# Python Programming Practice 🐍

A collection of beginner-friendly Python programs created for learning and practicing Python fundamentals.

## 📚 Programs Included

The repository contains small, individual Python programs covering calculations, conditional statements, loops, tuples, and classes.

| File | Topic | What it does |
|---|---|---|
| `1 to20.py` | Loops | Prints numbers from 1 to 19 using `range(1, 20)`. |
| `5tiemdiaply.py` | Tuples | Creates a tuple and prints the original tuple, its reverse, and its last three elements. |
| `accpttwo.py` | Menu-driven calculator | Accepts two numbers and performs addition, subtraction, multiplication, or division based on the selected menu option. |
| `aeraofcircle.py` | Circle calculations | Calculates the area and circumference of a circle from its radius. |
| `areatrianglr.py` | Triangle area | Calculates a triangle's area from its base and height. |
| `armstrong.py` | Number logic | Checks whether a number is an Armstrong number. |
| `calculategrosssalary.py` | Salary calculation | Calculates gross salary by adding basic salary, HRA, and DA. |
| `calculateintrest.py` | Simple interest | Calculates simple interest using principal, rate, and time. |
| `call clas method.py` | Classes and methods | Defines a calculator class and calls its `add()` method. |
| `celsius.py` | Temperature conversion | Converts Celsius to Fahrenheit. |
| `classstudent.py` | Classes and objects | Defines a student class with name, roll number, and marks, then displays them. |
| `constructor.py` | Constructors | Uses `__init__()` to initialize a student's name and marks. |
| `evaluate.py` | Average calculation | Accepts four values and calculates their average. |
| `evenandodd.py` | Conditional statements | Checks whether an integer is even or odd. |
| `factorial.py` | While loop | Calculates the factorial of an entered number. |

## 🧰 Requirements

- Python 3
- A code editor such as Visual Studio Code (recommended)
- Git, if you want to upload the project to GitHub

These are basic Python scripts and do not require third-party packages based on the code provided.

## 💻 Installation on Windows

### 1. Install Python

1. Download Python from [python.org/downloads](https://www.python.org/downloads/).
2. Run the installer.
3. Select **Add Python to PATH** if that option appears.
4. Complete the installation.

Verify Python is installed by opening Command Prompt or the VS Code terminal and running:

```bash
python --version
```

If the `python` command is not recognized, try:

```bash
py --version
```

### 2. Install Visual Studio Code

Download VS Code from [code.visualstudio.com](https://code.visualstudio.com/). In VS Code, install the **Python** extension published by Microsoft.

### 3. Get the code

Clone this repository (replace `YOUR-USERNAME` with your GitHub username):

```bash
git clone https://github.com/YOUR-USERNAME/python-programming-practice.git
cd python-programming-practice
```

Or download the repository as a ZIP file from GitHub and extract it.

## ▶️ How to Run a Program

1. Open the project folder in VS Code.
2. Open **Terminal → New Terminal**.
3. Run a Python file with:

```bash
python evenandodd.py
```

For example, to run the Celsius converter:

```bash
python celsius.py
```

To run the menu-driven calculator:

```bash
python "accpttwo.py"
```

Use quotation marks around filenames that contain spaces, such as `call clas method.py`.

If `python` does not work on Windows, try `py` instead:

```bash
py evenandodd.py
```

Each file is a separate program. Run one file at a time.

## ✍️ How to Write or Edit Python Code

1. Open the project folder in VS Code.
2. In the Explorer panel, choose **New File**.
3. Give the file a name ending in `.py`, such as `hello.py`.
4. Type your Python code and save with **Ctrl + S**.
5. Open a terminal and run `python hello.py`.

Example:

```python
name = input("Enter your name: ")
print("Hello,", name)
```

## 📤 Upload Your Code to GitHub

### 1. Install Git

Download Git from [git-scm.com/downloads](https://git-scm.com/downloads), then verify it in the terminal:

```bash
git --version
```

### 2. Create a GitHub repository

1. Go to [github.com/new](https://github.com/new).
2. Name the repository `python-programming-practice`.
3. Choose **Public** if you want others to see your learning portfolio, or **Private** if you want to keep it private.
4. Create the repository. If you already have local files, you can leave the option to add a README unchecked.

### 3. Push your local files

Open a terminal in the folder containing your Python files and `README.md`. Run:

```bash
git init
git add .
git commit -m "Add Python practice programs"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/python-programming-practice.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. If a remote named `origin` already exists, do not add it again; check it with `git remote -v`.

For later updates:

```bash
git add .
git commit -m "Update Python practice programs"
git push
```

## 🎯 Learning Goals

- Practice Python input and output
- Use arithmetic operators and formulas
- Understand `if`/`else` conditions
- Practice `for` and `while` loops
- Work with tuples
- Create classes, objects, methods, and constructors
- Learn basic Git and GitHub workflows

## 👤 Author

**Izhaan Inamdar**

GitHub: [IzhaanTech123](https://github.com/IzhaanTech123)

---

This repository is intended for learning and practice. Program behavior depends on the code in each file.
