"""
使用 Playwright 打开本地 HTML 文件并截图
"""
import asyncio
import os
from pathlib import Path

async def screenshot_chitalka():
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        import subprocess
        subprocess.run(["pip", "install", "playwright"], check=True)
        subprocess.run(["playwright", "install", "chromium"], check=True)
        from playwright.async_api import async_playwright
    
    html_path = r"c:\Users\36171\WorkBuddy\20260417222122\chitalka\index.html"
    output_dir = r"c:\Users\36171\WorkBuddy\20260417222122\chitalka\screenshots"
    os.makedirs(output_dir, exist_ok=True)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1280, "height": 800})
        
        # 打开本地 HTML 文件
        file_url = "file:///" + html_path.replace("\\", "/").replace(":", "%3A")
        print(f"Opening: {file_url}")
        await page.goto(file_url, wait_until="networkidle", timeout=10000)
        await page.wait_for_timeout(2000)
        
        # 截图1：主界面（空状态）
        await page.screenshot(path=os.path.join(output_dir, "01_main_interface.png"))
        print("Screenshot 1: main interface taken")
        
        # 尝试拖入测试文件（需要通过 set_input_files）
        # 由于是本地文件且需要交互，先截图空状态
        
        await browser.close()
        print(f"All screenshots saved to: {output_dir}")

if __name__ == "__main__":
    asyncio.run(screenshot_chitalka())
