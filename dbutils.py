import psycopg2
import os
from dotenv import load_dotenv, find_dotenv




load_dotenv(find_dotenv())
env_lst = ['HOST','USER','PORT','PASSWORD','DATABASE']
dict = {}
for item in env_lst:
    dict[item] = os.getenv(item)


conn = psycopg2.connect(host=dict['HOST'],database=dict['DATABASE'],
                        user=dict['USER'], password=dict['PASSWORD'], port=dict["PORT"])

print("Database Connected....")

cur = conn.cursor()

def create_tables():
    create_user_roles_table = "CREATE TABLE IF NOT EXISTS roles(" \
                              "role_id serial PRIMARY KEY, " \
                              "title VARCHAR (50)" \
                              ");"


    create_user_table = "CREATE TABLE IF NOT EXISTS users(" \
                        "user_id serial PRIMARY KEY, " \
                        "username  VARCHAR (50) UNIQUE, " \
                        "email VARCHAR (50) UNIQUE," \
                        "role_id INT," \
                        "FOREIGN KEY (role_id) REFERENCES roles (role_id)" \
                        ");"

    create_bugs_table = "CREATE TABLE IF NOT EXISTS bugs( " \
                  "bug_id serial PRIMARY KEY," \
                    "user_id INT," \
                    "status VARCHAR(50), " \
                    "assign_to INT, " \
                  "FOREIGN KEY (user_id) REFERENCES users (user_id), " \
                  "FOREIGN KEY (user_id) REFERENCES users (user_id)" \
                ");"
    cur.execute(create_user_roles_table)
    cur.execute(create_user_table)
    cur.execute(create_bugs_table)

    print("Tables created")


def drop_all_tables():
    drop_all_tables = "DROP TABLE users,bugs,roles"

    cur.execute(drop_all_tables)

    print("All tables dropped")


def test_data():
    one_role = "INSERT INTO roles VALUES(1 , 'developer');"
    one_user = "INSERT INTO users VALUES(1,'username','123@gmail.com',1);"

    cur.execute(one_role)
    cur.execute(one_user)


# cur.execute(create_user_table)
# cur.execute(create_bugs)
# print("user table Created....")
# cur.execute(create_bugs)
# print("bug table Created....")
# create_tables()
# drop_all_tables()
test_data()
conn.commit()
conn.close()

