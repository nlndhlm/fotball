from selenium import webdriver
import time
import pandas as pd

# datainnhenting
driver = webdriver.Firefox()
driver.get("https://understat.com/league/EPL")
 
html = driver.page_source
time.sleep(2)

driver.quit()

# databearbeiding
data = pd.read_html(html)

teams = data[0]     # lagdata
players = data[1]   # spillerdata

players["xG"].str.split("+", expand=False)

print(players[["Player", "xG"]])
