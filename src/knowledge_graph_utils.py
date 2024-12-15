import networkx as nx
import matplotlib.pyplot as plt
import json

from lit_review_utils import (
    get_arxiv_bibtex,
    get_bibtex_year,
    get_bibtex_title,
    get_bibtex_author,
    get_arxiv_abstract,
)


def build_knowledge_graph(arxiv_ids, citations_dict):
    """
    Build a knowledge graph using NetworkX from a list of arXiv IDs.
    Each paper is a node with its properties, and authors are nodes connected with "is_author" relations.
    """
    # Create the graph
    G = nx.DiGraph()

    # Iterate over each arXiv ID
    for arxiv_id in arxiv_ids:
        print(f"Processing arXiv ID: {arxiv_id}")

        # Retrieve the BibTeX and other data
        bibtex_string = get_arxiv_bibtex(arxiv_id)
        if not bibtex_string:
            print(f"Skipping ID {arxiv_id} due to missing BibTeX.")
            continue

        publication_year = get_bibtex_year(bibtex_string)
        publication_title = get_bibtex_title(bibtex_string)
        author_list = get_bibtex_author(bibtex_string)
        abstract = get_arxiv_abstract(arxiv_id)

        # Add paper node
        if not G.has_node(arxiv_id):
            G.add_node(
                arxiv_id,
                type="paper",
                title=publication_title,
                year=publication_year,
                abstract=abstract,
            )

        # Add author nodes and relationships
        for author in author_list:
            if not G.has_node(author):
                G.add_node(author, type="author")
            # Relationship "is_author"
            G.add_edge(author, arxiv_id, relation="is_author")
            # Relationship "authored_by"
            G.add_edge(arxiv_id, author, relation="authored_by")

    for arxiv_id in arxiv_ids:
        # Add citation relationships (if they exist in the dictionary)
        if arxiv_id in citations_dict:
            cited_papers = citations_dict[arxiv_id]
            for cited_id in cited_papers:
                # Ensure that the cited nodes also exist
                if not G.has_node(cited_id):
                    G.add_node(cited_id, type="paper", title="", year="", abstract="")

                # Relationship "cites" (from arxiv_id to cited_id)
                G.add_edge(arxiv_id, cited_id, relation="cites")
                # Inverse relationship "cited_in" (from cited_id to arxiv_id)
                G.add_edge(cited_id, arxiv_id, relation="cited_in")

    return G
