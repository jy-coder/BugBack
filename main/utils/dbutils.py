import psycopg2
import os
from dotenv import load_dotenv, find_dotenv
import string
import random





domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
letters = string.ascii_lowercase[:12]

def get_random_domain(domains):
    return random.choice(domains)

def get_random_name(letters,length):
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_emails(nb, length):
    return [get_random_name(letters, length) + '@' + get_random_domain(domains) for i in range(nb)]


def generate_random_name(nb, length):
  return [get_random_name(letters, length)  for i in range(nb)]


load_dotenv(find_dotenv())



conn = psycopg2.connect(host='localhost',database='bugapp',
                        user='myprojectuser', password='123456')

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



def init_role():
    gen_email = generate_random_emails(10, 5)
    gen_name = generate_random_name(10,5)
    print(gen_email,gen_name)







def test_data():
    one_role = "INSERT INTO roles VALUES(1 , 'developer');"
    # one_user = "INSERT INTO users VALUES(1,'username','123@gmail.com',1);"

    # one_role = "delete from roles where id=1;"
    # one_user= "delete from users where id=1;"

    cur.execute(one_role)
    # cur.execute(one_user)


# cur.execute(create_user_table)
# cur.execute(create_bugs)
# print("user table Created....")
# cur.execute(create_bugs)
# print("bug table Created....")
# create_tables()
# drop_all_tables()
# init_role()
test_data()
conn.commit()
conn.close()