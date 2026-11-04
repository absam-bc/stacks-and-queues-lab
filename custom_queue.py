import random


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # Add a customer to the back of the queue.
        self.items.append(item)

    def dequeue(self):
        # Remove and return the first customer.
        if self.is_empty():
            return None

        return self.items.pop(0)

    def peek(self):
        # Return the first customer without removing them.
        if self.is_empty():
            return None

        return self.items[0]

    def is_empty(self):
        # Check whether the queue has no customers.
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Removes everyone up to and including the winner.
        Returns the winning customer's name.
        """

        if self.is_empty():
            return None

        # Randomly select one customer.
        winner = random.choice(self.items)

        # Remove customers until the winner is removed.
        while not self.is_empty():
            customer = self.dequeue()

            if customer == winner:
                break

        return winner
