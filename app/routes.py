from flask import Flask, flash, Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Post, User
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@bp.route('/post1')
def index1():
    posts = Post.query.all()
    return render_template('post1.html', posts=posts)

@bp.route('/post2')
def index2():
    posts = Post.query.all()
    return render_template('post2.html', posts=posts)

@bp.route('/post3')
def index3():
    posts = Post.query.all()
    return render_template('post3.html', posts=posts)

@bp.route('/post4')
def index4():
    posts = Post.query.all()
    return render_template('post4.html', posts=posts)

@bp.route('/post5')
def index5():
    posts = Post.query.all()
    return render_template('post5.html', posts=posts)

@bp.route('/post6')
def index6():
    posts = Post.query.all()
    return render_template('post6.html', posts=posts)

@bp.route('/post7')
def index7():
    posts = Post.query.all()
    return render_template('post7.html', posts=posts)

@bp.route('/post8')
def index8():
    posts = Post.query.all()
    return render_template('post8.html', posts=posts)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # 이메일로 사용자 검색
        user = User.query.filter_by(email=email).first()

        # 이메일이 없는 경우
        if not user:
            return "<script>alert('입력하신 ID가 존재하지 않습니다. ID를 다시 입력해 주세요'); window.location.href='/login';</script>"

        # 비밀번호가 일치하지 않는 경우
        if not check_password_hash(user.password, password):
            return "<script>alert('비밀번호가 일치하지 않습니다!'); window.location.href='/login';</script>"

        # 로그인 성공 시 after_mainpage.html로 이동
        return redirect(url_for('main.afterindex'))

    return render_template('login.html')

@bp.route('/afterindex')
def afterindex():
    return render_template('afterindex.html')

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # 중복 이메일 확인
        user = User.query.filter_by(email=email).first()
        if user:
            flash('이미 존재하는 사용자입니다!', 'warning')  # 메시지를 flash로 설정
            return redirect(url_for('main.signup'))  # 다시 signup 페이지로 리다이렉트
        
        # 비밀번호 해싱 후 저장
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        # 성공적으로 회원가입 시 login 페이지로 리다이렉트
        flash('회원가입이 성공적으로 완료되었습니다!', 'success')
        return redirect(url_for('main.login'))

    return render_template('signup.html')

@bp.route('/aboutwe')
def aboutwe():
    posts = Post.query.all()
    return render_template('aboutwe.html', posts=posts)