import argparse
import json
import markovify
import tweepy

import thesecrets as thesecrets


# e.g. python3 tweeter.py rickBot 280



def main(args):
    twitter_auth_keys = {
        "consumer_key": thesecrets.consumer_key,
        "consumer_secret": thesecrets.consumer_secret,
        "access_token": thesecrets.access_token,
        "access_token_secret": thesecrets.access_token_secret
    }
    auth = tweepy.OAuthHandler(
        twitter_auth_keys['consumer_key'],
        twitter_auth_keys['consumer_secret']
    )
    auth.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
    )
    api = tweepy.API(auth)

    model = markovify.Text.from_json(json.load(open('./{}.json'.format(args.bot_type), 'r')))
    
    text = model.make_short_sentence(args.max_characters)
    status = api.update_status(status = text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run the bot.')
    parser.add_argument('bot_type',
                        type=str,
                        help='name of the bot to load (rickBot)')
    parser.add_argument('-mc',
                        '--max_characters',
                        default=280,
                        type=int,
                        help='maximun number of characters of the tweet')

    args = parser.parse_args()
    main(parser.parse_args())
