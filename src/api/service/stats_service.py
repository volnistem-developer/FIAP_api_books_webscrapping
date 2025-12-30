from src.dtos.stats_dto import AvailabilityStatsDTO, CategoryStatsDTO, OverviewDTO
from src.interfaces.application.interface_stats_application import IStatsApplication
from src.interfaces.service.interface_service_stats import IStatsService


class StatsService(IStatsService):

    def __init__(self, application: IStatsApplication):
        self.application = application

    def get_overview(self):
        data = self.application.get_overview()

        return OverviewDTO(
            total_books=data["total_books"],
            available_books=data["available_books"],
            unavailable_books=data["unavailable_books"],
            average_rating=round(data["average_rating"], 2),
            average_price_brl=round(data["average_price_brl"], 2),
            last_scrap_execution=data["last_scrap_execution"],
        )
    
    
    def get_categories_stats(self):
        stats = self.application.get_categories_stats()

        return [
            CategoryStatsDTO(
                category=s["category"],
                total_books=s["total_books"],
                available_books=s["available_books"],
                average_rating=round(s["average_rating"], 2),
                average_price_brl=round(s["average_price_brl"], 2),
            )
            for s in stats
        ]
    
    
    def get_availability_stats(self):
        stats = self.application.get_availability_stats()

        total = stats["total_books"]

        availability_rate = (
            round((stats["available_books"] / total) * 100, 2)
            if total > 0 else 0
        )
        
        return AvailabilityStatsDTO(
            total_books=total,
            available_books=stats["available_books"],
            unavailable_books=stats["unavailable_books"],
            availability_rate=availability_rate,
        )