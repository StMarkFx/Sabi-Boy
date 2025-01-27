from Bio import Entrez
from Bio.Entrez import efetch, read
from app.utils.error_handling import handle_api_error

# Set up PubMed API (Biopython)
Entrez.email = "your_email@example.com"  # Required for PubMed API

@handle_api_error
def fetch_pubmed_papers(query):
    """
    Fetches research papers from PubMed based on a query.
    """
    # Search PubMed
    handle = Entrez.esearch(db="pubmed", term=query, retmax=3)
    record = Entrez.read(handle)
    handle.close()
    id_list = record.get("IdList", [])

    # Fetch details for each paper
    papers = []
    for paper_id in id_list:
        handle = Entrez.efetch(db="pubmed", id=paper_id, rettype="abstract", retmode="text")
        paper_details = handle.read()
        handle.close()
        papers.append({"id": paper_id, "details": paper_details})
    return papers