import json
from libs import S3Client
from libs import Api

if __name__ == "__main__":
    # execute only if run as a script
    api = Api.Api()
    client = S3Client.S3Client()
    commands = json.loads(client.get_object("mudon", "ship-it/rest.json").read())

    for command in commands:
        print(command["method"], " -> ", command["url"])
        result = api.invoke(command)
        print(result.status_code, " <- ")