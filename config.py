import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'd1bl$7*nygc0gpp@6a8-2=6x9ixv8bd(j9c$c7=^xu_zka)b5s'
