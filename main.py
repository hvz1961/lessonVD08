from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
   news = None
   if request.method == 'POST':
       news = get_news()
   return render_template("index.html", news=news)
def get_news():
   api_key = "7aaf274108274b0b9479c8fde7022bd9"
   url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
   response = requests.get(url)
   return response.json().get("articles", [])



if __name__ == '__main__':
   app.run(debug=True)






