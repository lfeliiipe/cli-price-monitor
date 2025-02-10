import argparse
import csv
import sys
from persist import Persist

def main() -> None:
    
    # Needs one of 3 mutually exclusive options 
    parser = argparse.ArgumentParser(description="Monitor product prices")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-a", "--add", action="extend", nargs="+", help="Add one or more products", type=str)
    group.add_argument("-f", "--fetch", action="store_true", help="Fetch prices for listed products")
    group.add_argument("-l", "--list", action="store_true", help="List products")
    args = parser.parse_args()

    p: Persist = Persist(".persisted/products_list.csv")

    # Menu
    if args.add:
        products: list = add_products(args.add, p)
        print("Updated Products List:")
        for product in products:
            print(product)

    elif args.fetch:
        fetch()

    elif args.list:

        products: list = list_products(p)
        if len(products) == 0:
            print("No products yet")
            return

        for product in products:
            print(product)


def add_products(new_products: list, p: Persist) -> list:

    file = p.open_to("a")
    for new_product in new_products:
        file.write(f"{new_product}\n")
    file.close()

    return list_products(p)


def fetch():
    ...


def list_products(p: Persist) -> list:

    file = p.open_to("r")
    products: list = [ line.strip() for line in file ]
    file.close()

    return products


if __name__ == "__main__":
    main()