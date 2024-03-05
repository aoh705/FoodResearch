from src import Gmaps

queries = [
   "Springbone Kitchen"
]

Gmaps.places(queries, scrape_reviews=True, reviews_max=Gmaps.ALL_REVIEWS)