from pathlib import Path

from bs4 import BeautifulSoup

from app.entities.constituent import Constituent
from app.entities.market import Market

project_root = Path(__file__).resolve().parent.parent.parent

class StockMarketService:

    def fetch_market_constituents(self, market: Market) -> list[Constituent]:
        """ Loads the constituents of a provided stock market

        @param market: Name of a stock market such as "nasdaq" or "dax".
        @return: List of stocks.
        """
        with open(project_root/"scripts/temp.html", 'r', encoding='utf-8') as file:
            markup = file.read()

        if market == Market.NASDAQ:
            return self.fetch_nasdaq_constituents(markup=markup)
        if market == Market.DAX:
            return self.fetch_dax_constituents(markup=markup)

        raise ValueError(f"Unsupported market: {market}")

    @staticmethod
    def fetch_nasdaq_constituents(markup: str) -> list[Constituent]:
        """ Fetches all constituents of the Nasdaq-100 by iterating over Nasdaq's
            Wikipedia article.
        """
        soup = BeautifulSoup(markup=markup, features='html.parser')

        table = soup.find(name="table",
                          attrs={"id": "constituents"}).find_all('td')

        cells: list = list(map(lambda cell: cell.text.strip('\n'), table))

        constituents = []

        for i, _ in enumerate(cells[: -3]):
            if i % 4 == 0:
                constituent = Constituent(
                    symbol=cells[i],
                    name=cells[i + 1],
                    sector=cells[i + 2],
                    subIndustry=cells[i + 3]
                )
                constituents.append(constituent)

        return constituents

    @staticmethod
    def fetch_dax_constituents(markup: str) -> list[Constituent]:
        """
        Fetches all constituents of the German blue-chip index DAX by iterating
        over the DAX' Wikipedia article. The function returns a tuple of a share's
        name, stock ticker symbol and industry, such as ('Adidas', 'ADS.DE',
        'Apparel').
        """
        soup = BeautifulSoup(markup=markup, features='html.parser')

        table = soup.find(name="table",
                          attrs={"id": "constituents"}).find_all('td')

        cells: list = list(map(lambda cell: cell.text.strip('\n'), table))

        constituents = []

        for i, _ in enumerate(cells[: -4]):
            if i % 7 == 0:
                constituent = Constituent(
                    symbol=cells[i + 0],
                    name=cells[i + 2],
                    sector=cells[i + 3],
                )
                constituents.append(constituent)

        return constituents
