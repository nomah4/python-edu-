from bs4 import BeautifulSoup
import requests

# Загрузка HTML-кода страницы
url = "https://stepik.org/media/attachments/lesson/209723/4.html"
response = requests.get(url)
html_content = response.text

# Парсинг HTML-кода с помощью BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Поиск таблицы на странице
table = soup.find('table')

if table:
    # Извлечение всех чисел из ячеек таблицы
    numbers = []
    for row in table.findAll('tr'):
        for cell in row.findAll('td'):
            try:
                number = float(cell.text.strip())
                numbers.append(number)
            except ValueError:
                continue

    # Суммирование чисел
    total_sum = sum(numbers)

    print(total_sum)
else:
    print("Таблица не найдена на странице.")