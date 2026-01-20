# med_eun3b

의약정보 관리 웹사이트 - Django + MySQL 기반의 의약품 정보 관리 시스템

## 프로젝트 개요

Django와 MySQL을 사용하여 구축된 의약품 정보 관리 웹사이트입니다. 사용자들은 의약품 정보를 검색하고, 게시판을 통해 정보를 공유할 수 있습니다.

## 주요 기능

### 1. 회원 관리 (accounts 앱)
- 회원가입
- 로그인/로그아웃
- 회원정보 수정

### 2. 게시판 (board 앱)
- 게시글 목록 (페이징 포함)
- 게시글 작성 (로그인 필요)
- 게시글 보기/수정/삭제 (작성자만 가능)

### 3. 의약정보 (medicines 앱)
- 성분별 검색
- 회사별 검색
- 효능별 검색
- 약품 상세정보 보기
- 관련 제품 추천

### 4. 정적 페이지 (pages 앱)
- 홈 페이지
- About Us (회사 소개)

## 기술 스택

- **Backend**: Django 4.2
- **Database**: SQLite3 (개발), MySQL (운영)
- **Frontend**: Django Templates, Bootstrap 5
- **인증**: Django Authentication System

## 설치 방법

### 1. 저장소 클론

```bash
git clone https://github.com/ywhcho/med_eun3b.git
cd med_eun3b
```

### 2. 가상환경 생성 및 활성화

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. 패키지 설치

```bash
pip install -r requirements.txt
```

### 4. 데이터베이스 설정

#### SQLite3 사용 (기본 설정)
추가 설정 불필요. 바로 마이그레이션을 실행하세요.

#### MySQL 사용 (운영 환경)

1. MySQL 서버에 데이터베이스 생성:
```sql
CREATE DATABASE med_eun3b CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'your_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON med_eun3b.* TO 'your_user'@'localhost';
FLUSH PRIVILEGES;
```

2. `config/settings.py`의 DATABASES 설정을 MySQL로 변경:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'med_eun3b',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}
```

3. mysqlclient 설치:
```bash
pip install mysqlclient
```

### 5. 마이그레이션 실행

```bash
python manage.py migrate
```

### 6. 관리자 계정 생성

```bash
python manage.py createsuperuser
```

### 7. 샘플 데이터 로드 (선택사항)

```bash
python manage.py load_sample_medicines
```

### 8. 개발 서버 실행

```bash
python manage.py runserver
```

브라우저에서 `http://127.0.0.1:8000` 접속

## 프로젝트 구조

```
med_eun3b/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── config/                 # 프로젝트 설정
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/               # 회원 관리
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── board/                  # 게시판
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── medicines/              # 의약정보
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── management/
│       └── commands/
│           └── load_sample_medicines.py
├── pages/                  # 정적 페이지
│   ├── views.py
│   ├── urls.py
│   └── templates/
└── templates/              # 공통 템플릿
    └── base.html
```

## 관리자 페이지

관리자 페이지 접속: `http://127.0.0.1:8000/admin`

관리자 페이지에서 다음을 관리할 수 있습니다:
- 사용자 관리
- 게시글 관리
- 의약품 정보 관리

## 보안 기능

- CSRF 보호
- 비밀번호 해싱 (Django 기본 제공)
- SQL Injection 방지 (Django ORM 사용)
- 권한 기반 접근 제어
- 로그인 필요 기능 보호 (`@login_required`)

## 개발 가이드

### 의약품 데이터 추가

1. 관리자 페이지를 통해 수동 추가
2. Django shell을 통해 추가:
```python
python manage.py shell
from medicines.models import Medicine

Medicine.objects.create(
    약품명='약품명',
    성분명='성분명',
    효능='효능 설명',
    용량='용량',
    주의사항='주의사항',
    회사명='회사명'
)
```

### 커스텀 관리 명령어

샘플 데이터 로드:
```bash
python manage.py load_sample_medicines
```

## 라이선스

이 프로젝트는 교육 목적으로 작성되었습니다.

## 문의

- 이메일: info@med-eun3b.com
- GitHub Issues: https://github.com/ywhcho/med_eun3b/issues
