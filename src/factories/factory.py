from controllers.user_controller import UserController
from controllers.list_controller import ListingController
from controllers.category_controller import CategoryController
from repositories.user_repo import UserRepository
from repositories.list_repo import ListingRepository
from repositories.category_repo import CategoryRepository
from services.user_service import UserService
from services.list_service import ListingService
from services.category_service import CategoryService

class ServiceFactory:
    def __init__(self):
        # Repo
        self.user_repository = UserRepository()
        self.category_repository = CategoryRepository()
        self.listing_repository = ListingRepository(self.category_repository)

        # Service
        self.user_service = UserService(self.user_repository)
        self.category_service = CategoryService(self.category_repository, self.listing_repository, self.user_service)
        self.listing_service = ListingService(self.listing_repository, self.user_service, self.category_service)

        # Controller
        self.user_controller = UserController(self.user_service)
        self.listing_controller = ListingController(self.listing_service)
        self.category_controller = CategoryController(self.category_service)

    def get_user_controller(self):
        return self.user_controller

    def get_listing_controller(self):
        return self.listing_controller
    
    def get_category_controller(self):
        return self.category_controller