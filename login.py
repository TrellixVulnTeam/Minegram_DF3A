import instaloader


class Login:
    __slots__ = ['_user', '_password']

    def __init__(self, user, password):
        self._user = user
        self._password = password

    def check_login(self):
        test_log = instaloader.Instaloader()
        try:
            test_log.login(self._user, self._password)
            test_log.close()
            return True
        except(instaloader.ConnectionException, instaloader.BadCredentialsException):
            return False
