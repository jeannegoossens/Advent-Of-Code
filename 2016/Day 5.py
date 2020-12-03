input = 'ojvtpuvg'

from hashlib import md5

password = list('________')
i = 0
x = 0
while password.count('_') > 0:
    hashed = ''
    while hashed[:5] != '00000':
        string = input + str(i)
        hashed = str(md5(string.encode('utf-8')).hexdigest())
        i += 1
    print(password, hashed, string)
    try:
        if password[int(hashed[5])] == '_':
            password[int(hashed[5])] = hashed[6]
            x += 1
    except ValueError:
        pass
    except IndexError:
        pass

print(''.join(password))