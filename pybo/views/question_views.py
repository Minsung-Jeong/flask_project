from flask import Blueprint, render_template
from flask_project.pybo.models import Question

# _Question = Blueprint 별칭 또는 함수명, url 연결 함수명
bp = Blueprint('_Question', __name__, url_prefix='/question')

@bp.route('/list')
def _list():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)

# @bp.route('/detail/<int:question_id>/')
@bp.route('/detail/<question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)


