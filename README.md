# Market Scraper

Naive project for scraping the constituents of stock markets from Wikipedia.

## Overview

**market-scraper** is a Python-based tool designed to fetch and process the list of companies (constituents) from various stock market indices, such as DAX and NASDAQ, using data available on Wikipedia.

## Features

- Scrapes up-to-date index constituents from Wikipedia.
- Modular architecture with controllers, entities, and services.
- Easily extendable to support additional indices.
- Docker support for containerized deployment.
- Infrastructure as code with Terraform for deployment.

## Getting Started

### Prerequisites

- Python 3.12+
- [pip](https://pip.pypa.io/en/stable/)
- (Optional) [Docker](https://www.docker.com/)
- (Optional) [Terraform](https://www.terraform.io/)

### Installation

**Step 1:** Clone the repository:

```sh
git clone https://github.com/yourusername/market-scraper.git
cd market-scraper
```

**Step 2:** Create a virtual environment:

```sh
pip install -r requirements.txt
```

**Step 3:** Install dependencies:

```sh
python -m venv venv
```

**Step 4:** Copy the example environment file and configure as needed:

```sh
cp .env.example .env
```

### Usage

#### Run the Scraper

Source the .env file and spin up the project:

```sh
source .env && python main.py
```

#### Fetch DAX or NASDAQ constituents via scripts

```sh
source .env && ./scripts/nasdaq.sh
source .env && ./scripts/nasdaq.sh
```

#### Using Docker

Build and run the container:

```sh
docker build -t market-scraper .
docker run --env-file .env market-scraper
```

#### Infrastructure Deployment

Navigate to the deployment/ directory and use Terraform:

```sh
source .env && cd deployment
terraform init
terraform apply
```

#### Acknowledgements

Wikipedia for providing index constituent data.
