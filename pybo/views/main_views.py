from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

# main = Blueprint 별칭, __name__ = 모듈명인 main_views
bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/bp')
def ding():
    return redirect(url_for('_Question._list'))

@bp.route('/')
def index():
    return render_template('main/index.html')
