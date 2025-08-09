import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import random
import pyperclip
from data import prompts

import json






prefix = """Format the following text by removing unnecessary line breaks while preserving logical paragraph structure. Ensure it is compact and readable for placement in a website text field. Return the result inside a plain code block without adding extra formatting or blank lines.
"""
copy_prompts = prompts






def setup_driver():
    """Setup Chrome driver with compatible options"""
    try:
        options = uc.ChromeOptions()
        prefs = {
    "profile.default_content_setting_values.clipboard": 1,
    "profile.content_settings.exceptions.clipboard": {
        "https://chat.openai.com,*": {
            "setting": 1
        }
    }
}       
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = uc.Chrome(options=options, version_main=138)
        print("✓ Successfully created driver with Chrome 138")
        return driver
    except Exception as e:
        print(f"✗ Chrome 138 failed: {e}")
    try:
        options = uc.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = uc.Chrome(options=options)
        print("✓ Successfully created driver with fallback method")
        return driver
    except Exception as e:
        raise Exception("All ChromeDriver setup methods failed.") from e


def handle_stay_logged_out(driver):
    """Click 'Stay logged out' link if present"""
    try:
        stay_logged_out = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="#"].text-token-text-secondary'))
        )
        if "Stay logged out" in stay_logged_out.text:
            stay_logged_out.click()
            time.sleep(2)
            return True
    except TimeoutException:
        return False


def wait_for_page_load(driver):
    """Wait for page to fully load"""
    WebDriverWait(driver, 30).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )
    time.sleep(random.uniform(2, 4))

def click_all_copy_buttons(driver):
    """Click each visible copy button once and save copied content."""
    try:
        k=0
        time.sleep(10)
        print("Looking for copy buttons...")
        total_buttons = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button[aria-label="Copy"]'))
        )
        print(f"✓ Found {len(total_buttons)} copy buttons.")

        for i in range(len(total_buttons)):
            try:
                time.sleep(1)
                # 🔁 Refetch buttons fresh each time
                buttons = driver.find_elements(By.CSS_SELECTOR, 'button[aria-label="Copy"]')
                btn = buttons[i]

                # Scroll into view
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", btn)
                time.sleep(1)

                # JS click to avoid interception
                driver.execute_script("arguments[0].click();", btn)
                time.sleep(1)

                # Get clipboard content
                copied = pyperclip.paste()
                print(f"\n✓ Code block {i + 1} copied:\n{copied[:300]}...\n")

                if (i + 1 - 2) % 3 == 0:
                    print(f"\n\n✓ Code block {i + 1} copied:\n{copied[:300]}...\n\n")
                    copy_prompts[k]["response"] = copied
                    k=k+1                 


           
            except Exception as e:
                print(f"✗ Error clicking button {i + 1}: {e}")

        # with open('data.py', "w", encoding="utf-8") as f:
        #     f.write(copy_prompts)
        #     f.write("\n")

        with open("data.py", "w", encoding="utf-8") as f:
            f.write("prompts = [\n")
            for item in copy_prompts:
                f.write("    {\n")
                f.write(f"        'prompt': '''{item['prompt']}''',\n")
                f.write(f"        'response': '''{item['response']}'''\n")
                f.write("    },\n")
            f.write("]\n")



        print("✓ Finished copying all code blocks.\n")

    except TimeoutException:
        print("✗ No copy buttons found.")

def send_prompt(driver, prompt):
    """Send prompt to ChatGPT"""
    try:
        handle_stay_logged_out(driver)
        wait = WebDriverWait(driver, 30)
        input_selectors = [
            'div.ProseMirror[contenteditable="true"]',
            'textarea[placeholder*="Message"]',
            'div[contenteditable="true"]',
            '#prompt-textarea'
        ]

        input_element = None
        for selector in input_selectors:
            try:
                input_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                break
            except TimeoutException:
                continue

        if not input_element:
            raise Exception("❌ Input field not found.")

        driver.execute_script("arguments[0].scrollIntoView(true);", input_element)
        time.sleep(1)
        input_element.click()
        time.sleep(1)
        input_element.clear()

        full_prompt = f"{prefix}+{prompt} "
        pyperclip.copy(full_prompt)
        input_element.send_keys(Keys.CONTROL, "v")
        time.sleep(2)
        print("✓ Prompt pasted via clipboard.")
        input_element.send_keys(Keys.ENTER)

        print("⏳ Waiting for response...")
        time.sleep(15)  # Let the response generate for a bit

       

        return True

    except Exception as e:
        print(f"✗ Error in send_prompt: {e}")
        return False

def wait_and_click_close(driver, timeout=10):
    try:
        close_btn = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="close-button"]'))
        )
        close_btn.click()
        print("✓ Close button clicked.")
        return True
    except TimeoutException:
        print("✗ Close button not found in time.")
        return False




def main():
    driver = setup_driver()
    try:
 
        print("Opening ChatGPT...")
        driver.get("https://chat.openai.com/")
        wait_for_page_load(driver)
        handle_stay_logged_out(driver)
        wait_and_click_close(driver, timeout=10)
        time.sleep(5)
        success_count = 0
        for i, prompt in enumerate(copy_prompts, 1):

            print(f"\n--- Sending prompt {i}/{len(prompts)} ---")
            if send_prompt(driver, prompt['prompt']):
                success_count += 1
                time.sleep(random.uniform(5, 10))
            else:
                print(f"✗ Failed to send prompt {i}")
                time.sleep(5)
        print(f"\n✓ Finished sending prompts: {success_count}/{len(prompts)}")
        click_all_copy_buttons(driver)
        print("Sleeping 10s before closing...")
        time.sleep(10)

    except KeyboardInterrupt:
        print("\n⛔ Interrupted by user.")
    except Exception as e:
        print(f"❌ Fatal error: {e}")
    finally:
        print("Closing browser...")
        driver.quit()


if __name__ == "__main__":
    main()
