#q2
"""class Card:
    def __init__(self, number, color):
        self._number = number
        self._color = color

    def GetNumber(self):
        return int(self._number)
    
    def GetColor(self):
        return self._color
    
class Hand:

    def __init__(self,c1, c2, c3, c4, c5,):
        self._cards = [c1, c2, c3, c4, c5]
        self._firstCard = 0
        self._NumberCards = len(self._cards)


    def GetCard(self, index):
        if index >= 0 and index <= self._NumberCards:
            return self._cards[index]

def calc_value(player_hand: Hand):
    total = 0
    for value in player_hand:
        if value.

if __name__ == '__main__':
    cards = []
    #for every 5 there is a color
    for color in ['red', 'blue', 'yellow']:
        for i in range(1, 5):
            cards.append(Card(i, color))

    # Player 1 cards
    player1_hand = Hand(
        Card(1, "red"),
        Card(2, "red"),
        Card(3, "red"),
        Card(4, "red"),
        Card(1, "yellow")
    )

    # Player 2 cards
    player2_hand = Hand(
        Card(2, "yellow"),
        Card(3, "yellow"),
        Card(4, "yellow"),
        Card(5, "yellow"),
        Card(1, "blue")
    )
"""

#q3
# Initialize the array with -1 for all nodes
ArrayNodes = [[-1, -1, -1] for i in range(20)]

# Store given data in ArrayNodes
ArrayNodes[0] = [-1, 20, 5]
ArrayNodes[1] = [2, 15, -1]
ArrayNodes[2] = [-1, 33, 3]
ArrayNodes[3] = [-1, 94, -1]
ArrayNodes[4] = [1, 10, -1]
ArrayNodes[5] = [1, 58, -1]
ArrayNodes[6] = [-1, -1, -1]

# Initialize pointers
FreeNode = 6
RootPointer = 0

def SearchValue(root: int, ValueToFind: int):
    if root == -1:
        return -1

    if ArrayNodes[root][1] == ValueToFind:
        return root

    # Search left subtree
    left_result = SearchValue(ArrayNodes[root][0], ValueToFind)
    if left_result != -1:
        return left_result

    # Search right subtree
    return SearchValue(ArrayNodes[root][2], ValueToFind)

def PostOrder(root):
    if root == -1:
        return
    if ArrayNodes[root][0] != -1:
        PostOrder(ArrayNodes[root][0])
    if ArrayNodes[root][2] != -1:
        PostOrder(ArrayNodes[root][2])
    print(ArrayNodes[root][1])

if __name__ == '__main__':
    index = SearchValue(RootPointer, 15)
    print(f"Search result index: {index}")
    print("Post-order traversal output:")
    PostOrder(RootPointer)
