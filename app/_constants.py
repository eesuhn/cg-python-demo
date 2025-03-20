import os

from dotenv import load_dotenv


load_dotenv()

CG_PRO_API_KEY = os.getenv("CG_PRO_API_KEY")
CG_DEMO_API_KEY = os.getenv("CG_DEMO_API_KEY")
