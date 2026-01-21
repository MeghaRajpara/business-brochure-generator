from utilities import fetch_website_links, fetch_website_contents
from app.llm_client import select_relevant_links


def collect_company_content(base_url: str) -> str:
    """
    Fetch landing page content and selected internal pages.
    """
    landing_page = fetch_website_contents(base_url)
    raw_links = fetch_website_links(base_url)

    links_prompt = f"Website links:\n" + "\n".join(raw_links)
    selected_links = select_relevant_links(links_prompt)

    content = f"## Landing Page\n{landing_page}\n"

    for link in selected_links.get("links", []):
        content += f"\n## {link['type'].title()}\n"
        content += fetch_website_contents(link["url"])

    return content[:5000]  # Token safety
