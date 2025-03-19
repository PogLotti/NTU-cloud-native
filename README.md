# CloudShop - CLI Marketplace  

## Introduction  
CloudShop is a command-line interface (CLI) application that functions as a simple marketplace, enabling users to buy and sell items. It supports essential marketplace operations such as user registration, item listings, retrieving items by category, and deletion of listings. The system is designed with a focus on modularity, extensibility, and clean architecture.  

## Features  
- **User Registration**: Allows unique username registration.  
- **Create Listing**: Users can list items with a title, description, price, and category.  
- **Retrieve Listings**: Fetch details of a specific listing or all listings within a category.  
- **Delete Listings**: Owners can remove their listings.  
- **Get Top Category**: Determines the most popular category based on the highest number of listings.  

## Architecture  

The project is structured into the following components to ensure clear separation of concerns:  

- **`services/`**: Contains business logic and core marketplace functionalities.  
- **`controllers/`**: Handles user commands and interacts with the appropriate services.  
- **`repositories/`**: Manages data persistence and storage operations.  
- **`factories/`**: Provides object creation and dependency management.  

## Installation and Execution  

### Prerequisites  
- Python **3.9+**  

### Setup and Execution  
1. Clone the repository:  
   ```sh
   git clone <repository-url>
   cd NTU-cloud-native
2. Build the Project:
    ```sh
    ./build.sh      # Linux/macOS  
    sh build.sh     # Windows (Using Git Bash)  
3. Running the Application
    ```sh
    ./run.sh      # Linux/macOS  
    sh run.sh     # Windows (Using Git Bash)

## Command-line Examples  

| Command                         | Description                                      |
|----------------------------------|--------------------------------------------------|
| `REGISTER <username>`           | Register a new user                             |
| `CREATE_LISTING <title>`        | Create a new listing                           |
| `DELETE_LISTING <listing_id>`   | Delete a listing                               |
| `GET_LISTING <listing_id>`      | Retrieve listing information                   |
| `GET_CATEGORY <category>`       | Retrieve listings in a category (sorted by time) |
| `GET_TOP_CATEGORY`              | Get the category with the most listings        |
| `EXIT`                          | Exit the application                           |