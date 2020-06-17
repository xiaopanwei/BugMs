from flask import Blueprint, render_template, url_for, request, session
from flask_login import login_required
from werkzeug.utils import redirect

from dao import bugdao

bugadminister = Blueprint("bugadminister", __name__, static_folder="static",template_folder="template", url_prefix="/bugadminister")


@bugadminister.route("/<bugid>")
@login_required
def index(bugid):
    bugDetails= bugdao.findbyid(bugid)
    username = session.get('name')
    dealpeoplelist=bugdao.finddealpeople()
    return render_template("bugadminister.html",bugDetails=bugDetails,dealpeoplelist=dealpeoplelist,username=username)


@bugadminister.route("/updata/<bugid>",methods=['POST'])
@login_required
def doupdata(bugid):
    bugname = request.form.get('bugname')
    bugdetails = request.form.get('bugdetails')
    dealmethod = request.form.get('dealmethod')
    dealpeople = request.form.get('dealpeople')

    if dealpeople.strip()=="":
        bugdao.updata(bugid, bugname, bugdetails, dealmethod)
    else:
        bugdao.updatacontaindealpeople(bugid, bugname, bugdetails, dealmethod,dealpeople)

    return redirect(url_for('bugadminister.index',bugid=bugid))
