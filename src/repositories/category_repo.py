# category_repo.py

class CategoryRepository:
    def __init__(self, ):
        self.categories = {}

    def add_listing_to_category(self, category, listing_id, listing):

        if category not in self.categories:
            self.categories[category] = []
        self.categories[category].append((listing_id, listing.created_at))
        self.categories[category].sort(key=lambda x: x[1], reverse=True)
        
    def get_listings_by_category(self, category):
        
        return [listing[0] for listing in self.categories[category]] # return listing_id
        
    def get_top_category(self):
        if not self.categories:
            return None

        cat_count = {category: len(listings) for category, listings in self.categories.items()}

        max_count = max(cat_count.values())
        top_categories = [category for category, count in cat_count.items() if count == max_count]

        return top_categories
    
    def remove_listing_from_category(self, category, listing_id):
        if category not in self.categories:
            return  

        self.categories[category] = [
            listing for listing in self.categories[category] if listing[0] != listing_id
        ]
