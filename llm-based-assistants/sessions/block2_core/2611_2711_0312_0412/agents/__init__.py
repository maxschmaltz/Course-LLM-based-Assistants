import dotenv
dotenv.load_dotenv()    # that loads the .env file variables into os.environ

from agents.init_llm import init_llm
from agents.create_agent import create_agent