from flask import Flask, render_template, request
import requests

import requests
category = 'happiness'
api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
response = requests.get(api_url, headers={'X-Api-Key': 'vi8M2OJUeBGJRsWwJ6+AOA==VPVH5BvCfzJjIKBO'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)

# app = Flask(__name__)
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#    news = None
#    if request.method == 'POST':
#        news = get_news()
#    return render_template("index.html", news=news)
# def get_news():
#    api_key = "vi8M2OJUeBGJRsWwJ6+AOA==VPVH5BvCfzJjIKBO"
#    url = f"https://api.api-ninjas.com/v1/quotes?category=happiness"
#    response = requests.get(url)
#    return response.json().get("articles", [])
#
#
#
# if __name__ == '__main__':
#    app.run(debug=True)