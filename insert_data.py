import sqlite3

# sqlite db 파일 생성
con = sqlite3.connect('dbdb.db')

# sql 문장을 실행시키기 위한 준비
cursor = con.cursor() 

sql = '''
INSERT INTO Person (ID, Name, Birthday)
VALUES (1, '이혜리', '1994-06-09');
'''
cursor.execute(sql) # sql 실행
con.commit() # 적용
con.close() # db닫기