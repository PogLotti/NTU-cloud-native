# category_service.py

class CategoryService:
    def __init__(self, category_repo, listing_repo, user_service):

        self.category_repo = category_repo
        self.listing_repo = listing_repo
        self.user_service = user_service

    def add_listing_to_category(self, category, listing_id):

        listing = self.listing_repo.get_listing(listing_id)
        if listing:
            self.category_repo.add_listing_to_category(category, listing_id, listing)

    def get_listings_by_category(self, username, category):

        if category not in self.category_repo.categories:
            return "Error - category not found"
        
        if not self.user_service.user_exists(username):
            return "Error - user not found"

        listing_ids = self.category_repo.get_listings_by_category(category)

        listings = [self.listing_repo.get_listing(lid) for lid in listing_ids]
        result_lines = [
            f"{l.title}|{l.description}|{l.price}|{l.created_at}|{l.category}|{l.username}" for l in listings
        ]
        return "\n".join(result_lines)
    
    def get_top_category(self, username):

        if not self.user_service.user_exists(username):
            return "Error - unknown user"

        top_category = self.category_repo.get_top_category()
        if top_category:
                return ", ".join(top_category)  # Join the list into a string
        else:
            return "Error - category not found"
