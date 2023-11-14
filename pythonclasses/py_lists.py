products = ["Mangoes", "Bananas", "Apples"]

print(products[0])  # prints the first item
print(products[-1])  # prints the last item

# for i in products:  # prints all items
#     print(i)

products.append("Kiwi")  # adding items to the list
print(products)

products.insert(0, "Passion Fruit")
print(products)

products.sort()
print(products)

products.sort(reverse=True)
print(products)

products.remove("Kiwi")
print(products)

products.pop(0)
print(products)
