import tweepy
from config import credential_keys as keys
import requests
import json


def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)

    return tweepy.API(auth)


def tweet(api_arg: tweepy.API, message: str, image_path=None):
    if image_path:
        api_arg.update_status_with_media(message, image_path)
    else:
        api_arg.update_status(message)

    print("Tweeted successfully!")


def fetch_data_api(category: str):
    api_url = "https://api.api-ninjas.com/v1/quotes?category={}".format(category)
    response = requests.get(api_url, headers={'X-Api-Key': keys.quotes_api_key})

    if response.status_code == requests.codes.ok:
        data = response.text
        data_json = json.loads(data)
        data_dict = data_json[0]                          # traverse into list item (dictionary is stored inside a list)
        print("Successfully retrieved some data..." )
        return data_dict
    else:
        print("Error:", response.status_code, response.text)
        return "Error"


if __name__ == "__main__":
    api = api()
    data = fetch_data_api("success")
    tweet(api, "\"" + data["quote"] + "\"" + "\n\n- " + data["author"])

