from collections import deque

#simmulation people in a queue
ticket_queue= deque()
print(ticket_queue)

#people arriving to the queue
ticket_queue.append("chris")
ticket_queue.append("cathy")
ticket_queue.append("saint")
print(ticket_queue)


#people bought the ticket
ticket_queue.popleft()
ticket_queue.popleft()
ticket_queue.popleft()


#no onew is in the line
print(ticket_queue.popleft())