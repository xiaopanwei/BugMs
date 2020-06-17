from flask import Blueprint, render_template, url_for, redirect, session
from flask_login import login_required

from dao import bugdao

buglist = Blueprint("buglist", __name__, static_folder="static",template_folder="template", url_prefix="/buglist")


@buglist.route("/<page>")
@login_required
def index(page):
    pageSize = 10
    buglist= bugdao.find_all(page, pageSize)
    count= bugdao.count()
    username = session.get('name')
    return render_template("buglist.html",buglist=buglist,count=count,pageSize=pageSize,page=int(page),username=username)

@buglist.route("/confirm/<bugid>/<page>")
@login_required
def doconfirm(bugid,page):
    bugdao.confirm(bugid)
    return redirect(url_for('buglist.index',page=page))

@buglist.route("/close/<bugid>/<page>")
@login_required
def doclose(bugid,page):
    bugdao.close(bugid)
    return redirect(url_for('buglist.index',page=page))