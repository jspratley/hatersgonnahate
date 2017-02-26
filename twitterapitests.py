#!/usr/bin/python
from twitter import *
import userprofile

import sys

def search_twitter_profiles(t_c, name, num_results=20):
    """
    Searches for a user by name.
    :param name: the name to be searched
    :param num_results: the number of results to return, with default value of 20.
    :return: A list of UserProfile results that match the name.
    """
    user_profiles = []
    user_search_query = t_c.users.search(q=name, count=num_results)
    for user_dict in user_search_query:
        user_profiles.append(userprofile.UserProfile(user_dict["name"], user_dict["screen_name"], user_dict["id_str"],
                                                     user_dict["profile_background_image_url_https"]))
    if len(user_profiles) is 0:
        sys.stderr.write(search_twitter_profiles.__name__ + ": No user profiles found.\n")
    else:
        print("Successfully found %d profile(s) with the name %s. " % (num_results, name))
    return user_profiles


def block_twitter_profile(t_c, profile):
    """
    Attempts to block a user profile via screen name. Logs an error if this fails
    :param profile: A user profile that should be blocked for the specified account
    """
    try:
        t_c.blocks.create(screen_name=profile.screen_name)
        print("Successful Block : " + str(profile))
    except:
        sys.stderr.write(block_twitter_profile.__name__ + ": No user profiles found.\n")


"""config = {}
exec(compile(open("config.py", "rb").read(), "config.py", 'exec'), config)
twitter_config = Twitter(
    auth=OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))
profiles = search_twitter_profiles(twitter_config, "John Smith", 15)
block_twitter_profile(twitter_config, profiles[0])"""
