from db import db
from users import *

def get_list():
    sql = "SELECT M.content, U.username, M.sent_at FROM messages M, users U WHERE M.user_id=U.id ORDER BY M.id"
    result = db.session.execute(sql)
    return result.fetchall()

def get_latest_post():
    #sql = "SELECT M.content, U.username, M.sent_at FROM messages M, users U WHERE M.id = ( SELECT MAX(id) FROM messages )"
    #sql = "SELECT MAX(id) FROM messages)"
    #result = db.session.execute(sql)
    return ["moi", "Simo", 10-22]

def new_postt(title, content, category_id):
    user_id = get_user_id()
    sql = 'insert into posts (title, content, user_id, category_id, sent_at) values (:title, :content, :user_id, :category_id, now())'
    db.session.execute(sql, {'title':title, 'content':content, 'user_id':user_id, 'category_id':category_id})
    db.session.commit()

def new_post(title, content):
    user_id = get_user_id()
    cid=4
    if user_id == 0:
        return False
    sql = "INSERT INTO posts (title, content, user_id, category_id, sent_at) VALUES (:title, :content, :user_id, :category_id, now())"
    db.session.execute(sql, {"title":title, "content":content, "user_id":user_id, "category_id":cid})
    db.session.commit()
    return True