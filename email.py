email = input("write your email:")
k,j,d = 0,0,0
if len(email) >= 6:
    if email[0].isalpha():
        if '@' in email and email.count('@') == 1:
            if email[-4] or email[-3] == '.':
                for i in email:
                    if i == i.isspace():
                        k = 1
                    if k == 1:
                        print('Invalid email')
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                        elif i.isdigit():
                            continue
                        elif i == '_' or i == '.' or i == '@':
                            continue
                    if k==1 or j==1 or d==1:
                        print('nope')
                else:
                    d = 1
            else:
                print("Wrong email")
        else:
            print('incorrect email!')
    else:
        print('email should start with alphabet')
else:
    print("characters in email should be greater 5")
