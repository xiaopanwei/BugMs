# 获得所有数据
import time

from db import get_connection
from modal import bugInfo
from modal import imageInfo

def find_all(page, pageSize):
    conn = get_connection()
    limit = (int(page) - 1) * pageSize
    cursor = conn.cursor()
    sql = "select * from bug_record where flag=0  limit %s,%s"
    try:
        cursor.execute(sql, [limit, pageSize])
        bug = None
        if conn == "":
            return bug
        date = []
        for i in cursor:
            bug = bugInfo()
            bug.bug_id = i["bug_id"]
            bug.product = i["product"]
            bug.bugname = i["bugname"]
            bug.feedbacktime = i["feedbacktime"]
            bug.endtime = i["endtime"]
            bug.feedbackpeople = i["feedbackpeople"]
            bug.dealpeople = i["dealpeople"]
            bug.dealstate = i["dealstate"]
            bug.bugdetail = i["bugdetail"]
            bug.dealmethod = i["dealmethod"]
            bug.bugsystem = i["bugsystem"]
            bug.systemversion = i["systemversion"]
            bug.productsystem = i["productsystem"]
            bug.systemmodel = i["systemmodel"]
            date.append(bug)
    finally:
        conn.close()
    return date


def findbyid(bugid):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "select * from bug_record where flag=0 and bug_id=%s"
    try:
        cursor.execute(sql, bugid)
        bug = None
        if conn == "":
            return bug
        bug = bugInfo()
        for i in cursor:
            bug.bug_id = i["bug_id"]
            bug.product = i["product"]
            bug.bugname = i["bugname"]
            bug.feedbacktime = i["feedbacktime"]
            bug.endtime = i["endtime"]
            bug.feedbackpeople = i["feedbackpeople"]
            bug.dealpeople = i["dealpeople"]
            bug.dealstate = i["dealstate"]
            bug.bugdetail = i["bugdetail"]
            bug.dealmethod = i["dealmethod"]
            bug.bugsystem = i["bugsystem"]
            bug.systemversion = i["systemversion"]
            bug.productsystem = i["productsystem"]
            bug.systemmodel = i["systemmodel"]
    finally:
        conn.close()
    return bug


def count():
    """查找flag=1的数据总数"""
    count = 0
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT count(*)" \
                  " FROM bug_record " \
                  "WHERE flag=0 and dealstate!=3"
            cursor.execute(sql, ())
            for c in cursor:
                count = c['count(*)']
    finally:
        conn.close()
    return count


def upload(bug_introduce, product, product_version, system_version, system, bug_details, systemmodel,feedbackpeople):
    feedbacktime = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))

    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO bug_record (product,bugname,feedbacktime,dealstate,bugdetail,bugsystem," \
          "systemversion,productsystem,systemmodel,flag,feedbackpeople) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        cursor.execute(sql, (
            product, bug_introduce, feedbacktime, 1, bug_details, system, system_version, product_version, systemmodel,
            0,feedbackpeople))
        conn.commit()
    finally:
        conn.close()


def updata(bugid, bugname, bugdetails, dealmethod):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE bug_record SET bugname=%s,bugdetail=%s,dealmethod=%s WHERE bug_id=%s"
    try:
        cursor.execute(sql, (bugname, bugdetails, dealmethod, bugid))
        conn.commit()
    finally:
        conn.close()

def updatacontaindealpeople(bugid, bugname, bugdetails, dealmethod,dealpeople):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE bug_record SET bugname=%s,bugdetail=%s,dealmethod=%s ,dealpeople=%sWHERE bug_id=%s"
    try:
        cursor.execute(sql, (bugname, bugdetails, dealmethod,dealpeople, bugid,))
        conn.commit()
    finally:
        conn.close()

def confirm(bugid):
    print(bugid)
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE bug_record SET dealstate=2 WHERE bug_id=%s"
    try:
        cursor.execute(sql, (bugid))
        conn.commit()
    finally:
        conn.close()


def close(bugid):
    print(bugid)
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE bug_record SET dealstate=3 WHERE bug_id=%s"
    try:
        cursor.execute(sql, (bugid))
        conn.commit()
    finally:
        conn.close()


def find_user_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT count(*) FROM user WHERE name=%s"
    try:
        cursor.execute(sql, (name))
        for c in cursor:
            count = c['count(*)']
    finally:
        conn.close()
    return count

def find_pwd_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT pwd FROM user WHERE name=%s"
    try:
        cursor.execute(sql, (name))
        for c in cursor:
            pwd = c['pwd']
    finally:
        conn.close()
    return pwd


def findcountimagebybugid(bugid):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT count(*) FROM bugimage WHERE bugid=%s and flag=0"
    try:
        cursor.execute(sql, (bugid))
        for c in cursor:
            count = c['count(*)']
    finally:
        conn.close()
    return count


def findimagebybugid(bugid):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "select * from bugimage WHERE bugid=%s and flag=0"
    try:
        cursor.execute(sql, bugid)

        imageurl = []
        if conn == "":
            return imageurl
        for i in cursor:
            image= imageInfo()
            image.image_id=i["id"]
            image.image_url=i["imageurl"]
            imageurl.append( image)
    finally:
        conn.close()
    return imageurl


def insertimage(bugid, imagename):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO bugimage (bugid,imageurl) VALUES (%s,%s)"
    try:
        cursor.execute(sql, (bugid,imagename))
        conn.commit()
    finally:
        conn.close()


def finddealpeople():
    conn = get_connection()
    cursor = conn.cursor()
    sql = "select name from user WHERE type=1"
    try:
        cursor.execute(sql)
        dealpeople = []
        if conn == "":
            return dealpeople
        for i in cursor:
            dealpeople.append(i["name"])
    finally:
        conn.close()
    return dealpeople


def search(content):
    conn = get_connection()
    cursor = conn.cursor()
    args = ['%' + content + '%']
    sql = "select * from bug_record where flag=0 and bugname like %s;"
    try:
        cursor.execute(sql, args)
        bug = None
        if conn == "":
            return bug
        date = []
        for i in cursor:
            bug = bugInfo()
            bug.bug_id = i["bug_id"]
            bug.product = i["product"]
            bug.bugname = i["bugname"]
            bug.feedbacktime = i["feedbacktime"]
            bug.endtime = i["endtime"]
            bug.feedbackpeople = i["feedbackpeople"]
            bug.dealpeople = i["dealpeople"]
            bug.dealstate = i["dealstate"]
            bug.bugdetail = i["bugdetail"]
            bug.dealmethod = i["dealmethod"]
            bug.bugsystem = i["bugsystem"]
            bug.systemversion = i["systemversion"]
            bug.productsystem = i["productsystem"]
            bug.systemmodel = i["systemmodel"]
            date.append(bug)
    finally:
        conn.close()
    return date
