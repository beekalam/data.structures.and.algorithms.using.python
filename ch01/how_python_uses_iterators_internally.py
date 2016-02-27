from linearbag import Bag

if __name__ == "__main__":
    myBag = Bag()
    myBag.add("item1")
    myBag.add("item2")
    myBag.add("item3")
    # create a BagIterator object for myBag
    iterator = myBag.__iter__()

    # Repeat the while loop until break is called
    while True:
        try:
            # Get the next item from the bag. If there are no
            # more items , the StopIteration exception is raised
            item = iterator.__next__()
            # perform the body of the for loop
            print(item)
        # catch the exception and break from the loop when we are done.
        except StopIteration:
            break


