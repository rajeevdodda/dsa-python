# Fruits into Baskets (medium)


def fruits_into_basket(array):
    basket = dict()
    start = 0
    max_fruits = 0
    for i in range(len(array)):
        last = array[i]

        if last not in basket:
            basket[last] = 0
        basket[last] += 1

        while len(basket) > 2:
            first = array[start]

            basket[first] -= 1
            if basket[first] == 0:
                del basket[first]
            start += 1

        max_fruits = max(max_fruits, i - start + 1)

    print(max_fruits)


a = ['A', 'B', 'C', 'A', 'C']
fruits_into_basket(a)
b = ['A', 'B', 'C', 'B', 'B', 'C']
fruits_into_basket(b)
