class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError('The username must be between 5 and 15 characters long.')
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if self.is_len(value) and self.is_upper_in(value) and self.is_digit_in(value):
            self.__password = value
            return
        raise ValueError(
            'The password must be at least 8 or more characters long with at least 1 digit and 1 uppercase letter.')

    def is_len(self, password):
        return len(password) >= 8

    def is_upper_in(self, password):
        upper_letters = [ch for ch in password if ch.isupper()]
        return True if upper_letters else False

    def is_digit_in(self, password):
        digits = [ch for ch in password if ch.isdigit()]
        return True if digits else False

    def __str__(self):
        return f'you have a profile with username {self.username} and password: {"*" * len(self.password)}'


# invalid_name = Profile('asd', 'password')
# invalid_name.username = 'few'
invalid_password = Profile('asdfew', 'Mypassword3')
invalid_password.password = ''
