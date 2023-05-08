import sqlite3

print(sqlite3.version) # 버전확인

# sqlite db 파일 생성

con = sqlite3.connect('dbdb.db')
print(type(con))
cursor = con.cursor() # sql 문장을 실행시키기 위한 준비

sql = '''
CREATE TABLE "melon" (
    "rank"    INTEGER NOT NULL,
    "title"  TEXT NOT NULL,
    "artist"  TEXT NOT NULL,
    PRIMARY KEY("rank" AUTOINCREMENT)
)
'''

cursor.execute(sql) # sql 실행
con.commit() # 적용
con.close() # db닫기