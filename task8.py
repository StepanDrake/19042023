# Task 8
username = input('your nickname is(only letters):')
password = input('your password is:')
contains_username_only_letters = username.isalpha()
contains_password_only_digidts_letters = password.isalnum()

if contains_username_only_letters and contains_password_only_digidts_letters:

    confirm_pass = input('confirm password:')
    if password == confirm_pass:
        print('You are succesfully login')
        print('The user is disconnected due to the whims of the teacher')

        username_again_login = str(input('your nickname is(only letters):'))
        password_again_login = str(input('your password is:'))
        if password_again_login == password and username_again_login == username:
            print('You are succesfully login')
        else:
            print('')
    else:
        print('password incorrect')
else:
    print('login or password incorrect')
