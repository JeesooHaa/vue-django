student@M702 MINGW64 ~/development/vue_django
$ mkdir todo-back

student@M702 MINGW64 ~/development/vue_django
$ cd todo-back

student@M702 MINGW64 ~/development/vue_django/todo-back
$ python -V
Python 3.5.3

student@M702 MINGW64 ~/development/vue_django/todo-back
$ venv
(3.7.4)
student@M702 MINGW64 ~/development/vue_django/todo-back
$ python -V
Python 3.7.4
(3.7.4)
student@M702 MINGW64 ~/development/vue_django/todo-back
$ python -m venv venv
(3.7.4)
student@M702 MINGW64 ~/development/vue_django/todo-back
$ source venv/Scripts/activate
(venv)
student@M702 MINGW64 ~/development/vue_django/todo-back
$ python -V
Python 3.7.4
(venv)
student@M702 MINGW64 ~/development/vue_django/todo-back
$ pip list
Package    Version
---------- -------
pip        19.0.3
setuptools 40.8.0
You are using pip version 19.0.3, however version 19.3.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
(venv)
student@M702 MINGW64 ~/development/vue_django/todo-back
$ python -m pip install --upgrade pip
Collecting pip
  Using cached https://files.pythonhosted.org/packages/00/b6/9cfa56b4081ad13874b0c6f96af8ce16cfbc1cb06bedf8e9164ce5551ec1/pip-19.3.1-py2.py3-none-any.whl
Installing collected packages: pip
  Found existing installation: pip 19.0.3
    Uninstalling pip-19.0.3:
      Successfully uninstalled pip-19.0.3
Successfully installed pip-19.3.1
(venv)
student@M702 MINGW64 ~/development/vue_django/todo-back
$ pip list
Package    Version
---------- -------
pip        19.3.1
setuptools 40.8.0
(venv)
student@M702 MINGW64 ~/development/vue_django/todo-back
$ pip install django
Collecting django
  Downloading https://files.pythonhosted.org/packages/a0/36/463632a2e9161a7e713488d719a280e8cb0c7e3a66ed32a32e801891caae/Django-2.2.7-py3-none-any.whl (7.5MB)
     |████████████████████████████████| 7.5MB 930kB/s
Collecting pytz
  Using cached https://files.pythonhosted.org/packages/e7/f9/f0b53f88060247251bf481fa6ea62cd0d25bf1b11a87888e53ce5b7c8ad2/pytz-2019.3-py2.py3-none-any.whl
Collecting sqlparse
  Using cached https://files.pythonhosted.org/packages/ef/53/900f7d2a54557c6a37886585a91336520e5539e3ae2423ff1102daf4f3a7/sqlparse-0.3.0-py2.py3-none-any.whl
Installing collected packages: pytz, sqlparse, django
Successfully installed django-2.2.7 pytz-2019.3 sqlparse-0.3.0
(venv)
student@M702 MINGW64 ~/development/vue_django/todo-back
$ pip list
Package    Version
---------- -------
Django     2.2.7
pip        19.3.1
pytz       2019.3
setuptools 40.8.0
sqlparse   0.3.0
(venv)
student@M702 MINGW64 ~/development/vue_django/todo-back
$ django-admin startproject todoback .
(venv)
student@M702 MINGW64 ~/development/vue_django/todo-back
$ deactivate

student@M702 MINGW64 ~/development/vue_django/todo-back
$ python -V
Python 3.5.3

student@M702 MINGW64 ~/development/vue_django/todo-back
$ cd ..

student@M702 MINGW64 ~/development/vue_django
$ vue --version
@vue/cli 4.0.5

student@M702 MINGW64 ~/development/vue_django
$ node --version
v12.13.0

student@M702 MINGW64 ~/development/vue_django
$ npm --version
6.12.0

student@M702 MINGW64 ~/development/vue_django
$ vue create todo-front

student@M702 MINGW64 ~/development/vue_django/todo-front (master)
$ rm -rf .git

student@M702 MINGW64 ~/development/vue_django/todo-front (master)
$ vue ui

student@M702 MINGW64 ~/development/vue_django/todo-front (master)
$ npm i bootstrap bootstrap-vue

student@M702 MINGW64 ~/development/vue_django/todo-front (master)
$ npm i axios

CORS...

student@M702 MINGW64 ~/development/vue_django/todo-back (master)
$ pip install djangorestframework

student@M702 MINGW64 ~/development/vue_django/todo-back (master)
$ pip install djangorestframework-jwt

student@M702 MINGW64 ~/development/vue_django/todo-back (master)
$ pip install django-cors-headers

access token : 접근할 때 사용
refresh token : access token 요청시 같이 발행 

jwt.io

토큰을 가지고 있다 => 로그인이 되어 있는 상태이다. 
세션 스토리지, 로컬 스토리지, 토큰 

student@M702 MINGW64 ~/development/vue_django/todo-front (master)
$ npm install vue-session

조건부 렌더링 ! 