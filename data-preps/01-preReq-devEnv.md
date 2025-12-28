# 1. Prerequisites & Dev Environment

1. Install Python 3.10+ (or latest stable).

   > check syllabus > Setup Checklist

2. Create project folder (pwd)
   > ex.pwd : _"REPO_ALIEN_01"_

- go to PWD > RC > "open Git Bash here" > T:$ `code .` > Enter
- open VSCode > open Terminal (Ctrl + `) :
  - T:$ `mkdir python-brocode-test1`
  - or, use existing project folder: `python-brocode-test1`

3. Prepare documentation for the project:

- go to new project folder > create new folder:
  - T:$ `cd python-brocode-test1`
  - T:$ `mkdir data-prep`
  - T:$ `echo "# Project Guidance" > py-guide1.md`

4. define virtual env (venv) for this project

- T:$ `python -m venv .venv`

- next, Activate venv (Win)
  - T:$ `.venv\Scripts\activate`

### If you use VSCode, instead of Jupyter Notebook, follow the instruction below:

5. Setup VSCode

- Install Python extension.

#### use Local env

- Select the Python interpreter for the workspace:

  - press `Ctrl+Shift+P` > to open command palette
  - type 'Python: Select Interpreter' and select it
  - then, select 'Enter Interpreter path' >
  - go to: `(project folder)/.venv/Scripts/python.exe` > RC > Copy path
  - paste it (as Interpreter path)
    - D:\DEV_PHYTON2b (DA-ML)\REPO-BASUKI-PY-ML-CLONE\basuki_python-master\.venv\Scripts\python.exe

- or, when we run the script > it will require interpreter > go to command pallete
  - "Select Another Kernel.." > Python Environment.. : `(project folder)/.venv/Scripts/python.exe`
- it becomes local interpreter: `.venv (3.13.7)`
  > .\basuki-python-master\.venv\Scripts\python.exe

#### use Conda env

- or, use Conda Interpreter path: `Python 3.11.7 (64-bit)`
  > c:\ProgramData\anaconda3\python.exe

#### use Global env

- or, use Global Interpreter path: `Python 3.13.7 (64-bit)`
  > ~\AppData\Local\Programs\Python\Python313\python.exe

# 2. Start to write code

Test to assign the same variable twice, it simply changes values.

```python
test = 3
test = "cheese"
print(test)
```

- Install package needed > Writes to venv

# 3. Run & debug your Python file

- Run the program:
  - by clicking button (>): 'Run Python File'
  - or using terminal command > T: `python main-test1.py`

#### Next, deactivate virtual env (venv) after running the script

- terminal command > T: `deactivate`
- venv will be deactivated, and terminal prompt will return to normal

---

> [!NOTE]
> To preview markdown file

- [x] install extention: Markdown Preview Enhanced (by Yiyi Wang)
  - to run preview on side: **_(Ctrl+k) v_**
- [x] install GitLens (by GitKraken)
  > [!WARNING]
  > This is a warning.
