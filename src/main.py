import os
from dotenv import load_dotenv

# 1. Загружаем переменные окружения из файла .env
load_dotenv()

def print_author():
    # 2. Читаем значение переменной AUTHOR из окружения
    author = os.getenv("AUTHOR")
    
    # 3. Печатаем результат
    print(f"Автор проекта: {author}")

# 4. Вызываем функцию, чтобы проверить её работу
if __name__ == "__main__":
    print_author()
