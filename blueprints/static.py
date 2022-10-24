from flask import Blueprint, render_template, request, redirect, url_for
from exts import mail, db
from flask_mail import Message
import string
import random
from models import EmailCpatchaModel, UserModel
from datetime import datetime
from .forms import RegisterForm

bp = Blueprint('static', __name__, url_prefix='/')


@bp.route('/contact')
def contact():
    return render_template('contact.html')


@bp.route('/index')
def index():
    return render_template('index.html')


@bp.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@bp.route('/portfolio2')
def portfolio2():
    return render_template('portfolio2.html')


@bp.route('/pricing-table')
def pricing():
    return render_template('pricing-table.html')


@bp.route('/progress')
def progress():
    return render_template('progress.html')


@bp.route('/login')
def login():
    return render_template('login.html')


@bp.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data

            user = UserModel(email=email, username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('static.login'))
        else:
            return redirect(url_for('static.register'))


@bp.route('/captcha')
def get_captcha():
    email = request.args.get('email')
    letters = string.ascii_letters + string.digits
    captcha = ''.join(random.sample(letters, 4))
    if email:
        message = Message(
            subject='邮箱测试',
            recipients=[email],
            body=f'[盘锦中录]您的注册验证码是：{captcha},请不要告诉任何人哦！'
        )
        mail.send(message)
        captcha_model = EmailCpatchaModel.query.filter_by(email=email).first()
        if captcha_model:
            captcha_model.captcha = captcha
            captcha_model.creat_time = datetime.now()
            db.session.commit()
        else:
            captcha_model = EmailCpatchaModel(email=email, captcha=captcha)
            db.session.add(captcha_model)
            db.session.commit()
        print('captcha',captcha)
        return '发送完毕'
    else:
        return '没有传递邮箱'
