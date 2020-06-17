import osfrom flask import Blueprint, render_template, session, request, jsonify, make_responsefrom flask_login import login_requiredfrom werkzeug.utils import secure_filenamefrom dao import bugdaobugdetails = Blueprint("bugdetails", __name__, static_folder="static",template_folder="template", url_prefix="/bugdetails")@bugdetails.route("/<bugid>")@login_requireddef index(bugid):    bugdetail= bugdao.findbyid(bugid)    username = session.get('name')    imageurls = bugdao.findimagebybugid(bugid)    upload_path=[]    for image in imageurls:        upload_path.append(os.path.join( '../../static/image', image))    print(upload_path)    return render_template("bugdetails.html",bugdetail=bugdetail,username=username,upload_path=upload_path)@bugdetails.route("/loadimage/<bugid>", methods=['POST'])def imageload(bugid):    if request.method == 'POST':        f = request.files['file']        if not (f and allowed_file(f.filename)):            return jsonify({"error": 1001, "msg": "请检查上传的图片类型，仅限于png、PNG、jpg、JPG、bmp"})        print(bugid)        count = bugdao.findcountimagebybugid(bugid)        imagename=bugid+"_"+((str)(count+1))+"."+f.filename.rsplit('.', 1)[1]        bugdao.insertimage(bugid,imagename)        upload_path = os.getcwd() +'/static/image/'+secure_filename(imagename)  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径        f.save(upload_path)        image_data = open(upload_path, "rb").read()        response = make_response(image_data)        response.headers['Content-Type'] = 'image/png'        print(response)        return jsonify({"error": 0, "msg": "上传图片成功"})# 设置允许的文件格式ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])def allowed_file(filename):    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS