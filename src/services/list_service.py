# list_service.py

class ListingService:
    def __init__(self, listing_repo, user_service, category_service):

        self.listing_repo = listing_repo
        self.user_service = user_service
        self.category_service = category_service

    def create_listing(self, username, title, description, price, category):
        if not self.user_service.user_exists(username):
            return "Error - user not found"

        listing = self.listing_repo.create_listing(username, title, description, price, category) # obj

        self.category_service.add_listing_to_category(category, listing.listing_id)

        return str(listing.listing_id)
    
    def get_listing(self, username, listing_id):

        if not self.user_service.user_exists(username):
            return "Error - user not found"
        
        listing = self.listing_repo.get_listing(listing_id)
        if not listing:
            return "Error - listing not found"

        return f"{listing.title}|{listing.description}|{listing.price}|{listing.created_at}|{listing.category}|{listing.username}"
    
    def delete_listing(self, username, listing_id):
        if not self.user_service.user_exists(username):
            return "Error - unknown user "

        listing = self.listing_repo.get_listing(listing_id)
        if not listing:
            return "Error - listing not found"

        if listing.username != username:
            return "Error - listing owner mismatch"
        self.listing_repo.delete_listing(username, listing_id)
        return "Success"