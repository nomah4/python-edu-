import requests
from bs4 import BeautifulSoup

# Шаг 1: Получение содержимого веб-страницы
url = "https://stepik.org/media/attachments/lesson/209719/2.html"
response = requests.get(url)
content = response.text

# Шаг 2: Парсинг HTML-кода для поиска текста внутри тегов <code></code>
soup = BeautifulSoup(content, 'html.parser')
codes = soup.find_all('code')

# Шаг 3: Сбор всех текстовых значений из тегов <code></code>
code_texts = [code.text.strip() for code in codes]

# Шаг 4: Подсчет количества повторений каждого значения и сортировка
from collections import Counter
counter = Counter(code_texts)
sorted_counter = dict(sorted(counter.items()))

# Вывод результата
for text, count in sorted_counter.items():
    print(f"{text}: {count}")