import re

from playwright.sync_api import Page, expect


def test_amazon_search_returns_results(page: Page) -> None:
    page.goto("https://www.amazon.in/")

    search_box = page.get_by_role("searchbox", name="Search Amazon.in")
    search_box.fill("cricket kit")
    search_box.press("Enter")

    expect(page).to_have_url(re.compile(r"k=cricket\+kit"))
    expect(page.get_by_role("link", name=re.compile(r"cricket", re.IGNORECASE)).first).to_be_visible()
