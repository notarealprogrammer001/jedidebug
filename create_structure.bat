@echo off
REM Windows batch script to create the jedidebug project structure
REM Run this from the jedidebug/ top folder

echo Creating jedidebug project structure...

REM Create root level files
echo Creating root level files...
type nul > LICENSE
type nul > README.md
type nul > pyproject.toml
type nul > setup.py
type nul > .gitignore

REM Create main package directory and files
echo Creating main package directory and files...
mkdir jedidebug
type nul > jedidebug\__init__.py
type nul > jedidebug\core.py
type nul > jedidebug\quotes.py
type nul > jedidebug\handlers.py

REM Create examples directory and files
echo Creating examples directory and files...
mkdir examples
type nul > examples\example.py

REM Create tests directory and files
echo Creating tests directory and files...
mkdir tests
type nul > tests\__init__.py
type nul > tests\test_jedidebug.py

REM Create a git setup script
echo Creating git setup script...
type nul > git_setup.bat
echo @echo off > git_setup.bat
echo REM Script to initialize git repository >> git_setup.bat
echo git init >> git_setup.bat
echo git remote add origin https://github.com/notarealprogrammer001/jedidebug >> git_setup.bat
echo git add . >> git_setup.bat
echo git commit -m "Initial commit with correct structure" >> git_setup.bat
echo git push -u origin master >> git_setup.bat

echo.
echo Project structure created successfully!
echo.
echo Directory structure:
echo jedidebug\
echo ├── LICENSE
echo ├── README.md
echo ├── pyproject.toml
echo ├── setup.py
echo ├── .gitignore
echo ├── git_setup.bat
echo ├── jedidebug\
echo │   ├── __init__.py
echo │   ├── core.py
echo │   ├── quotes.py
echo │   └── handlers.py
echo ├── examples\
echo │   └── example.py
echo └── tests\
echo     ├── __init__.py
echo     └── test_jedidebug.py
echo.
echo You can now populate these files with content.
echo To initialize the git repository, run: git_setup.bat