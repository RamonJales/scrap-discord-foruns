import requests
import json
import argparse
import os

def retrive_message(chanelid):
    headers = {
        'authorization': os.getenv('DISCORD_AUTH_TOKEN'),
    }

    r = requests.get(f'https://discord.com/api/v9/channels/{chanelid}/messages', headers=headers)

    content = json.loads(r.text)

    with open('message.json', 'w') as f:
        json.dump(content, f, indent=4)

    print('Message saved in message.json')

    return content


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("chanelid", type=str, help="The discord chanel id.")
    args = parser.parse_args()
    chanelid = args.chanelid
    content = retrive_message(chanelid)
    for value in content:
        print(value, '\n')


if __name__ == "__main__":
    main()

