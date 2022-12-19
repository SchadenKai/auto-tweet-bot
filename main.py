import tweepy
from config import credential_keys as keys


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


if __name__ == "__main__":
    api = api()
    tweet(api, "Testing sample kung nagana", "chopper_img.webp")
