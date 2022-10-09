from db import db

categories = ("opiskelu", "urheilu", "rakkaus", "fanifiktio", "politiikka")

def create_categories():
    for category in categories:
        sql = 'INSERT INTO categories (category) VALUE (:category)'
        db.session.execute(sql, {'category':category})
        db.session.commit()

def get_categories_list():
    sql = "SELECT * FROM categories"
    result = db.session.execute(sql)
    return result.fetchall()