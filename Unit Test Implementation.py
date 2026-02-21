# test_shopping.py

import unittest
from bs4 import BeautifulSoup

# Load HTML from file
with open("shopping.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Parse HTML
soup = BeautifulSoup(html_content, "html.parser")

# Expected product data
expected_products = [
    ("Herems Irelan Tote Bag", "R199.99"),
    ("Novelty Handbag", "R249.99"),
    ("Moschino Essential Pure Leather Handbag", "R179.99"),
    ("Chris Bella Tote Bag", "R299.99"),
    ("Zara Crossbody bag", "R219.99"),
    ("Ted Baker Bag", "R189.99"),
    ("Straw Tote Bag", "R159.99"),
    ("Galaxboy Dome Bag", "R279.99"),
    ("Woven Straw Tote Bag", "R199.99"),
    ("Lacosta Set Bags", "R229.99"),
]

class TestShoppingHTML(unittest.TestCase):

    def test_number_of_products(self):
        products = soup.find_all("div", class_="col-sm-6 col-md-4 col-lg-3")
        self.assertEqual(len(products), 10, "There should be exactly 10 products displayed")

    def test_each_product_has_buy_button(self):
        product_cards = soup.find_all("div", class_="card")
        for card in product_cards:
            button = card.find("button", class_="btn-primary")
            self.assertIsNotNone(button, "Each product should have a Buy button")

    def test_product_titles_and_prices(self):
        product_cards = soup.find_all("div", class_="card")
        for card, (expected_title, expected_price) in zip(product_cards, expected_products):
            title = card.find("h5", class_="card-title").text.strip()
            price = card.find("p", class_="card-text").text.strip()
            self.assertEqual(title, expected_title, f"Product title should be {expected_title}")
            self.assertEqual(price, expected_price, f"Product price should be {expected_price}")

if __name__ == "__main__":
    unittest.main()
