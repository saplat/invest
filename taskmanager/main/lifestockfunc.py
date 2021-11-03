import pandas as pd
from bs4 import BeautifulSoup

class Lifestockfunc():
    @staticmethod
    def web_content_div(web_content, class_path):
        web_content_div = web_content.find_all('div', {'class': class_path})
        try:
            spans = web_content_div[0].find_all('span')
            texts = [span.get_text() for span in spans]
        except IndexError:
            texts = []
        return texts