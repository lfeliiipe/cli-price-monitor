import argparse
import csv
import re
import sys
from persist import Persist

def main() -> None:
    
    # Needs one of 3 mutually exclusive options 
    parser = argparse.ArgumentParser(description="Monitor product prices")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-a", "--add", action="extend", nargs="+", help="Add one or more products", type=str)
    group.add_argument("-r", "--remove", action="store_true", help="Remove product(s)")
    group.add_argument("-l", "--list", action="store_true", help="List products")
    args = parser.parse_args()

    p: Persist = Persist(".persisted/products_list.csv")

    # Add new products
    if args.add:

        products: list = add_products(args.add, p)
        print("Updated Products List:")
        for product in products:
            print(product)

    # List persisted products
    elif args.list:

        products: list = list_products(p)
        if len(products) == 0:
            print("No products yet")
            return

        for product in products:
            print(product)

    # Remove products from persisted list
    elif args.remove:
        
        print("Insert the products' index(es) to be removed")
        print("Example: 2 3 4 12")

        products: list = list_products(p)
        enum_products: enumerate = enumerate(products, start=1)
        for i, product in enum_products:
            print(f"Index: {i}, Product: {product}")

        if to_remove := get_ints(input("\nType here: ")):
            updated_products: list = remove_products(to_remove, products, p)
            print("\nUpdated products:")
            for product in updated_products:
                print(product)
            
            return
        
        print("No matches")


def add_products(new_products: list, p: Persist) -> list:

    file = p.open_to("a")
    for new_product in new_products:
        file.write(f"{new_product}\n")
    file.close()

    return list_products(p)


def get_ints(prompt: str) -> list:

    if matches := re.findall(r"\b(\d+)\b", prompt.strip()):
        return [ int(match) for match in matches ]
    return []

def list_products(p: Persist) -> list:

    file = p.open_to("r")
    products: list = [ line.strip() for line in file ]
    file.close()

    return products


def remove_products(remove_list: list, products: list, p: Persist) -> list:
    
    file = p.open_to("w")
    updated_products: list = [ product for i, product in enumerate(products, start=1) if i not in remove_list ]
    for product in updated_products:
        file.write(f"{product}\n")
    file.close()
    
    return list_products(p)


if __name__ == "__main__":
    main()