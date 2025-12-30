from decimal import ROUND_HALF_UP, Decimal
import os
from pathlib import Path
import re
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup, Tag
import requests
from src.exceptions.exceptions import BookScrapingApiError
from src.infraestrutura.config.env_config import ENV_CONFIG

SRC_DIR = Path(__file__).resolve().parents[2]
IMAGES_DIR = SRC_DIR / "public" / "images" / "books"

class AnticorruptionBooksScraping():

    def __init__(self):
        self.__url = ENV_CONFIG['URL_TO_SCRAPE']
    
    def scrap_books(self):
        catalog = []
        categories = self.get_categories()

        for category in categories: 
            books = self.get_books_from_category(category)
            catalog.extend(books)
        
        return catalog
    
    def get_books_from_category(self, category: dict):
        books = []
        page_url = category['url']

        while True:
            response = requests.get(page_url)

            if response.status_code == 404:
                break

            site = BeautifulSoup(response.text, 'html.parser')

            print(f"Categoria: {category['name']} | Página: {page_url}")

            for book in site.select('article.product_pod'):
                title = book.find('h3').find('a').get('title')

                rating = self.__extract_rating(book)
                price = self.__extract_price(book)
                slug = self.__extract_book_slug(book)
                image_url = self.__extract_image_url(book, self.__url)
                available = self.__extract_disponibility(book)

                image_path = None
                if image_url:
                    absolute_path = self.__dowload_image(image_url, slug, IMAGES_DIR)
                    if absolute_path:
                        image_path = str(
                            Path(absolute_path).relative_to(SRC_DIR).as_posix()
                        )

                books.append({
                    "name": title,
                    "slug": slug,
                    "category": category["name"],
                    "rating": rating,
                    "original_price": self.__convert_price_to_cents(price),
                    "image_path": image_path,
                    "available": available
                })

            next_page = site.select_one('li.next a')

            if not next_page:
                break

            page_url = urljoin(page_url, next_page.get("href"))

        return books

    def get_categories(self):
        response = requests.get(self.__url)
        site = BeautifulSoup(response.text, "html.parser")

        categories = []
        links = site.select("ul.nav-list ul li a")

        for link in links:
            categories.append({
                "name": link.text.strip(),
                "url": urljoin(self.__url, link.get("href"))
            })

        return categories

    def __extract_price(self, book: Tag):
        price_tag = book.find('p', class_='price_color')

        if not price_tag:
            return None
        
        raw_price = price_tag.get_text(strip=True)

        price_number = float(re.sub(r'[^\d.]', '', raw_price))

        return price_number

    def __extract_rating(self, book: Tag):
        rating_tag = book.find('p', class_='star-rating')

        if not rating_tag:
            return 0
        
        list_of_class = rating_tag.get('class', [])

        rating_classes = [c for c in list_of_class if c != 'star-rating']

        rating_str = rating_classes[0] if rating_classes else None

        return self.__convert_rating_to_number(rating_str)
    
    def __extract_image_url(self, book: Tag, base_url: str):
        img = book.find("img")

        if not img: 
            return None
        
        return urljoin(self.__url, img.get("src"))

    def __extract_book_slug(self, book: Tag):
        href = book.find('h3').find('a').get('href')
        path = urlparse(href).path
        parts = Path(path).parts

        return parts[-2]

    def __extract_disponibility(self, book:Tag):
        element = book.find('p', class_="availability")

        if not element:
            return False
        
        classes = element.get('class', [])
        text = element.get_text(strip=True).lower()

        if "instock" in classes:
            return True
        
        return "in stock" in text

    def __convert_rating_to_number(self, number_as_string: str) -> int:

        match number_as_string:
            case "One": return 1
            case "Two": return 2
            case "Three": return 3
            case "Four": return 4
            case "Five": return 5
            case _: return 0

    def __dowload_image(self, image_url: str, slug: str, folder: Path):
        folder.mkdir(parents=True, exist_ok=True)

        extension = Path(image_url).suffix or ".jpg"
        file_path = folder / f"{slug}{extension}"

        if file_path.exists():
            return str(file_path)
        
        response = requests.get(image_url, stream=True, timeout=10)

        if response.status_code != 200:
            return None
        
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        return str(file_path)

    def __convert_price_to_cents(self, value:float):
        decimal = Decimal(str(value))
        cents = (decimal * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
        return int(cents)