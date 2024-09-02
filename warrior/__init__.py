import os
import logging

import pyromod.listen

from pyrogram import Client 
from pymongo import MongoClient


#prefix for commands
prefix = [".","!","?","*","$","#","/"]


#mongo database 
MONGODB_URL = "mongodb+srv://tiwarireeta004:peqxLEd36RAg7ors@cluster0.furypd3.mongodb.net/?retryWrites=true&w=majority"
MONGO = MongoClient(MONGODB_URL)
DATABASE = MONGO.WARRIOR



FORMAT = "[Warrior]: %(message)s"

logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()], format=FORMAT)


API_ID = os.getenv("24074986")
API_HASH = os.getenv("f4f6272a85d0e50e39a24cb378be118d")
TOKEN = os.getenv("7017047992:AAFdn36ey8whO8Cz1t-2K7_tIUWPwcK0oZk")
GROUP_ID = os.getenv("-1002147169639")



bot = Client(
       name="warrior",
       api_id=API_ID,
       api_hash=API_HASH,
       bot_token=TOKEN,
       plugins=dict(root="warrior"),)


