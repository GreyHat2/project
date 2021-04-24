from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

def encrypt(ID):
    # Encrypting the file with the Fernet key
    print("This is your unique key please save it: "+str(key.decode("utf-8")))
    f = Fernet(key)
    filename = ID
    with open(filename, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, 'wb') as file:
        file.write(encrypted_data)

    # Writing the Fernet key to a file(key.txt)
    s = str(key.decode("utf-8"))
    with open("key.txt", "w") as f:
        f.write(s)

def decrypt(key, ID):
    f = Fernet(key)
    filename = ID
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrtpted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrtpted_data)     

