from db import db
from users import *

def get_likes(post_id):
    sql = "select l.liked from likes l where l.liked=1 and l.post_id=:post_id"
    result = db.session.execute(sql, {"post_id":post_id})
    return result.fetchall()

def get_dislikes(post_id):
    sql = "select l.liked from likes l where l.liked=0 and l.post_id=:post_id"
    result = db.session.execute(sql, {"post_id":post_id})
    return result.fetchall()

def add_like(post_id):
    user_id = get_user_id()
    if user_id == 0:
        return False
    sql = "select * from likes l where l.user_id=:user_id and l.post_id=:post_id"
    result = db.session.execute(sql, {"user_id":user_id, "post_id":post_id})
    result_list = result.fetchall()
    if result_list is None:
        sql = "insert into likes (liked, user_id, post_id) values (1, :user_id, :post_id)"
        result = db.session.execute(sql, {"user_id":user_id, "post_id":post_id})
        return True
    elif result_list[1] == 1:
        sql = "delete from likes l where l.user_id=:user_id and l.post_id=:post_id"
        result = db.session.execute(sql, {"user_id":user_id, "post_id":post_id})
        return True
    else:
        sql = "update likes set liked=1 where user_id=:user_id and post_id=:post_id"
        result = db.session.execute(sql, {"user_id":user_id, "post_id":post_id})
        return True

def add_dislike(post_id):
    user_id = get_user_id()
    if user_id == 0:
        return False
    sql = "select * from likes l where l.user_id=:user_id and l.post_id=:post_id"
    result = db.session.execute(sql, {"user_id":user_id, "post_id":post_id})
    result_list = result.fetchall()
    if result_list is None:
        sql = "insert into likes (liked, user_id, post_id) values (0, :user_id, :post_id)"
        result = db.session.execute(sql, {"user_id":user_id, "post_id":post_id})
        return True
    elif result_list[1] == 0:
        sql = "delete from likes l where l.user_id=:user_id and l.post_id=:post_id"
        result = db.session.execute(sql, {"user_id":user_id, "post_id":post_id})
        return True
    else:
        sql = "update likes set liked=0 where user_id=:user_id and post_id=:post_id"
        result = db.session.execute(sql, {"user_id":user_id, "post_id":post_id})
        return True

