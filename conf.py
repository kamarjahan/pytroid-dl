import os


class Config(object):
    dl_link = os.environ.get("dl_link", "")
