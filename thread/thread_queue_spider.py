import requests
from lxml import etree
import threading
from queue import Queue

class Spider():

    def __init__(self):
        self.headrs = None
