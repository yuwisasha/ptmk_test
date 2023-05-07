# PTMK TEST TASK 

## Python 3.11.3 + PostgreSQL 15.1:

### Run:
Create a db named "ptmk"
and after that run program via terminal:
```
git clone https://github.com/yuwisasha/ptmk_test.git
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python myApp.py *from 1 to 5*
```

Не уверен что можно оптимизировать запрос, в клиенте psql отрабатывает за 22 миллисекунды в среднем, с выводом в консоль существенно больше соотвественно из-за вывода.