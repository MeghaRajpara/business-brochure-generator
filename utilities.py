from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin, urlparse


headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/117.0.0.0 Safari/537.36"
    )
}


def _is_valid_url(url: str) -> bool:
    """Check if URL has a valid HTTP/HTTPS scheme."""
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https")


def fetch_website_contents(url: str) -> str:
    """
    Fetch title and cleaned body text from a website.
    Returns empty string if URL is invalid.
    """
    if not _is_valid_url(url):
        return ""

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return ""

    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.title.string.strip() if soup.title else "No title found"

    if soup.body:
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""

    return (title + "\n\n" + text)[:2_000]


def fetch_website_links(base_url: str) -> list[str]:
    """
    Fetch and normalize all valid internal and external links
    found on the webpage.
    """
    try:
        response = requests.get(base_url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    links = []

    for tag in soup.find_all("a", href=True):
        href = tag.get("href").strip()

        # Skip anchors, mailto, javascript
        if href.startswith(("#", "mailto:", "javascript:")):
            continue

        absolute_url = urljoin(base_url, href)

        if _is_valid_url(absolute_url):
            links.append(absolute_url)

    return list(set(links))  # remove duplicates
