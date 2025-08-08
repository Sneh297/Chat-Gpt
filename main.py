import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome options
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Start browser
driver = uc.Chrome(options=options, version_main=138)

# Open ChatGPT
driver.get("https://www.chatgpt.com")

# --- WAIT: Login manually if needed ---
  # Give time for manual login
time.sleep(5)

# Wait for the real contenteditable input box


def input(prompt):
    wait = WebDriverWait(driver, 30)
    input_div = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.ProseMirror[contenteditable="true"]')
    ))

    # Click to focus it
    input_div.click()

    # Type your message
    input_div.send_keys(prompt + "under 100 words")

    # Press Enter to send
    input_div.send_keys(Keys.ENTER)
    time.sleep(10)

prompts = [
    "What makes Europa a candidate for extraterrestrial life?",
    "How do gas giants like Jupiter and Saturn form?",
    "Why does Titan have a thick atmosphere while other moons don't?",
    "What causes the extreme temperature swings on Mercury?",
    "Could humans ever colonize Mars or one of its moons?"
]

for i in range(0,5):


    
    input(prompts[i])


# Wait to see result
time.sleep(100)

# Close browser
driver.quit()
