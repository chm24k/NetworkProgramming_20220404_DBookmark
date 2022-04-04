# DBookmark
___
###Django 호출 순서2, 개발 순서
- project/urls.py -> app/urls.py -> views.py -> models.py -> templates/app/index.html
- admin.py : 관리자 사이트
- form.py : 입력 사이트 
- 개발 순서 : models.py , views.py , urls.py , templates
###하단 설명 참고
1. startproject DBookmark
   1. python -m pip install django~=3.2  (Django설치)
   2. django-admin startproject DBookmark .
   3. python .\manage.py runserver