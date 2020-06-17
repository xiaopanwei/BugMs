from flask import Blueprint, render_template, url_for, redirect, session, request
from flask_login import login_required

from dao import bugdao

bugsearch = Blueprint("bugsearch", __name__, static_folder="static",template_folder="template", url_prefix="/bugsearch")


@bugsearch.route("/<content>")
@login_required
def dosearch(content):
    username = session.get('name')
    if content=="0":
        buglist=[]
    else:
        buglist=bugdao.search(content)
    return render_template("bugsearch.html",username=username,buglist=buglist)

@bugsearch.route("/search", methods=['POST'])
@login_required
def search():
    content = request.form.get('content')
    return redirect(url_for('bugsearch.dosearch',content=content))
