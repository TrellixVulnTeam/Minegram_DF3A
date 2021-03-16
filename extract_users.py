import instaloader
from instaloader import Instaloader


class ExtractUsers:
    def __init__(self, accont_logged, profile_to_extract):
        self.login = Instaloader.login(accont_logged._user, accont_logged._password)
        self._profile = instaloader.Profile.from_username(self.login.context, profile_to_extract)
        self._list_of_extracted = []

    def config_extract(self, number_of_users_per_comment, hard_extract=False):
        if number_of_users_per_comment == 1:
            self.get_one_follower(hard_extract)
        elif number_of_users_per_comment == 2:
            self.get_two_followers(hard_extract)
        elif number_of_users_per_comment == 3:
            self.get_three_followers(hard_extract)


    def check_profile(self):
        try:
            if self._profile.followers > 100:
                return True
            else:
                return False
        except():
            return False

    # FROM HARD EXTRACT USAGE

    def is_invalid_user(self, user):
        try:
            if (user.is_private is True) or (user.is_verified is True)\
                    or (user.is_business_account is True) or (user.followers > 2500):
                return True
        except():
            return False

    def remove_user0(self):
        try:
            if self.is_invalid_user(self._list_of_extracted[0]) is True:
                self._list_of_extracted.remove(self._list_of_extracted[0])
                return True
            else:
                return False
        except():
            return False

    def remove_user1(self):
        try:
            if self.is_invalid_user(self._list_of_extracted[1]) is True:
                self._list_of_extracted.remove(self._list_of_extracted[1])
                return True
            else:
                return False
        except():
            return False

    def remove_user2(self):
        try:
            if self.is_invalid_user(self._list_of_extracted[2]) is True:
                self._list_of_extracted.remove(self._list_of_extracted[2])
                return True
            else:
                return False
        except():
            return False

    # GET FOLLOWER(S)

    def get_list_of_followers(self):
        try:
            if self.check_profile() is True:
                for user in self._profile.get_followers():
                    self._list_of_extracted.append('@'+user.username)
                return True
            else:
                return False
        except():
            return False

    def get_one_follower(self, hard_extract=False):
        try:
            follower = []
            follower.clear()
            if hard_extract is True and self.remove_user0() is True:
                pass
            else:
                follower.append(self._list_of_extracted[0])
                self._list_of_extracted.remove(self._list_of_extracted[0])
                return follower[0]
        except():
            return False

    def get_two_followers(self, hard_extract=False):
        try:
            followers = []
            followers.clear()
            if hard_extract is True and self.remove_user0() is True or self.remove_user1() is True:
                pass
            else:
                followers.append(self._list_of_extracted[0] + ' ' + self._list_of_extracted[1])
                self._list_of_extracted.remove(self._list_of_extracted[0])
                self._list_of_extracted.remove(self._list_of_extracted[1])
                return followers[0]
        except():
            return False

    def get_three_followers(self, hard_extract=False):
        try:
            followers = []
            followers.clear()
            if hard_extract is True and self.remove_user0() is True\
                    or self.remove_user1() is True or self.remove_user2() is True:
                pass
            else:
                followers.append(self._list_of_extracted[0] + ' ' + self._list_of_extracted[1]
                                 + ' ' + self._list_of_extracted[2])
                self._list_of_extracted.remove(self._list_of_extracted[0])
                self._list_of_extracted.remove(self._list_of_extracted[1])
                self._list_of_extracted.remove(self._list_of_extracted[2])
                return followers[0]
        except():
            return False
