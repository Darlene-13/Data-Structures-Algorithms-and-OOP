"""
This is a file for the linear search algorithm.
This is one of the most common and easy algorithms to use.
Basically this involves performing a query through a list element by element until the desired element is found or the list is exhausted.
"""

def locate_card (cards, query):
    # Initialize an empty list to store the indices for the matching card
    position = 0
    # Set a loop for repetition, set the while loop to be such that the position should always be less than the length of the cards
    while position < len(cards):
        # Check if the current position is within the bounds of the list
        for i in range(len(cards)):
            print('Checking position:', position)
            if cards[position] == query:
                return position
            # If the current position is out of bounds, break the loop
            if position >= len(cards):
                break
            # Increment the position
            position += 1
            # Check if we have reached the end of the query, return number not found
            if position == len(cards):
                return -1
            print('Card not found at position:', position)

# Create test cases
tests = []

# cards does not contain query 
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})