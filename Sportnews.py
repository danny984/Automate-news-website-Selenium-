from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime
import os
import sys

# Preparing script before we convert it to executable
application_path = os.path.dirname(sys.executable)

# get date in format MMDDYYYY
now = datetime.now()
month_day_year = now.strftime("%m%d%Y")


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Headless mode
options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get("https://www.thesun.co.uk/sport/football/")

# Finding the elements

containers= driver.find_elements(By.XPATH,"//div[@class='teaser__copy-container']")

titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(By.XPATH, "./a/span").text
    subtitle = container.find_element(By.XPATH, "./a/h3").text
    link = container.find_element(By.XPATH, "./a").get_attribute('href')
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)


# Exporting data to a CSV file

my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
file_name = f'football_headlines_{month_day_year}.csv'
final_path = os.path.join(application_path, file_name)
df_headlines.to_csv(final_path)

driver.quit()