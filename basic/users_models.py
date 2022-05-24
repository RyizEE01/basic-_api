from db import get_db

def get_users():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, username, password, students_id FROM tbl_users"
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    result = []
    
    for row in cursor.fetchall():
        result.append(dict(zip(columns, row)))

    return result


def get_users_by_id(id):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, username, password, students_id FROM tbl_users WHERE id = ?"
    cursor.execute(query, [id])
    columns = [column[0] for column in cursor.description]
    result = []
    result.append(dict(zip(columns, cursor.fetchone())))

    return result


def insert_users(username, password, students_id):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO tbl_users(username, password, students_id) VALUES (?, ?, ?)"
    cursor.execute(query, [username, password, students_id])
    db.commit()

    return True


def update_users(id, username, password, students_id):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE tbl_users SET username = ?, password = ?, students_id = ? WHERE id = ?"
    cursor.execute(query, [username, password, students_id, id])
    db.commit()

    return True


def delete_users(id):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM tbl_users WHERE id = ?"
    cursor.execute(query, [id])
    db.commit()

    return True

def get_users_all_join():
    db = get_db()
    cursor = db.cursor()

    query = "SELECT * FROM tbl_users LEFT JOIN tbl_students ON tbl_users.students_id = tbl_students.id"
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    result = []
    
    for row in cursor.fetchall():
        result.append(dict(zip(columns, row)))

    return result

def get_users_by_id_join(students_id):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM tbl_users LEFT JOIN tbl_students ON tbl_users.students_id = tbl_students.id WHERE students_id = ?"
    cursor.execute(query, [students_id])
    columns = [column[0] for column in cursor.description]
    result = []
    result.append(dict(zip(columns, cursor.fetchone())))
        
    return result
