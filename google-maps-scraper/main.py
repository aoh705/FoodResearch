from src import Gmaps

queries = [
   "Woorijip nyc"
]

Gmaps.places(queries, scrape_reviews=True, reviews_max=Gmaps.ALL_REVIEWS)