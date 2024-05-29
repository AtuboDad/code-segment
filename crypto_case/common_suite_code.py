import hashlib


from werkzeug.security import generate_password_hash, check_password_hash

key = 'BFEBFBFF000A0671'

passwd = 'BFEBFBFF000A0671'

sh = hashlib.sha256()

sh.update((key + '_' + passwd + '_' + passwd).encode())

res = sh.hexdigest()
encty_word = str(res)

result = generate_password_hash(encty_word)
encty_result = hashlib.md5(bytes(result, 'utf-8')).hexdigest()
print('E' + encty_result.upper() + 'C')

flag = check_password_hash('pbkdf2:sha256:260000$mFOKivMGifE9i36L$78dd626412cab829e93acd84043a11edaf26095c5956f4e00c9f80cf7563771c', encty_word)
print(flag)