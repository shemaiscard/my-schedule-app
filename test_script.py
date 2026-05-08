import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        page.on("console", lambda msg: print(f"CONSOLE: {msg.text}"))
        page.on("pageerror", lambda err: print(f"PAGE ERROR: {err}"))
        
        await page.goto("http://localhost:8000/schedule.html", wait_until="networkidle")
        
        # Check if tabs are rendered
        content = await page.content()
        if "day-tab" in content:
            print("Tabs rendered!")
        else:
            print("Tabs NOT rendered!")
            
        await browser.close()

asyncio.run(run())
