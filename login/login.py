from flask import Blueprint, render_template, session
from flask_login import login_user

from User import User, addusers
from dao import bugdao

login = Blueprint("login", __name__, static_folder="static", template_folder="template", url_prefix="/login")


@login.route("/login")
def index():
    return render_template("login.html", ss="display:none;")


@login.route("/loginResult/<name>/<pwd>", methods=['POST'])
def dologinResult(name, pwd):
    if int(bugdao.find_user_by_name(name)) > 0:
        if bugdao.find_pwd_by_name(name) == pwd:
            curr_user = User()
            addusers({'id': name, 'username':name, 'password': pwd})
            curr_user.id = name
            session['name']=name
            # 通过Flask-Login的login_user方法登录用户
            login_user(curr_user)

            return '{"state":0,"msg":"账号密码正确"}'
        else:
            return '{"state":1,"msg":"密码不正确"}'
    else:
        return '{"state":2,"msg":"账号不存在"}'
