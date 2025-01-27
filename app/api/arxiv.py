import arxiv
from app.utils.error_handling import handle_api_error

@handle_api_error
def fetch_arxiv_papers(query):
    """
    Fetches research papers from arXiv based on a query.
    """
    search = arxiv.Search(query=query, max_results=3)
    papers = []
    for result in search.results():
        papers.append({
            "title": result.title,
            "authors": ", ".join([author.name for author in result.authors]),
            "link": result.entry_id,
            "summary": result.summary
        })
    return papers