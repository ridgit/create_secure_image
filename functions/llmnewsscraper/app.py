from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = 'https://www.bloomberg.com/canada'  # Remplacez par la source d'actualités que vous voulez scraper
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_title = soup.find('h1', class_='news-title').text
    news_author = soup.find('p', class_='news-author').text
    news_content = soup.find('div', class_='news-content').text
  
    return render_template('home.html', title=news_title, author=news_author, content=news_content)

if __name__ == '__main__':
    app.run(debug=True)
