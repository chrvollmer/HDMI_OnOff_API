import os


MSG_CLIENT_ID = os.getenv("MSG_CLIENT_ID")
if not MSG_CLIENT_ID:
    raise ValueError("Need to define MSG_CLIENT_ID environment variable")

MSG_CLIENT_SECRET = os.getenv("MSG_CLIENT_SECRET")
if not MSG_CLIENT_SECRET:
    raise ValueError("Need to define MSG_CLIENT_SECRET environment variable")

MSG_AUTHORITY = os.getenv("MSG_AUTHORITY")
if not MSG_AUTHORITY:
    raise ValueError("Need to define MSG_AUTHORITY environment variable")