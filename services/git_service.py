from github import Github
import os

def obtener_contenido_archivo(ruta_archivo):
    token = os.getenv("GITHUB_TOKEN")
    repo_name = os.getenv("GITHUB_REPO")
    g = Github(token)
    repo = g.get_repo(repo_name)
    contents = repo.get_contents(ruta_archivo, ref="main")
    return contents.decoded_content.decode()
