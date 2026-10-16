# Employee Manager
# Employee Manager

## Purpose

Employee Manager is a beginner-friendly Python project that demonstrates modules, packages, JSON file storage, virtual environments, and Git version control.

## Features

- List employees in a formatted Rich table
- Add new employees
- Validate salary and email inputs
- Store employee records in JSON
- Generate department headcount and average salary reports



## How to run
create new folder open terminal and run below commands one by one:-
- clone this repo - git clone https://github.com/Suraj-Kolhe-2003/empmgr-project.git
- create virtual environment -  python -m venv .venv
- active virtual environment - .venv\Scripts\activate
- install all require pacakges - pip install -r requirements.txt
- run this project - python -  m empmgr.cli

## Usage

Activate the virtual environment, install dependencies from `requirements.txt`, and run the application from the project root:

```bash
python -m empmgr.cli
```





## Purpose
A beginner-friendly Python project for managing employee records using modules, packages, JSON storage, and Git.

## Project Structure
- `empmgr/models.py` — Creates employee records
- `empmgr/validators.py` — Validates user input
- `empmgr/storage.py` — Loads and saves employee data
- `empmgr/cli.py` — Displays the menu and handles user interaction
- `empmgr/report.py` — Generates department summaries
- `empmgr/__init__.py` — Exports public functions
- `data/employees.json` — Stores sample employee data


# history
(.venv) PS C:\Users\DEEL\Desktop\empmgr-project> git log --oneline --graph --all
* 08fba81 (HEAD -> main, origin/main) emp manager project main branch
* c66c3af (origin/feature/readme-polish, origin/HEAD, feature/readme-polish) Polish README documentation
* dc91064 (feature/report) Add department headcount and salary report
* b264b63 (feature/validation) Add project documentation and sample employee data
* 0c9b58f Add gitignore for Python project
