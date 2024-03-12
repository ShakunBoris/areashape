# areashape

This repo is organised the way it is for the comfort of checking out test task.    
Not the deploy version.     
This dir is common dir which stores: library, tests, graphical implementation.    
It has additional requirements reflected in requirements.txt. You can try it with    

```bash
git clone https://github.com/ShakunBoris/areashape.git
pip install -r requirements.txt
py test_app.py
``` 

# **areashape library**
To install **the areashape library** and it's dependencies only 
follow the instructions in .areashape/readme.md

## Testing
- run run_tests.py it will run all tests from tests/
- run_tests.bat works only assuming it's Windows and virtual environment installed like this:
 .\.venv\Scripts\python.exe -m unittest tests
- manually one by one in tests folder run files "*_test.py" 
- ***test_app.py is dev tool***