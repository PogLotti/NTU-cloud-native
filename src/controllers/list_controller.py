# list_controller.py

class ListingController:
    def __init__(self, service):
        self.service = service

    def create_listing(self, username, title, description, price, category):
        return self.service.create_listing(username, title, description, price, category)

    def get_listing(self, username, listing_id):
        return self.service.get_listing(username, listing_id)

    def delete_listing(self, username, listing_id):
        return self.service.delete_listing(username, listing_id)
    
    def update_listing(self, username, listing_id):
        pass