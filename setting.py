from dotenv import load_dotenv
import os

load_dotenv('.env')


def get(key):
    env = os.environ.get(key)
    return env
