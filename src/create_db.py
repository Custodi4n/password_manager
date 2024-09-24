import sqlite3
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import hashlib

def create_table():
    conn = sqlite3.connect('password_manager.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL,
            password TEXT NOT NULL,
            master_password_hash TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            website TEXT NOT NULL,
            username TEXT NOT NULL,
            encrypted_password TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')

    conn.commit()
    conn.close()

def create_user(login, password, master_password):
    conn = sqlite3.connect('password_manager.db')
    cursor = conn.cursor()

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    hashed_master_password = hashlib.sha256(master_password.encode()).hexdigest()

    cursor.execute('''
        INSERT INTO users (login, password, master_password_hash)
        VALUES (?, ?, ?)
    ''', (login, hashed_password, hashed_master_password))

    user_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return user_id

def login_user(login, password):
    conn = sqlite3.connect('password_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id FROM users
        WHERE login=? AND password=?
    ''', (login, hashlib.sha256(password.encode()).hexdigest()))
    result = cursor.fetchone()
    conn.close()

    if result:
        return result
    else:
        return False

def check_master_password(user_id, entered_password):
    conn = sqlite3.connect('password_manager.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT master_password_hash FROM users
        WHERE id=?
    ''', (user_id,))

    result = cursor.fetchone()
    print(result)
    conn.close()

    if result:
        hashed_stored_password = result[0]
        hashed_entered_password = hashlib.sha256(entered_password.encode()).hexdigest()
        return hashed_entered_password == hashed_stored_password
    else:
        return False

def encrypt_password(password, key):
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(password.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CFB(b'\0' * 16), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_password = encryptor.update(padded_data) + encryptor.finalize()

    return encrypted_password

def add_password(user_id, website, username, password):
    conn = sqlite3.connect('password_manager.db')
    cursor = conn.cursor()

    key = hashlib.sha256(str(user_id).encode()).digest()
    encrypted_password = encrypt_password(password, key)

    cursor.execute('''
        INSERT INTO passwords (user_id, website, username, encrypted_password)
        VALUES (?, ?, ?, ?)
    ''', (user_id, website, username, encrypted_password))

    conn.commit()
    conn.close()

def delete_data(user_id, row_id):
    conn = sqlite3.connect('password_manager.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM passwords
    WHERE user_id=? AND id=?''', (user_id, row_id))
    row = cursor.fetchone()
    if row is None:
        conn.close()
        return

    cursor.execute('''
    DELETE FROM passwords
    WHERE user_id=? AND id=?''', (user_id, row_id))
    conn.commit()
    conn.close()
    return

def decrypt_password(encrypted_password, key):
    cipher = Cipher(algorithms.AES(key), modes.CFB(b'\0' * 16), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_password) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_password = unpadder.update(decrypted_data) + unpadder.finalize()

    return decrypted_password.decode()

def get_password(user_id, website, username):
    conn = sqlite3.connect('password_manager.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT encrypted_password FROM passwords
        WHERE user_id=? AND website=? AND username=?
    ''', (user_id, website, username))

    result = cursor.fetchone()

    conn.close()

    if result:
        encrypted_password = result[0]
        key = hashlib.sha256(str(user_id).encode()).digest()
        decrypted_password = decrypt_password(encrypted_password, key)
        return decrypted_password
    else:
        return None

def view_all_data(user_id):
    conn = sqlite3.connect('password_manager.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT website, username, encrypted_password FROM passwords
        WHERE user_id=?
    ''', (user_id,))

    results = cursor.fetchall()
    print(results)
    conn.close()
    data = []
    if results:
        for row in results:
            website, username, encrypted_password = row
            key = hashlib.sha256(str(user_id).encode()).digest()
            decrypted_password = decrypt_password(encrypted_password, key)
            data.append((website, username, decrypted_password))
    return data