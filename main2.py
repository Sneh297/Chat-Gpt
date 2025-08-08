import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import random
import pyperclip


prefix = """Format the following text by removing unnecessary line breaks while preserving logical paragraph structure. Ensure it is compact and readable for placement in a website text field. Return the result inside a plain code block without adding extra formatting or blank lines.
"""
g =2

# prompts = ["what is your name and how well do you play circket " , "I am in 4 year ocmputer sciense what aobut you ","sdgwszdgthrjyhnfgbdwqasfdgnhmb ichvs nodnvodnoe bsoefwo ","dfgwrw qw  qrw w opj p jq[ w]] wro ","sdon ownqpn nq30j apsna oj30 japs jaw","aosfbqnwo bh9w 0auw0qu wuz0","odfaposndaosgbaobc onzdov"]



prompts = [
           """Minimum Time to Complete Tasks with Dependencies
You are given N tasks numbered from 0 to N-1. Each task takes 1 unit of time to complete. Some tasks depend on the completion of other tasks and can only start once all their prerequisite tasks are finished. You are given a list of dependency pairs (a, b), meaning task a must be completed before task b can start.

You have unlimited resources and can run multiple tasks in parallel as long as their dependencies are satisfied. Your task is to find the minimum time required to complete all tasks.

Function Description:  
Implement the function minimumTimeToCompleteTasks with parameters:  
- N: integer, total number of tasks  
- M: integer, number of dependency pairs  
- dependencies: list of pairs (a, b) where task a must be completed before task b

Return:  
- int: minimum time to complete all tasks

Constraints:  
- 1 ≤ N ≤ 10^5  
- 0 ≤ M ≤ 10^5  
- 0 ≤ a, b < N

Sample Input:  
5 4  
0 1  
1 2  
0 3  
3 4

Sample Output:  
3

Explanation:  
- Task 0 starts at time 1  
- Tasks 1 and 3 depend on task 0, so they start at time 2  
- Task 2 depends on 1, and task 4 depends on 3, so they start at time 3  
Thus, the minimum time to complete all tasks is 3.""",

"""Rotten Oranges

You are given an N x M grid representing a storage area for oranges. Each cell in the grid can be:  
- 0: empty cell  
- 1: fresh orange  
- 2: rotten orange  

A rotten orange at position (i, j) spreads rot to its adjacent fresh oranges (up, down, left, right) every minute. The rotting process happens simultaneously for all rotten oranges at each time step.  

Your task is to determine the minimum time required for all fresh oranges to become rotten. If at least one fresh orange cannot rot, return -1.

Function Description:  
Implement the function minTimeToRottenOranges with parameters:  
- int N: number of rows in the grid  
- int M: number of columns in the grid  
- int[][] grid: a 2D array representing the orange states

Returns:  
- int: minimum minutes for all fresh oranges to rot, or -1 if impossible.""",
"""
Implement a prototype for a text editor application with the following functionalities:

Command  
Actions:  
- ["Insert", s]: Insert the string s at the current cursor position. The cursor moves right by the length of s.  
- ["Left", x]: Move the cursor x positions to the left, but not past the start of the string.  
- ["Right", x]: Move the cursor x positions to the right, but not past the end of the string.  
- ["Backspace", x]: Remove x characters immediately to the left of the cursor, moving the cursor left accordingly.  
- ["Delete", x]: Remove x characters immediately to the right of the cursor. Cursor position does not change.  
- ["Print", x]: If the cursor is at position m, print all characters from index m - x to m + x (inclusive), adjusting for string boundaries.

Given a 2D array of commands of size n x 2, perform the operations starting from an empty string and cursor at position 0. For each "Print" command, record the resulting substring. Return all printed substrings as an array, in the order they are printed.

Note: The second argument in commands is always a string and should be converted to integer where applicable.

Function Description  
Complete the function getPrintedStrings with parameter:  
commands[n][2]: list of commands to execute.

Returns  
string[]: list of printed strings from "Print" commands.

Constraints  
- 1 ≤ n ≤ 5000  
- Sum of lengths of all inserted strings ≤ 5 * 10^3  
- First inserted string length ≤ 100, subsequent insertions ≤ 25  
- All strings contain only lowercase English letters.

Input Format For Custom Testing  
- First line: integer n, number of commands  
- Second line: integer 2  
- Next n lines: two space-separated strings commands[i][0] and commands[i][1]

Sample Case 0

Input:  
7  
2  
Insert addthis  
Print 5  
Left 4  
Right 2  
Backspace 1  
Delete 1  
Print 10

Output:  
dthis  
addts

Explanation:  
1. Insert "addthis": string = "addthis", cursor = 7  
2. Print 5: substring from 7 - 5 = 2 to 7 + 5 = 12 → "dthis"  
3. Left 4: cursor moves from 7 to 3  
4. Right 2: cursor moves from 3 to 5  
5. Backspace 1: remove 1 char left of cursor → string = "addtis", cursor = 4  
6. Delete 1: remove 1 char right of cursor → string = "addts", cursor = 4  
7. Print 10: substring from max(0, 4 - 10) = 0 to min(len, 4 + 10) = 9 → "addts"

Sample Case 1

Input:  
7  
2  
Insert present  
Print 5  
Left 4  
Insert test  
Print 8  
Delete 4  
Print 7

Output:  
esent  
pretestsent  
pretest

Explanation:  
1. Insert "present": string = "present", cursor = 7  
2. Print 5: substring 7 - 5 = 2 to 7 + 5 = 12 → "esent"  
3. Left 4: cursor = 3  
4. Insert "test": string = "pretestsent", cursor = 7  
5. Print 8: substring 7 - 8 = -1 to 7 + 8 = 15 → "pretestsent"  
6. Delete 4: remove 4 chars right of cursor → string = "pretest", cursor = 7  
7. Print 7: substring max(0, 7 - 7) = 0 to min(len, 7 + 7) = 14 → "pretest"
""",

"""You've been asked to program a bot for a popular bank that will automate the management of incoming requests. Every request has its own timestamp in seconds, and it is guaranteed that all requests come sequentially, i.e. the timestamp is strictly increasing. There are two types of incoming requests: 

. deposit <timestamp> <holder_id> <amount> - request to deposit <amount> amount of money in the <holder_id> account; 

. withdraw <timestamp> <holder_id> <amount> - request to withdraw <amount> amount of money from the <holder_id> account. As a bonus, the bank also provides a cashback policy - 2% of the withdrawn amount rounded down to the nearest integer will be returned to the account exactly 24 hours after the request timestamp. If the cashback and deposit/withdrawal happen at the same timestamp, assume cashback happens earlier.

Your system should also handle invalid requests. There are two types of invalid requests: 

. invalid account number; 

. withdrawal of a larger amount of money than is currently available.

For the given list of initial balances and requests, return the state of balances straight after the last request has been processed, or an array of a single element [-<request_id>] (please note the minus sign), where <request_id> is the 1-based index of the first invalid request. Note that cashback requests which haven't happened before the last request timestamp should be ignored.

Example

Example 1: For balances = [1000, 1500] and requests = ["withdraw 1613327630 2 480", "withdraw 1613327644 2 800", "withdraw 1614105244 1 100", "deposit 1614108844 2 200", "withdraw 1614108845 2 150"], the output should be solution(balances, requests) = [900, 295].

Explanation: Here are the states of balances after each request:

. Initially: [1000, 1500]; 
. "withdraw 1613327630 2 480": [1000, 1020]; 
. "withdraw 1613327644 2 800": [1000, 220]; 
. At 1613414030 the 2nd account will receive the cashback of 480 * 0.02 = 9.6, which is rounded down to 9: [1000, 229]; 
. At 1613414044 the 2nd account will receive the cashback of 800 * 0.02 = 16: [1000, 245]; 
. "withdraw 1614105244 1 100": [900, 245]; 
. At 1614191644 the 1st account will receive cashback of 2: [902, 245]; 
. "deposit 1614108844 2 200": [902, 445]; 
. "withdraw 1614108845 2 150": [902, 295]; 
. Final state: [902, 295].

Example 2: For balances = [20, 1000, 500, 40, 90] and requests = ["deposit 1613327630 3 400", "withdraw 1613327635 1 20", "withdraw 1613327651 1 50", "deposit 1613327655 1 50"], the output should be solution(balances, requests) = [-3].

Explanation: Here are the states of balances after each request:

. Initially: [20, 1000, 500, 40, 90]; 
. "deposit 1613327630 3 400": [20, 1000, 900, 40, 90]; 
. "withdraw 1613327635 1 20": [0, 1000, 900, 40, 90]; 
. "withdraw 1613327651 1 50": it is not possible to withdraw 50 from the 1st account, so the request is invalid; 
. The rest of the requests are not processed.

Input/Output

. [execution time limit] 4 seconds (py3) 
. [memory limit] 1 GB 
. [input] array.integer balances: Array of integers, where balances[i] is the amount of money in the (i + 1)th account.

Guaranteed constraints: 1 ≤ balances.length < 100
""",
    """Minimum Time to Complete Tasks with Dependencies

You are given N tasks numbered from 0 to N-1. Each task takes 1 unit of time to complete. Some tasks depend on the completion of other tasks and can only start once all their prerequisite tasks are finished. You are given a list of dependency pairs (a, b), meaning task a must be completed before task b can start.

You have unlimited resources and can run multiple tasks in parallel as long as their dependencies are satisfied. Your task is to find the minimum time required to complete all tasks.

Function Description:  
Implement the function minimumTimeToCompleteTasks with parameters:  
- N: integer, total number of tasks  
- M: integer, number of dependency pairs  
- dependencies: list of pairs (a, b) where task a must be completed before task b

Return:  
- int: minimum time to complete all tasks

Constraints:  
- 1 ≤ N ≤ 10^5  
- 0 ≤ M ≤ 10^5  
- 0 ≤ a, b < N

Sample Input:  
5 4  
0 1  
1 2  
0 3  
3 4

Sample Output:  
3

Explanation:  
- Task 0 starts at time 1  
- Tasks 1 and 3 depend on task 0, so they start at time 2  
- Task 2 depends on 1, and task 4 depends on 3, so they start at time 3  
Thus, the minimum time to complete all tasks is 3.""",

"""Rotten Oranges

You are given an N x M grid representing a storage area for oranges. Each cell in the grid can be:  
- 0: empty cell  
- 1: fresh orange  
- 2: rotten orange  

A rotten orange at position (i, j) spreads rot to its adjacent fresh oranges (up, down, left, right) every minute. The rotting process happens simultaneously for all rotten oranges at each time step.  

Your task is to determine the minimum time required for all fresh oranges to become rotten. If at least one fresh orange cannot rot, return -1.

Function Description:  
Implement the function minTimeToRottenOranges with parameters:  
- int N: number of rows in the grid  
- int M: number of columns in the grid  
- int[][] grid: a 2D array representing the orange states

Returns:  
- int: minimum minutes for all fresh oranges to rot, or -1 if impossible.""",
"""
Implement a prototype for a text editor application with the following functionalities:

Command  
Actions:  
- ["Insert", s]: Insert the string s at the current cursor position. The cursor moves right by the length of s.  
- ["Left", x]: Move the cursor x positions to the left, but not past the start of the string.  
- ["Right", x]: Move the cursor x positions to the right, but not past the end of the string.  
- ["Backspace", x]: Remove x characters immediately to the left of the cursor, moving the cursor left accordingly.  
- ["Delete", x]: Remove x characters immediately to the right of the cursor. Cursor position does not change.  
- ["Print", x]: If the cursor is at position m, print all characters from index m - x to m + x (inclusive), adjusting for string boundaries.

Given a 2D array of commands of size n x 2, perform the operations starting from an empty string and cursor at position 0. For each "Print" command, record the resulting substring. Return all printed substrings as an array, in the order they are printed.

Note: The second argument in commands is always a string and should be converted to integer where applicable.

Function Description  
Complete the function getPrintedStrings with parameter:  
commands[n][2]: list of commands to execute.

Returns  
string[]: list of printed strings from "Print" commands.

Constraints  
- 1 ≤ n ≤ 5000  
- Sum of lengths of all inserted strings ≤ 5 * 10^3  
- First inserted string length ≤ 100, subsequent insertions ≤ 25  
- All strings contain only lowercase English letters.

Input Format For Custom Testing  
- First line: integer n, number of commands  
- Second line: integer 2  
- Next n lines: two space-separated strings commands[i][0] and commands[i][1]

Sample Case 0

Input:  
7  
2  
Insert addthis  
Print 5  
Left 4  
Right 2  
Backspace 1  
Delete 1  
Print 10

Output:  
dthis  
addts

Explanation:  
1. Insert "addthis": string = "addthis", cursor = 7  
2. Print 5: substring from 7 - 5 = 2 to 7 + 5 = 12 → "dthis"  
3. Left 4: cursor moves from 7 to 3  
4. Right 2: cursor moves from 3 to 5  
5. Backspace 1: remove 1 char left of cursor → string = "addtis", cursor = 4  
6. Delete 1: remove 1 char right of cursor → string = "addts", cursor = 4  
7. Print 10: substring from max(0, 4 - 10) = 0 to min(len, 4 + 10) = 9 → "addts"

Sample Case 1

Input:  
7  
2  
Insert present  
Print 5  
Left 4  
Insert test  
Print 8  
Delete 4  
Print 7

Output:  
esent  
pretestsent  
pretest

Explanation:  
1. Insert "present": string = "present", cursor = 7  
2. Print 5: substring 7 - 5 = 2 to 7 + 5 = 12 → "esent"  
3. Left 4: cursor = 3  
4. Insert "test": string = "pretestsent", cursor = 7  
5. Print 8: substring 7 - 8 = -1 to 7 + 8 = 15 → "pretestsent"  
6. Delete 4: remove 4 chars right of cursor → string = "pretest", cursor = 7  
7. Print 7: substring max(0, 7 - 7) = 0 to min(len, 7 + 7) = 14 → "pretest"
""",

"""You've been asked to program a bot for a popular bank that will automate the management of incoming requests. Every request has its own timestamp in seconds, and it is guaranteed that all requests come sequentially, i.e. the timestamp is strictly increasing. There are two types of incoming requests: 

. deposit <timestamp> <holder_id> <amount> - request to deposit <amount> amount of money in the <holder_id> account; 

. withdraw <timestamp> <holder_id> <amount> - request to withdraw <amount> amount of money from the <holder_id> account. As a bonus, the bank also provides a cashback policy - 2% of the withdrawn amount rounded down to the nearest integer will be returned to the account exactly 24 hours after the request timestamp. If the cashback and deposit/withdrawal happen at the same timestamp, assume cashback happens earlier.

Your system should also handle invalid requests. There are two types of invalid requests: 

. invalid account number; 

. withdrawal of a larger amount of money than is currently available.

For the given list of initial balances and requests, return the state of balances straight after the last request has been processed, or an array of a single element [-<request_id>] (please note the minus sign), where <request_id> is the 1-based index of the first invalid request. Note that cashback requests which haven't happened before the last request timestamp should be ignored.

Example

Example 1: For balances = [1000, 1500] and requests = ["withdraw 1613327630 2 480", "withdraw 1613327644 2 800", "withdraw 1614105244 1 100", "deposit 1614108844 2 200", "withdraw 1614108845 2 150"], the output should be solution(balances, requests) = [900, 295].

Explanation: Here are the states of balances after each request:

. Initially: [1000, 1500]; 
. "withdraw 1613327630 2 480": [1000, 1020]; 
. "withdraw 1613327644 2 800": [1000, 220]; 
. At 1613414030 the 2nd account will receive the cashback of 480 * 0.02 = 9.6, which is rounded down to 9: [1000, 229]; 
. At 1613414044 the 2nd account will receive the cashback of 800 * 0.02 = 16: [1000, 245]; 
. "withdraw 1614105244 1 100": [900, 245]; 
. At 1614191644 the 1st account will receive cashback of 2: [902, 245]; 
. "deposit 1614108844 2 200": [902, 445]; 
. "withdraw 1614108845 2 150": [902, 295]; 
. Final state: [902, 295].

Example 2: For balances = [20, 1000, 500, 40, 90] and requests = ["deposit 1613327630 3 400", "withdraw 1613327635 1 20", "withdraw 1613327651 1 50", "deposit 1613327655 1 50"], the output should be solution(balances, requests) = [-3].

Explanation: Here are the states of balances after each request:

. Initially: [20, 1000, 500, 40, 90]; 
. "deposit 1613327630 3 400": [20, 1000, 900, 40, 90]; 
. "withdraw 1613327635 1 20": [0, 1000, 900, 40, 90]; 
. "withdraw 1613327651 1 50": it is not possible to withdraw 50 from the 1st account, so the request is invalid; 
. The rest of the requests are not processed.

Input/Output

. [execution time limit] 4 seconds (py3) 
. [memory limit] 1 GB 
. [input] array.integer balances: Array of integers, where balances[i] is the amount of money in the (i + 1)th account.

Guaranteed constraints: 1 ≤ balances.length < 100
"""
        ]


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
        options.add_argument("--headless")

        driver = uc.Chrome(options=options, version_main=138)
        print("✓ Successfully created driver with Chrome 138")
        return driver
    except Exception as e:
        print(f"✗ Chrome 138 failed: {e}")

    try:
        options = uc.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless")
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
                 with open("all_responses.txt", "a", encoding="utf-8") as f:
                    f.write("i+1 \n\n"+copied + "\n\n")  # optional: add newline between entries



                

            except Exception as e:
                print(f"✗ Error clicking button {i + 1}: {e}")

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


def main():
    driver = setup_driver()
    try:
        print("Opening ChatGPT...")
        driver.get("https://chat.openai.com/")
        wait_for_page_load(driver)
        handle_stay_logged_out(driver)
        time.sleep(5)

       

        success_count = 0
        for i, prompt in enumerate(prompts, 1):
            print(f"\n--- Sending prompt {i}/{len(prompts)} ---")
            if send_prompt(driver, prompt):
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
