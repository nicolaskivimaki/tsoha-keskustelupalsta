from db import db

categories = ("opiskelu", "urheilu", "rakkaus", "fanifiktio", "politiikka")

def create_categories():
    for category in categories:
        sql = 'INSERT INTO categories (category) VALUES (:category)'
        db.session.execute(sql, {'category':category})
        db.session.commit()

def get_categories_list():
    sql = "SELECT * FROM categories"
    result = db.session.execute(sql)
    return result.fetchall()

def get_name(id):
    sql = 'SELECT * FROM categories where id=:id'
    return db.session.execute(sql, {'id':id}).fetchone()[1]

def get_posts(id):
    sql = 'select p.id, p.title, p.content, p.sent_at, p.user_id, u.username from posts p, users u where p.category_id=:category_id and p.user_id=u.id order by p.id desc'
    return db.session.execute(sql, {'category_id':id}).fetchall()