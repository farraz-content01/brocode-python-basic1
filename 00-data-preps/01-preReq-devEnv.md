# Python - Prerequisites & Dev Environment
## A. Install Python & Define Environment
1. Install Python 3.10+ (or latest stable).

2. Create project folder (pwd)
   > ex.pwd : _"D:\REPO_ALIEN_01\farraz-content01"_

- go to PWD > RC > "open Git Bash here" > T:$ `code .` > Enter
- open VSCode > open Terminal (Ctrl + `) :

  - T:$ `mkdir python-noval-basic1 && cd python-noval-basic1`
  - or, use existing project folder: `python-noval-basic1`

- Save VSCode-workspace > to upper from project-folder:
  > save in pwd : _"D:\REPO_ALIEN_01\farraz-content01"_

3. Prepare documentation for the project:

- go to new project folder > then, create new folder:
  - T:$ `cd python-brocode-test1`
  - T:$ `mkdir 00-data-preps`
  - T:$ `echo "# SYLLABUS" > 00-syllabus-noval-python2026.md`

4. define virtual env (venv) for this project

- go to new project folder > then, open Terminal:
- T:$ `python -m venv .venv`

- next, Activate venv (Win)
  - T:$ `.venv\Scripts\activate`

### If you use VSCode, instead of Jupyter Notebook, follow the instruction below:

5. Setup VSCode

- Install Python extension.

#### use Local env

- Select the Python interpreter for the workspace:

  - press `Ctrl+Shift+P` ➜ to open command palette
  - type **'Python: Select Interpreter'** ➜ select it
  - then, select: `.venv\Scripts\python.exe` -- Recommended
  - or, select 'Enter Interpreter path' >
  - go to: `(project folder)/.venv/Scripts/python.exe` > RC > Copy path
  - paste it (as Interpreter path)
    > _D:\REPO_ALIEN_01\farraz-content01\python-noval-basic1\.venv\Scripts\python.exe_

- or, when we run the script ➜ it will require interpreter > go to command pallete
  - "Select Another Kernel.." ➜ Python Environment.. : `(project folder)/.venv/Scripts/python.exe`
- it becomes local interpreter: `.venv (3.13.7)`
  > it will also need to install .ipykernel

#### use Conda env

- or, use Conda Interpreter path: `Python 3.11.7 (64-bit)`
  > c:\ProgramData\anaconda3\python.exe

#### use Global env

- or, use Global Interpreter path: `Python 3.13.7 (64-bit)`
  > ~\AppData\Local\Programs\Python\Python313\python.exe
---
## B. Setting Up 'Run by Line' & 'Debugging' Tools 
> Install `ipykernel` ➜ for Jupyter Notebooks

REF: https://github.com/microsoft/vscode-jupyter/wiki/Setting-Up-Run-by-Line-and-Debugging-for-Notebooks

The Run by Line and Debugging features for Python notebooks requires ipykernel v6.0.0 or greater to be installed in the notebook's kernel.

#### use Anaconda
1. Use Anaconda Navigator or an Anaconda prompt to install `ipykernel` into your desired notebook environment.
2. Close and reopen VSCode and your desired notebook. The Developer: Reload Window command works well for this.

#### use Pip
1. Open a Python terminal and 'activate' your 'desired notebook environment'.
  - T:$ `.venv\Scripts\activate`

2. Install kernel
  - if needed, upgrade pip
    T:$ `python.exe -m pip install --upgrade pip`
  - Then, install kernel
    T:$ `pip install -U ipykernel`

3. Close and re-open VS Code and your desired notebook. 
  - The Developer: Reload Window command works well for this.
---

## C. Start to write code

Demo: Test to assign the same variable twice, it simply changes values.

```python
test = 3
test = "cheese"
print(test)
```

- Install package needed ➜ Writes to venv

#### Run & Debug your Python file

- Run the program:
  - by clicking button (>):
    - 'Run Python File' /
    - 'Run Current File in Interactive Window' => Jupyter style
  - or using terminal command > T: `python main-test1.py`

#### Next, Deactivate virtual env (venv) after running the script

- terminal command ➜ T: `deactivate`
- `venv` will be deactivated, and terminal prompt will return to normal

---
