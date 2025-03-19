
# main.py
import sys
import shlex
from factories.factory import ServiceFactory

def main():

    service_factory = ServiceFactory()
    user_controller = service_factory.get_user_controller()
    listing_controller = service_factory.get_listing_controller()
    category_controller = service_factory.get_category_controller()

    # Display prompt and process commands from STDIN.
    sys.stdout.write("# ")
    sys.stdout.flush()

    for line in sys.stdin:
        try:
            line = line.strip()
            if not line:
                continue

            # Use shlex.split to properly handle quoted arguments
            tokens = shlex.split(line)
            command = tokens[0].upper()

            if command == "REGISTER" and len(tokens) == 2:
                print(user_controller.register(tokens[1]))

            elif command == "CREATE_LISTING" and len(tokens) == 6:
                username, title, description, price_str, category = tokens[1:]
                print(listing_controller.create_listing(username, title, description, int(price_str), category))

            elif command == "GET_LISTING" and len(tokens) == 3:
                print(listing_controller.get_listing(tokens[1], int(tokens[2])))

            elif command == "DELETE_LISTING" and len(tokens) == 3:
                print(listing_controller.delete_listing(tokens[1], int(tokens[2])))

            elif command == "GET_CATEGORY" and len(tokens) == 3:
                print(category_controller.get_category(tokens[1], tokens[2]))

            elif command == "GET_TOP_CATEGORY" and len(tokens) == 2:
                print(category_controller.get_top_category(tokens[1]))


        except Exception as e:
            print(f"Error - invalid command {e}")

        sys.stdout.write("# ")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
