from playwright.sync_api import sync_playwright


def test_wikipedia_title():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.wikipedia.org")
        assert "Wikipedia" in page.title()
        browser.close()


def test_login_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/login")
        assert page.is_visible("input[name='username']")
        browser.close()
