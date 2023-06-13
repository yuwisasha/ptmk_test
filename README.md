# PTMK TEST TASK 

## Python 3.11.3 + PostgreSQL 15.1:

### Run:
1. Change config.py:
* Create a db named "ptmk"
* put your data
2. run program via terminal:
```
git clone https://github.com/yuwisasha/ptmk_test.git
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python myApp.py *from 1 to 5*
```
* ```1``` Creates a table with fields as fullname, birthdate, sex.
* ```2``` Put record into db ```python myApp.py Panteleev Alexandr Sergeevich 26.05.2000 Male``` for example
* ```3``` Print all records with unique fullname+birthdate sorted by fullname, prints fullname, birthdate, sex, years
* ```4``` Generating 1.000.000 random records and 100 records with a surname starts with letter "F"
* ```5``` Print all records which has sex=Male and fullname=startswith("F")

![изображение](https://github.com/yuwisasha/ptmk_test/assets/113836827/fc6cd43c-73e7-4190-b31f-7d8d20680c08)
![изображение](https://github.com/yuwisasha/ptmk_test/assets/113836827/e8a8cb52-cfc0-44d5-9ace-d8ca27c51fd3)
