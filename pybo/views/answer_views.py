from datetime import datetime
from flask import Blueprint, url_for, request, render_template
from werkzeug.utils import redirect

from flask_project.pybo import db
from flask_project.pybo.models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')


@bp.route('/create/<int:question_id>', methods=('POST',))
def create(question_id):
    question = Question.query.get_or_404(question_id)
    content = request.form['content'] #html 상에서 textarea에 설정한 name='content'
    print(request.args.get('content'), request.args.to_dict())
    answer = Answer(content=content, create_date=datetime.now())
    question.answer_set.append(answer)
    db.session.commit()
    return redirect(url_for('_Question.detail', question_id=question_id))
