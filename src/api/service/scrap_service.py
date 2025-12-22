
from typing import Dict
from src.anticorruption.books_scrape_script import AnticorruptionBooksScraping
from src.interfaces.application.interface_scrap_application import IScrapApplication
from src.interfaces.service.interface_service_scrap import IServiceScrap

class ScrapService(IServiceScrap):

    def __init__(self, application: IScrapApplication):
        self.application = application

    def start_scraping(self) -> None:
        return self.application.start_scraping()

    def get_status(self) -> Dict:
        return self.application.get_status()