import bcrypt

def hash(text:str) -> str:
    text_bytes = text.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_bytes = bcrypt.hashpw(password=text_bytes, salt=salt)
    return hashed_bytes.decode('utf-8')

def verify_hash(hash_text:str, real_text:str) -> bool:
    hash_bytes = hash_text.encode('utf-8') 
    real_bytes = real_text.encode('utf-8')
    return bcrypt.checkpw(real_bytes, hash_bytes)