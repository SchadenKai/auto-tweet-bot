# auto-tweet-bot
Automatic tweeting system using python with integration of retrieving API for automatic content to post.

## Setup 
**Needed:** Developer Twitter Account and API Ninja Account 
- First, install the tweepy module through your IDE. `pip install tweepy`
- Retrieve your necessary API keys in your twitter developer account.
- Next is retrieve the api key in your API Ninja account.
**Necessary keys and token:** `api_key`; `api_secret`; `access_token`; `access_token_secret`; `quotes_api_key`
- Paste all the necessary information in the `sample_credential_keys.py` in the config folder. Then replace the file name into `credential_keys.py`.
- Then run and see the results in your twitter account. 

## More
If you want to change the categories of the quotes that is being retrieved and posted. You can change the category in: \
`data = fetch_data_api("category name")` \
The list of categories are available in the API Ninja website under Quotes. [Click Me](https://api-ninjas.com/api/quotes) for the categories available.

For the live sample of the project you can follow my [Twitter account](https://twitter.com/dailyquotesapi). This is where
the bot app post quotes retrieved from the API Ninja.
