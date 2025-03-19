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

        # 計算每個分類的數量
        cat_count = {category: len(listings) for category, listings in self.categories.items()}

        # 先按數量排序，再按字母倒序排列
        return max(sorted(cat_count.keys(), reverse=True), key=cat_count.get)

    def remove_listing_from_category(self, category, listing_id):
        if category not in self.categories:
            return  # 沒有該分類，什麼都不做

        # 從分類中移除對應的 listing_id
        self.categories[category] = [
            listing for listing in self.categories[category] if listing[0] != listing_id
        ]
