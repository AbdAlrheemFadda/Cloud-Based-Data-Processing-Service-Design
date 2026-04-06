import asyncio
from playwright.async_api import async_playwright
import os

async def capture_screenshots():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Get absolute path to index.html
        path = os.path.abspath("index.html")
        await page.goto(f"file://{path}")

        # 1. Final Page Full Screenshot
        await page.screenshot(path="final_page.png", full_page=True)
        print("Captured final_page.png")

        # 2. Hero Section (Simulating settings)
        hero = await page.query_selector(".hero")
        await hero.screenshot(path="wp_setting_hero.png")
        print("Captured wp_setting_hero.png")

        # 3. Discover Section
        discover = await page.query_selector(".discover")
        await discover.screenshot(path="wp_setting_discover.png")
        print("Captured wp_setting_discover.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_screenshots())
