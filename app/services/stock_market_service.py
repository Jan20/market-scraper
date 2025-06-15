import os

import requests
from bs4 import BeautifulSoup

from app.entities.market import Constituent


class StockMarketService:

    def fetch_market_constituents(self, market: str) -> list[Constituent]:
        """ Loads the constituents of a provided stock market

        @param market: Name of a stock market such as "nasdaq" or "dax".
        @return: List of stocks.
        """
        if market == "nasdaq":
            return self.fetch_nasdaq_constituents()
        if market == "dax":
            return self.fetch_dax_constituents()

    @staticmethod
    def fetch_nasdaq_constituents() -> list[Constituent]:
        """ Fetches all constituents of the Nasdaq-100 by iterating over Nasdaq's
            Wikipedia article.
        """
        nasdaq_url = os.getenv("NASDAQ_URL")
        markup: str = requests.get(nasdaq_url).text
        soup: BeautifulSoup = BeautifulSoup(markup=markup, features='html.parser')

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
    def fetch_dax_constituents() -> list[Constituent]:
        """
        Fetches all constituents of the German blue-chip index DAX by iterating
        over the DAX' Wikipedia article. The function returns a tuple of a share's
        name, stock ticker symbol and industry, such as ('Adidas', 'ADS.DE',
        'Apparel').
        """
        dax_url = os.getenv("DAX_URL")

        markup: str = requests.get(dax_url).text
        soup: BeautifulSoup = BeautifulSoup(markup=markup, features='html.parser')

        table = soup.find(name="table",
                          attrs={"id": "constituents"}).find_all('td')

        cells: list = list(map(lambda cell: cell.text.strip('\n'), table))

        constituents = []

        for i, _ in enumerate(cells[: -4]):
            if i % 7 == 0:
                constituent = Constituent(
                    symbol=cells[i + 3],
                    name=cells[i + 1],
                    sector=cells[i + 2],
                )
                constituents.append(constituent)

        return constituents
