from flask_project.pybo.models import Question, Answer
from datetime import datetime


q = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고 싶습니다.', create_date=datetime.now())


from flask_project.pybo import db
db.session.add(q)
db.session.commit()


from datetime import datetime
from flask_project.pybo.models import Question, Answer
from flask_project.pybo import db
q = Question.query.get(2)
a = Answer(question=q, content='네 자동생성 됩니다', create_date=datetime.now())

db.session.add(a)
db.session.commit()