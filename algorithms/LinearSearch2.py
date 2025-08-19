"""
This is a second way of solving a linear search challenge but with better time complexity.
The cards in this case is organized in decreasing order
"""
def locate_card( cards, query):
    # Initialize the search boundaries
    left = 0
    right = len(cards) - 1
    # Loop while the range is still valid
    while left <= right:
        mid = (left + right) //2 # Always get the middle one,,start from it and evaluate if our target lies to the left or to the right.......this is a sorted list
        print('Checking position:', mid)
        if cards[mid] == query:
            print('Card found at position:', mid)
            return mid
        elif cards[mid] < query:
            left = mid + 1 # Move to the right half
            print('Card not found at position:', mid, 'moving right')
        else:
            right = mid - 1
            print('Card not found at position:', mid, 'moving left')
    print('Card not found, returning -1')
    return -1


tests = [
    ([52, 47, 36, 25, 18, 10], 25),
    ([52, 47, 36, 25, 18, 10], 10),
    ([52, 47, 36, 25, 18, 10], 52),
    ([52, 47, 36, 25, 18, 10], 18),
    ([52, 47, 36, 25, 18, 10], 100)
]

for i, (cards, query) in enumerate(tests):
    print(f'Test {i + 1}:')
    locate_card(cards, query)
    print()