from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# API ключ для доступа к публичному API
api_key = "vi8M2OJUeBGJRsWwJ6+AOA==VPVH5BvCfzJjIKBO"

# Функция для перевода текста на русский язык
def translate_to_russian(text):
    translate_url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": "en",
        "tl": "ru",
        "dt": "t",
        "q": text
    }
    try:
        response = requests.get(translate_url, params=params)
        if response.status_code == 200:
            # Ответ возвращается в виде вложенных списков
            translated_text = response.json()[0][0][0]
            return translated_text
        else:
            return "Ошибка перевода"
    except Exception as e:
        return f"Произошла ошибка при переводе: {e}"

# Функция для получения случайной цитаты из публичного API
def get_random_quote():
    category = 'happiness'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    try:
        response = requests.get(api_url, headers={'X-Api-Key': api_key})
        if response.status_code == 200:
            data = response.json()
            if data:
                quote = data[0]['quote']
                author = data[0]['author']
                # Перевод цитаты на русский
                quote_ru = translate_to_russian(quote)
                return quote_ru, author
            else:
                return "No quotes found for this category.", "Unknown"
        else:
            return f"Error: Received status code {response.status_code}", "Unknown"
    except Exception as e:
        return f"An error occurred: {e}", "Unknown"

@app.route('/')
def index():
    quote, author = get_random_quote()
    return render_template('index.html', quote=quote, author=author)

if __name__ == '__main__':
    app.run(debug=True)
