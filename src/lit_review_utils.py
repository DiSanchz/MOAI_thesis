import requests
import re
import bs4


def get_arxiv_bibtex(arxiv_id):
    """
    Retrieve the BibTeX entry for a given arXiv ID from the arXiv website.

    Parameters:
        arxiv_id (str): The unique identifier of the paper on arXiv.

    Returns:
        str: The BibTeX entry as a string if successful, otherwise None.
    """
    url = f"https://arxiv.org/bibtex/{arxiv_id}"  # Construct the URL to fetch BibTeX
    try:
        # Make an HTTP GET request to the arXiv BibTeX endpoint
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code != 200:
            print("Error fetching the BibTeX entry")
            return None

        # Return the BibTeX entry text
        bibtex = response.text
        return bibtex

    except Exception as e:
        # Handle any errors during the HTTP request
        print(f"Error: {e}")
        return None


def get_bibtex_author(bibtex_string):
    """
    Extract the list of authors from a BibTeX string.

    Parameters:
        bibtex_string (str): The BibTeX entry as a string.

    Returns:
        list: A list of author names if found, otherwise None.
    """
    # Regular expression to find the content of the 'author' field in the BibTeX string
    author_pattern = r"author=\{(.*?)\}"

    # Search for the 'author' field in the BibTeX string
    match = re.search(author_pattern, bibtex_string, re.DOTALL)

    if match:
        # Extract the authors string from the matched group
        authors = match.group(1)

        # Split the authors by "and" into a list
        author_list = authors.split(" and ")
        # print("Authors:", authors)
        return author_list
    else:
        # Print an error message if no authors are found
        print("No authors found")
        return None


def get_bibtex_year(bibtex_string):
    """
    Extract the year from a BibTeX string.

    Parameters:
        bibtex_string (str): The BibTeX entry as a string.

    Returns:
        str: The year as a string if found, otherwise None.
    """
    # Regular expression to find the content of the 'year' field in the BibTeX string
    year_pattern = r"year=\{(\d{4})\}"

    # Search for the 'year' field in the BibTeX string
    match = re.search(year_pattern, bibtex_string)

    if match:
        # Extract the year from the matched group
        year = match.group(1)
        # print("Year:", year)
        return year
    else:
        # Print an error message if no year is found
        print("No year found")
        return None


def get_bibtex_title(bibtex_string):
    """
    Extract the title from a BibTeX string.

    Parameters:
        bibtex_string (str): The BibTeX entry as a string.

    Returns:
        str: The title as a string if found, otherwise None.
    """
    # Regular expression to find the content of the 'title' field in the BibTeX string
    title_pattern = r"title=\{(.*?)\}"

    # Search for the 'title' field in the BibTeX string
    match = re.search(title_pattern, bibtex_string, re.DOTALL)

    if match:
        # Extract the title from the matched group
        title = match.group(1)
        # print("Title:", title)
        return title
    else:
        # Print an error message if no title is found
        print("No title found")
        return None


def get_arxiv_abstract(arxiv_id):
    """
    Fetch and extract the abstract from an arXiv paper given its ID.

    Parameters:
        arxiv_id (str): The arXiv paper ID (e.g., '2408.08921').

    Returns:
        str: The extracted abstract text if found, otherwise None.
    """
    # Define the arXiv URL based on the arXiv ID
    url = f"https://arxiv.org/abs/{arxiv_id}"
    try:
        # Make a request to fetch the HTML content
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch page. HTTP Status Code: {response.status_code}")
            return None

        # Parse the HTML content with BeautifulSoup
        soup = bs4.BeautifulSoup(response.text, "html.parser")

        # Locate the abstract block using <blockquote> with class "abstract mathjax"
        abstract_block = soup.find("blockquote", class_="abstract mathjax")
        if abstract_block:
            # Extract the text, remove the label "Abstract:" and clean up whitespace
            abstract_text = abstract_block.get_text(strip=True)
            abstract_clean = abstract_text.replace("Abstract:", "").strip()
            return abstract_clean
        else:
            print("No abstract found in the HTML content.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
