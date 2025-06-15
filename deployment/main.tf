terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "3.0.2"
    }
  }
}

resource "docker_image" "market-scraper" {
  name         = "market-scraper:latest"
  keep_locally = true
}

resource "docker_container" "market-scraper" {
  name  = "flask_app"
  image = docker_image.market-scraper.image_id

  ports {
    internal = 8080
    external = 8080
  }
}