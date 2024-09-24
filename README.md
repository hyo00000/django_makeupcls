# django_makeupcls

***
## DAY1. 환경세팅
(git repository 생성 - README.md까지)


### 1. 가상환경 설정
   ```
   <venv>
   1.가상환경 생성
   python -m venv .venv 
   2.가상환경 활성화
   source .venv/bin/activate
   3.비활성화
   deactivate
   <pyenv>
   1.가상환경 생성
   pyenv virtualenv 3.12.5 myenv
   2.가상환경 활성화
   pyenv local myenv (ls -al : .python-version파일 생성(.gitignore))
   * 가상환경 경로
   Users > 로그인하는 유저 > .pyenv > versions > 폴더명 > bin > python
   <poetry>
   1.poetry 프로젝트 초기화
   poetry init
   2.가상환경 활성화
   poetry shell
   3.의존성 관리(django 설치)
   poetry add django
   4.django 프로젝트 생성
   django-admin startproject config .
   ```
   -> interpreter settings에서 설정 잡기
   -> settings/language&framework/django 에서 폴더별 폴더위치, settings.py, manage.py경로 잡기
   
### 2.settings.py 분리 (dev용/prod용)
    ->보안: 배포용 설정에서는 SECRET_KEY, DB_PASSWORD, DEBUG_MODE설정등 민감한 정보를 보호(배포시 DEBUG=False)
    ->코드 중복을 줄이고 유지보수를 용이하게 함
```
django_makeup/
├── config/
│   ├── settings/
│   │   ├── base.py    # 기본 공통 설정
│   │   ├── local.py   # 개발 환경 설정
│   │   ├── prod.py    # 배포 환경 설정
│   │   ├── settings.py  # settings를 로드하는 파일 (바로가기 역할)
                          -> cd config/settings
                          -> ln -sf local.py setting.py (심볼릭 링크 파일 생성)
* python manage.py runserver 실행 가능 해야 함
```

### 3. base.py 설정
   - BASE_DIR 경로 확인 
   - DEBUG, ALLOWED_HOSTS -> 삭제(개발용, 배포용에 나눠서 분리함)
   - INSTALLED_APPS 분리
   - DATABASE 변경 (python-dotenv라이브러리 사용(.env를 간편하게 로드하여 python 애플리케이션을 사용할 수 있게 함))
     -> postgresql 변경 시
     
        -psql postgres : 관리자 접속
     
        -\du :데이터베이스의 사용자와 사용자들이 가지고 있는 권한을 보여주는 명령어
     
        -CREATE ROLE 이름 WITH LOGIN PASSWORD '원하는 비밀번호'; : 새로운 ROLE NAME 생성
     
        -CREATE DATABASE 데이터베이스 이름; : 데이터베이스 만들기
     
        -psql -U 이름 -d 데이터베이스이름 -h localhost -p 포트번호 : 만든 이름 데이터 베이스 접속
     

### 4. Git Flow 연결(main에서 실행)
   - git flow init
   - git flow feature start 브랜치이름
***
    
