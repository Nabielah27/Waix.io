import sqlite3

conn = sqlite3.connect('exam_result.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS exam_result(
        id INTEGER PRIMARY KEY,
        exam_result_id TEXT,
        student_name TEXT,
        exam_score INTEGER,
        exam_subject TEXT
    )
''')

cursor.execute("INSERT INTO exam_result (exam_result_id, student_name, exam_score, exam_subject) VALUES (?, ?, ?, ?)",
               ('1234567890', 'JOhn Doe', 90, 'Math'))
cursor.execute("INSERT INTO exam_result (exam_result_id, student_name, exam_score, exam_subject) VALUES (?, ?, ?, ?)",
               ('9876543210', 'Jane Doe', 85, 'Science'))

conn.commit()
conn.close()