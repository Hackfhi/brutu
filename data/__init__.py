import os
from .app import *
from .facebook import facebook


os.system('cls' if os.name == 'nt' else 'clear')
lol(open(os.path.dirname(os.path.realpath(__file__))+'/__data__/banners.txt', 'r').read())
