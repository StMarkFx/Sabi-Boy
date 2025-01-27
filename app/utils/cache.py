from functools import lru_cache

@lru_cache(maxsize=100)
def cached_fetch_semantic_scholar_papers(query):
    """
    Caches results from Semantic Scholar API.
    """
    from app.api.semantic_scholar import fetch_semantic_scholar_papers
    return fetch_semantic_scholar_papers(query)

@lru_cache(maxsize=100)
def cached_fetch_pubmed_papers(query):
    """
    Caches results from PubMed API.
    """
    from app.api.pubmed import fetch_pubmed_papers
    return fetch_pubmed_papers(query)

@lru_cache(maxsize=100)
def cached_fetch_google_scholar_papers(query):
    """
    Caches results from Google Scholar web scraping.
    """
    from app.api.google_scholar import fetch_google_scholar_papers
    return fetch_google_scholar_papers(query)

@lru_cache(maxsize=100)
def cached_fetch_arxiv_papers(query):
    """
    Caches results from arXiv API.
    """
    from app.api.arxiv import fetch_arxiv_papers
    return fetch_arxiv_papers(query)