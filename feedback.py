from db import db
from users import *

def new_feedback(content):
    user_id = get_user_id()
    if user_id == 0:
        return False
    sql = "insert into feedback (content, user_id, sent_at) values (:content, :user_id, now())"
    db.session.execute(sql, {"content":content, "user_id":user_id})
    db.session.commit()
    return True

def get_feedback():
    sql = "select f.content, u.username, f.sent_at from feedback f, users u where f.user_id=u.id order by f.id"
    result = db.session.execute(sql)
    return result.fetchall()
