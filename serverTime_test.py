from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re

# Set up Selenium webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Load the webpage
driver.get("https://www.liberty.edu/")

while True:
    # Execute JavaScript to retrieve the server time
    server_time_script = "return new Date().toLocaleTimeString();"
    server_time = driver.execute_script(server_time_script)

    # Remove non-numeric characters from server_time
    server_time = re.sub(r"[^0-9:]", "", server_time)

    # Extract the hour, minute, and second from the server time
    time_components = server_time.split(":")
    if len(time_components) >= 3:
        server_hour = int(time_components[0])
        server_minute = int(time_components[1])
        server_second = int(time_components[2])
    else:
        print("Failed to extract server time.")

    print("Server time: {:02d}:{:02d}:{:02d}".format(server_hour, server_minute, server_second))

    # Check if the server time is 22:20
    if server_hour == 12 and server_minute == 1:
        # Execute your code here
        print("Hello, it's 12:02!")
        # Take screenshots, perform actions, etc.
        break

# # Close the browser
# driver.quit()
