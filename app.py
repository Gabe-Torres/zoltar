from selenium import webdriver
from selenium.webdriver.common.by import By
from flask import Flask, render_template
from selenium.webdriver.chrome.service import Service



PATH = "/Users/gabrieltorres/Downloads/chromedriver_mac_arm64/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("http://127.0.0.1:5000")

driver.close()

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)