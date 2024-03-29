from src import Gmaps

queries = [
   "Forsyth Fire Escape"
]

Gmaps.places(queries, scrape_reviews=True, reviews_max=Gmaps.ALL_REVIEWS)