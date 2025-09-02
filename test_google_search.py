'''This module contains a simple Playwright test to automate a Google search.'''
import sys
try:
    from playwright.sync_api import sync_playwright
except ImportError as e:
    print(f"Import failed: {e}", file=sys.stderr)
    sys.exit(1)


def test_google_search():
    '''Test that opens a browser, navigates to Google, and closes it.'''
    print("Starting test...")
    try:
        with sync_playwright() as p:
            print("Launching browser (headless=False)...")
            browser = p.chromium.launch(headless=False)  # Visible browser
            print("Browser launched, creating page...")
            page = browser.new_page()
            print("Navigating to Google...")
            page.goto("https://www.google.com")
            print("Navigated to Google")
            browser.close()
        print("Test finished")
    except Exception as e:
        print(f"Error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    test_google_search()
