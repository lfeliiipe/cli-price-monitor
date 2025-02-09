import argparse
import csv
import sys

PRODUCTS_DIRECTORY = ".persisted/"
PRODUCTS_FILE = "products_list.csv"

def main() -> None:
    
    # Needs one of 3 mutually exclusive options 
    parser = argparse.ArgumentParser(description="Monitor product prices")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-a", "--add", action="extend", nargs="+", help="Add one or more products", type=str)
    group.add_argument("-f", "--fetch", action="store_true", help="Fetch prices for listed products")
    group.add_argument("-l", "--list", action="store_true", help="List products")
    args = parser.parse_args()

    if args.add:
        products: list = add_products(args.add)
        for product in products:
            print(product)

    elif args.fetch:
        fetch()

    elif args.list:

        products: list = list_products()
        if len(products) == 0:
            print("No products yet")
            return

        for product in products:
            print(product)


def add_products(products: list) -> list:
    
    try:
        file = open(f"{PRODUCTS_DIRECTORY}{PRODUCTS_FILE}", "a")
    except FileNotFoundError:
        sys.exit(f"File not found in {PRODUCTS_DIRECTORY}{PRODUCTS_FILE}")

    for product in products:
        file.write(f"{product}\n")
    file.close()

    return list_products()


def fetch():
    ...


def list_products() -> list:
    
    try:
        file = open(f"{PRODUCTS_DIRECTORY}{PRODUCTS_FILE}")
    except FileNotFoundError:
        sys.exit(f"File not found in {PRODUCTS_DIRECTORY}{PRODUCTS_FILE}")
    
    return list(map(str.strip, file))


if __name__ == "__main__":
    main()