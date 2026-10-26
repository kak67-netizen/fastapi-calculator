"""Browser tests for calculator interactions."""

from playwright.sync_api import expect, sync_playwright


def test_addition_in_browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            page.goto("http://127.0.0.1:8000")
            page.fill("#a", "2")
            page.fill("#b", "3")
            page.click("button#add")

            expect(page.locator("#result")).to_have_text("Result: 5")
        finally:
            browser.close()


def test_divide_by_zero_in_browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            page.goto("http://127.0.0.1:8000")
            page.fill("#a", "10")
            page.fill("#b", "0")
            page.click("button#divide")

            expect(page.locator("#result")).to_have_text(
                "Error: Cannot divide by zero."
            )
        finally:
            browser.close()