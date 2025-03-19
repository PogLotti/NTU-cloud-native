import datetime

class Listing:
    def __init__(self, listing_id, username, title, description, price, category, created_at):
        self.listing_id = listing_id
        self.username = username
        self.title = title
        self.description = description
        self.price = price
        self.category = category
        self.created_at = created_at

class ListingRepository:
    def __init__(self, category_repo):
        self.listings = {}
        self.counter = 100001 # Start listing IDs at 100001
        self.category_repo = category_repo  # CategoryRepository

    def create_listing(self, username, title, description, price, category):
        listing_id = self.counter
        self.counter += 1
        created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        listing = Listing(listing_id, username, title, description, price, category, created_at)
        self.listings[listing_id] = listing
        return listing

    def get_listing(self, listing_id):
        return self.listings.get(listing_id)

    def delete_listing(self, username, listing_id):
    
        if listing_id not in self.listings:
            return False  # listing 不存在，刪除失敗

        listing = self.listings[listing_id]

        # 確保使用者是 Listing 的擁有者
        if listing.username != username:
            return False  # 擁有者不符，刪除失敗
        
        self.category_repo.remove_listing_from_category(listing.category, listing_id)

        # 刪除 listing
        del self.listings[listing_id]

        return True  # 刪除成功