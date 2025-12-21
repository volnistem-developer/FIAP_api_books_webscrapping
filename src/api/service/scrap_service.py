
from src.anticorruption.books_scrape_script import AnticorruptionBooksScraping
from src.interfaces.application.interface_scrap_application import IScrapApplication

class ScrapService:

    def __init__(self, application: IScrapApplication):
        self.application = application

    def start_scraping(self):
        return self.application.start_scraping()

    def get_status(self):
        return self.application.get_status()