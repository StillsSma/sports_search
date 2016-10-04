import psycopg2

connection = psycopg2.connect("dbname=we_like_sports")

cursor = connection.cursor()

cursor.execute("SELECT * FROM corn_huskers")
results = cursor.fetchall()

print("Welcome to Sports!")


def search():

    name = input("Search for player by first and last name: ")
    print (name)
    cursor.execute("SELECT * FROM corn_huskers where Player = %s", [name])
    results = cursor.fetchall()
    print(results)

def menu():
    choice = input("Would you like to search[s] or add new data[a]? ")

    if choice == 's':
        search()
    elif choice == 'a':
        add_data()
    else:
        print("come again?")
        menu()

def add_data():
    new_row = []
    data_fields = ["player","ATT","YDS","AVG","TD"]
    for items in data_fields:
        new_row.append(input("add {} ".format(items)))
    cursor.execute("INSERT INTO corn_huskers VALUES (%s, %s, %s, %s, %s)",
    (new_row[0], new_row[1], new_row[2], new_row[3], new_row[4]))

menu()




connection.commit()
cursor.close()
connection.close()
