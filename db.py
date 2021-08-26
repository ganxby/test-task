import requests
import sqlite3

req_posts = requests.get('http://jsonplaceholder.typicode.com/posts')
json_posts = req_posts.json()

req_users = requests.get('http://jsonplaceholder.typicode.com/users')
json_users = req_users.json()

#con = sqlite3.connect('db.sqlite3')
con = sqlite3.connect('dj_task/db.sqlite3')


def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM mainapp_user')
    rows = cursorObj.fetchall()

    if not rows:
        print('DB is empty!')

    for row in rows:
        print(row)

    con.commit()


def sql_delete_all_rows(con):
    cursorObj = con.cursor()

    cursorObj.execute('DELETE FROM mainapp_user')
    cursorObj.execute("delete from sqlite_sequence where name='mainapp_user' ")  #сброс ID

    cursorObj.execute('DELETE FROM mainapp_address')
    cursorObj.execute("delete from sqlite_sequence where name='mainapp_address' ")

    cursorObj.execute('DELETE FROM mainapp_company')
    cursorObj.execute("delete from sqlite_sequence where name='mainapp_company' ")

    cursorObj.execute('DELETE FROM mainapp_geo')
    cursorObj.execute("delete from sqlite_sequence where name='mainapp_geo' ")

    cursorObj.execute('DELETE FROM mainapp_post')
    cursorObj.execute("delete from sqlite_sequence where name='mainapp_post' ")

    con.commit()

    print('Done')

def sql_append_json_users(con):
    for keys in json_users:
        cursorObj = con.cursor()

        main_info = (keys['name'], keys['username'], keys['email'],
                    keys['phone'], keys['website'])
        cursorObj.execute('INSERT INTO mainapp_user(name, username, email, phone, website) '
                          'VALUES(?, ?, ?, ?, ?)', main_info)

        addr_info = (keys['address']['street'], keys['address']['suite'],
                     keys['address']['city'], keys['address']['zipcode'], keys['id'])
        cursorObj.execute('INSERT INTO mainapp_address(street, suite, city, zipcode, user_id) '
                          'VALUES(?, ?, ?, ?, ?)', addr_info)

        geo_info = (keys['address']['geo']['lat'], keys['address']['geo']['lng'], keys['id'])
        cursorObj.execute('INSERT INTO mainapp_geo(latitude, longitude, address_id) '
                          'VALUES(?, ?, ?)', geo_info)

        company_info = (keys['company']['name'], keys['company']['catchPhrase'],
                        keys['company']['bs'], keys['id'])
        cursorObj.execute('INSERT INTO mainapp_company(name, catchPhrase, bs, user_id) '
                          'VALUES(?, ?, ?, ?)', company_info)
        con.commit()


    for keys_2st in json_posts:
        cursorObj = con.cursor()
        posts_info = (keys_2st['title'], keys_2st['body'], keys_2st['userId'])
        cursorObj.execute('INSERT INTO mainapp_post(title, body, user_id) '
                            'VALUES(?, ?, ?)', posts_info)
        con.commit()


    print('Done')

print('Select an available method: ')
print('1. Users view')
print('2. Populating the database with data from JSON')
print('3. Delete database\n')

choice = input(str("--> "))

if choice == '1':
    sql_fetch(con)
elif choice == '2':
    sql_append_json_users(con)
elif choice == '3':
    sql_delete_all_rows(con)
else:
    print('Unknown command!')


input()

#sql_append_json_users(con)
#sql_delete_all_rows(con)
#sql_fetch(con)
