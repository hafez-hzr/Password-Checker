def check_password(pw):
    if len(pw) < 6:
        return f'{pw} ---------- Weak ---------- Less than 6 Characters\n'
    elif pw.isupper():
        return f'{pw} ---------- Weak ---------- All Upper Case\n'
    elif pw.islower():
        return f'{pw} ---------- Weak ---------- All Lower Case\n'
    elif pw.isnumeric():
        return f' {pw} ---------- Weak ---------- All Numerical\n'
    else:
        for j in common_words:
            if j in pw:
                return f'{pw} ---------- Weak ---------- contains {j}\n'
        else:
            return f'{pw} ---------- Strong ---------- \n'

n = int(input("Enter the Number of Passwords: "))
m = int(input("Enter the Number of Common Words: "))
passwords, common_words = [], []
passwords += [input(f'Enter the  Password {i+1}: ') for i in range(n)]
common_words += [input(f'Enter the Common Word {i+1} : ') for i in range(m)]

print('Password----------Strong/Weak----------Remarks\n'
      '----------------------------------------------')
for i in passwords:
    print(check_password(i))