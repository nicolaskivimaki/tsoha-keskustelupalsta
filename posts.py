from db import db
from messages import *
from users import *

def get_post(post_id):
    sql = 'select p.id, p.title, p.content, p.sent_at, p.user_id, u.username from posts p, users u where p.id=:post_id and u.id=p.user_id'
    return db.session.execute(sql, {'post_id':post_id}).fetchone()