#this is a python course by Jovian as I go through the courses I post them here
# Lesson 1 - Binary Search, Linked Lists and Complexity


def test_location(cards, query, mid):
    if cards[mid] == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif cards[mid] < query:
        return 'left'
    else:
        return 'right'

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1


cards = ['2C', '4D', '6H', '8S', '10C', 'QD', 'KH']
query = '8S'

print("Searching for card:", query)
index = locate_card(cards, query)
if index != -1:
    print("Card found at index:", index)
else:
    print("Card not found in list.")
