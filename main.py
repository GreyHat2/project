import DB as d
import encrypt1 as e



def data():
    # d.createdb()
    name = input("Enter a name: ")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    d.insertdb(name, username, password)

def create():
    d.createdb()

def delete():
    id = int(input("Enter id: "))
    d.delete(id)

def main():
    com = input("Get help (h) or enter a command: ").lower()

    if com == "h":
        print("""    ##Commmands##
    >Create a database(c)
    >Delete a row(d)
    >Lock database(l)
    >Unlock database(o)
    >Show data(s)
    >Add data(a)
    >Quit(q)
        """)
        main()
    elif com == "l":
        e.encrypt("data.db")
    
    elif com == "o":
        ID = input("Enter database name: ") 
        key = input("Enter the key: ")
        e.decrypt(key, ID)

    elif com == "c":
        d.createdb()
        main()
    elif com == "d":
        id = input("Enter ID: ")
        d.delete(id)
        main()
    elif com == "s": 
        d.fetchall()
        main() 
    elif com == "a":
        data()
        main()
    elif com == "q":
        quit()
    else:
        print("Invalid option")
        main()

if __name__ == '__main__':
    main()
