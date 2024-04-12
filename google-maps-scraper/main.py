from src import Gmaps

queries = [
   "Golden Wuish"
]

Gmaps.places(queries, scrape_reviews=True, reviews_max=Gmaps.ALL_REVIEWS)