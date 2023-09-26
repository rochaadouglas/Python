def cousin_number(number):
    value = number
    count = 1
    cousin = 0
    while count <= value:
        if value % count == 0:
            cousin = cousin + 1
        count += 1
    if cousin == 2:
        return True
    else:
        return False

print(f'{cousin_number(10)}')