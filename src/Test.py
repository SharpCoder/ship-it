import json
from libs import S3Client

if __name__ == "__main__":
    # execute only if run as a script
    print("hi")
    client = S3Client.S3Client()
    commands = json.loads(client.get_object("mudon", "ship-it/rest.json").read())
    print(commands)