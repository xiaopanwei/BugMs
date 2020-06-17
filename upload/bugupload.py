from flask import Blueprint, render_template, url_for, redirect, request, session
from flask_login import login_required

from dao import bugdao

bugupload = Blueprint("bugupload", __name__, static_folder="static",template_folder="template", url_prefix="/bugupload")


@bugupload.route("/")
@login_required
def index():
    once=1
    username = session.get('name')
    return render_template("bugupload.html",once=once,username=username)

@bugupload.route("/once")
@login_required
def once():
    once=0
    username = session.get('name')
    return render_template("bugupload.html",once=once,username=username)

@bugupload.route("/upload/<once>",methods=['POST'])
@login_required
def upload(once):
    bug_introduce = request.form.get('introduce')
    product = request.form.get('product')

    product_version = request.form.get('productversion')
    system_version = request.form.get('systemversion')
    system = request.form.get('system')
    systemmodel= request.form.get('systemmodel')
    bug_details = request.form.get('details')
    feedbackpeople = request.form.get('feedbackpeople')

    bugdao.upload(bug_introduce, product, product_version, system_version, system, bug_details, systemmodel,feedbackpeople)
    if int(once)==1:
        return redirect(url_for('bugupload.index'))
    else:
        return redirect(url_for('buglist.index',page=1))




