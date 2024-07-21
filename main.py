import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/search?q=tungguakudi&oq=tungguakudi&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDYyMTZqMGoyqAIAsAIB&sourceid=chrome&ie=UTF-8")
    page.goto("https://tungguakudi.com/")
    page.get_by_role("link", name="Beli Tiket").nth(1).click()
    page.locator("div").filter(has_text="Beli Tiket").nth(2).click(click_count=100)
    time.sleep(3600)  # wait for the page to load

   

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
