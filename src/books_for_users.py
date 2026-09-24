import csv
import json
from pathlib import Path
from typing import Dict, List, Union

BASE_DIR = Path(__file__).resolve().parent.parent

def read_json(filename: str) -> Union[list, dict]:
    """Читает JSON файл и возвращает данные"""
    file_path = BASE_DIR / "data" / filename
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def read_csv(filename: str) -> List[Dict]:
    """Читает CSV как список словарей"""
    file_path = BASE_DIR / "data" / filename
    with open(file_path, 'r', encoding='utf-8', newline='\n') as f:
        reader = csv.DictReader(f)
        return list(reader)


def write_json(filename: str, data: Union[list, dict]) -> None:
    """Записывает данные в JSON файл"""
    file_path = BASE_DIR / "data" / filename
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    books_data = read_csv("books.csv")
    users_data = read_json("users.json")

    total_books = len(books_data)
    total_users = len(users_data)

    base_books_per_user = total_books // total_users
    leftover_books = total_books % total_users

    result_structure = []
    book_pointer = 0

    for i in range(total_users):
        user = users_data[i]

        if i < leftover_books:
            chunk_size = base_books_per_user + 1
        else:
            chunk_size = base_books_per_user

        raw_books_chunk = books_data[book_pointer: book_pointer + chunk_size]
        book_pointer = book_pointer + chunk_size
        user_books = []

        for row in raw_books_chunk:
            book = {
                "title": row.get("Title") or row.get("title"),
                "author": row.get("Author") or row.get("author"),
                "pages": int(row.get("Pages") or row.get("pages") or 0),
                "genre": row.get("Genre") or row.get("genre")
            }
            user_books.append(book)

        new_user = {
            "name": user.get("name"),
            "gender": user.get("gender"),
            "address": user.get("address"),
            "age": user.get("age"),
            "books": user_books
        }
        result_structure.append(new_user)

    write_json("result.json", result_structure)

