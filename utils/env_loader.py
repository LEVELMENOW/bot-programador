import os
from dotenv import load_dotenv

def load_env():
    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    load_dotenv(dotenv_path)
    print("✅ Variables de entorno cargadas:")
    print(f"🔑 GITHUB_REPO: {os.getenv('GITHUB_REPO')}")
    print(f"🔑 OPENAI_API_KEY: {'Cargada' if os.getenv('OPENAI_API_KEY') else 'Faltante'}")
    print(f"🔑 GITHUB_TOKEN: {'Cargada' if os.getenv('GITHUB_TOKEN') else 'Faltante'}")
