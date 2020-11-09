#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # hash each ticket with source and destination being key and value
    ticket_cache = {}
    route = [None] * length

    for ticket in tickets:
        ticket_cache[ticket.source] = ticket.destination
    next = ticket_cache["NONE"]

    for i in range(0, length):
        route[i] = next
        next = ticket_cache[next]
    return route



# for testing
