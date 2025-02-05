from bag.py import Bag

def main():
    ## TESTING ONLY
    test = Bag()
    test.add(item1)
    test.add(item1)
    test.add(item2)
    test.add(item3)
    print("Added item1, item1, item2, item3.")
    print(f"Distinct items: {test.distinct_items()}")
    print(f"item1 count: {test.count(item1)}")
    test.remove(item3)
    print("item3 removed.")
    test.clear()
    print(f"Distinct items: {test.distinct_items()}")


if __name__ == '__main__':
    main()
