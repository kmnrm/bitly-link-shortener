import os
import requests
import json
import argparse
from dotenv import load_dotenv

HOST = "https://api-ssl.bitly.com/"
VERSION = "v4"
DOMAIN = "bit.ly"
DESCRIPTION ='''
Bitly url shorterer is a program that lets you shorten long urls by BITLY URL shorten service via console commands.
This program also counts clicks on user's short bit.ly links.
'''


def shorten_link(token, url):
    
    shorten_address = "/shorten"
    user_address = "/user"
    shorten_address = "{}{}{}".format(HOST, VERSION, shorten_address)
    user_address = "{}{}{}".format(HOST, VERSION, user_address)
    headers = {
        "Authorization": "Bearer %s" % token
    }
    response = requests.get(user_address, headers=headers)
    response.raise_for_status()
    response = response.json()
    group_guid = response.get("default_group_guid")

    payload = {
        "long_url": url,
        "group_guid": group_guid,
        "domain": DOMAIN,
    }
    response = requests.post(shorten_address, headers=headers, json=payload)
    response.raise_for_status()
    response = json.loads(response.text)
    bitlink = response.get("id")
    return bitlink


def count_clicks(token, link):
    link = link.replace("https://", "")
    address = "/bitlinks/{}/clicks/summary".format(link)
    address = "{}{}{}".format(HOST, VERSION, address)
    headers = {
        "Authorization": "Bearer %s" % token
    }
    params = {
        "unit": "day",
        "units": -1,
    }
    response = requests.get(address, headers=headers, params=params)
    response.raise_for_status()
    response = response.json()
    total_clicks = response.get("total_clicks")
    return total_clicks


def main():
    load_dotenv()
    bitly_token = os.getenv("BITLY_GENERIC_ACCESS_TOKEN_1")
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('userlink', help='User URL')
    args = parser.parse_args()
    user_url = args.userlink
    if user_url.startswith("http://"):
        user_url = user_url.replace("http://", "https://")

    elif not user_url.startswith("http://") and not user_url.startswith("https://"):
        user_url_head = 'https://'
        user_url = "{}{}".format(user_url_head, user_url)


    if user_url.startswith("https://{}".format(DOMAIN)):
        try:
            total_clicks = count_clicks(bitly_token, user_url)
        except requests.exceptions.HTTPError as http_error:
            exit("HTTPError. Just leave, please... Or come again next time!")
        print("Total clicks:", total_clicks)

    else:
        try:
            bitlink = shorten_link(bitly_token, user_url)
        except requests.exceptions.HTTPError as http_error:
            exit("HTTPError. You gotta be kiddin' me, man. Bye...")
        print("Here's your bitlink, gringo:", bitlink)


if __name__ == "__main__":
    main()
