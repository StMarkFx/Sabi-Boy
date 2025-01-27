import requests
from app.utils.error_handling import handle_api_error

@handle_api_error
def fetch_semantic_scholar_papers(query):
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=3"
    response = requests.get(url)
    if response.status_code == 200:
        papers = response.json().get("papers", [])
        return papers
    return []