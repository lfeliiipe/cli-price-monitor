import argparse

def main() -> None:
    
    # Needs one of 3 mutually exclusive options 
    parser = argparse.ArgumentParser(description="Monitor product prices")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-a", "--add", action="extend", nargs="+", help="Add one or more products", type=str)
    group.add_argument("-f", "--fetch", action="store_true", help="Fetch prices for listed products")
    group.add_argument("-l", "--list", action="store_true", help="List products")
    args = parser.parse_args()

    if args.add:
        add_products(args.add)  
    elif args.fetch:
        fetch()
    elif args.list:
        list_products()


def add_products(products: list) -> None:
    ...


def fetch():
    ...


def list_products():
    ...


if __name__ == "__main__":
    main()