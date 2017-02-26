__author__ = 'Noel'

class UserProfile:

    def __init__(self, name = "", screen_name = "", user_id = "", profile_picture_link = "", on_block_list = ""):
        self.name = name
        self.screen_name = screen_name
        self.user_id = user_id
        self.profile_picture_link = profile_picture_link
        self.on_block_list = on_block_list

    def __str__(self):
        return self.name + " : " + self.screen_name + " : " + self.user_id + " : " + self.profile_picture_link
