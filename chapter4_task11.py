def decorator(func):
    def wrapper():
        try:
            result = func()
        except TypeError as e:
            e = str(e).split('\'')

            if e[1] == 'new_password':
                raise 'Вы не вели новый пароль!'

            elif e[1] == 'input_username':
                raise'Вы не вели имя пользывателя!'
                
    return wrapper

class User:
    username = 'Mederbek'
    password = 'qwerty'

    def get_account_balance(self, input_username):
        self.input_username = input_username

    def change_password(self, new_password):
        self.new_password = new_password

        self.password = new_password

@decorator
def main():
    u = User()

    u.change_password()
    u.get_account_balance()

if __name__ == '__main__':
    main()
