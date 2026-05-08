import re

from playwright.sync_api import Page, expect


def test_amazon_mx_player_telugu_navigation(page: Page) -> None:
    page.goto("https://www.amazon.in/")
    page.get_by_role("link", name="MX Player").click()
    page.get_by_role("link", name="New & Hot").click()
    page.get_by_role("link", name="Romance").click()
    page.get_by_role("link", name="Telugu").click()

    expect(page).to_have_url(re.compile(r"amazon\.in"))
