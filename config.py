import os


# 이 부분 체크
# BASE_DIR = os.path.dirname('PycharmProjects/pythonProject/flask_project/config.py')
# BASE_DIR = os.path.dirname('./pythonProject/flask_project/config.py')
BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

