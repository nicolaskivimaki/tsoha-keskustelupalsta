from db import db
from users import *

def get_comments(post_id):
    sql = "select c.comment, u.username, c.sent_at from comments c, users u where c.post_id=:post_id and c.user_id=u.id order by c.id"
    result = db.session.execute(sql, {"post_id":post_id})
    return result.fetchall()

def new_comment(comment, post_id):
    user_id = get_user_id()
    if user_id == 0:
        return False
    sql = "insert into comments (comment, user_id, post_id, sent_at) values (:comment, :user_id, :post_id, now())"
    db.session.execute(sql, {"comment":comment, "user_id":user_id, "post_id":post_id})
    db.session.commit()
    return True