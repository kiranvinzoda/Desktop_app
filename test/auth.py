import bcrypt

salt = '$2b$12$WXHOHMO.3CyFTUqK4SVmle'

def create_hash_passowrd(plain_text):
    plain_password = plain_text.encode('utf-8')
    salt_bytes = salt.encode('utf-8')
    hash_password = bcrypt.hashpw(plain_password, salt_bytes).decode()
    return hash_password

