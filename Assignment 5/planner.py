from flight import Flight
from queues import Queue
from heaps import Heap
class Planner:
    def __init__(self, flights):
        """The Planner

        Args:
            flights (List[Flight]): A list of information of all the flights (objects of class Flight)
        """
        cities=[]
        for flight in flights:
            if flight.start_city not in cities:
                cities.append(flight.start_city)
            if flight.end_city not in cities:
                cities.append(flight.end_city)               
        self.city_outgoing_list=[]
        for _ in range(len(cities)*2):#change *2
            self.city_outgoing_list.append([])        
        self.city_incoming_list=[]
        for _ in range(len(cities)*2):
            self.city_incoming_list.append([])  
        self.flight_adj_list=[]
        for _ in range(len(flights)*2):
            self.flight_adj_list.append([])
        self.flight_list=flights
        for flight in flights:
            self.city_outgoing_list[flight.start_city].append((flight,flight.flight_no))
        for flight in flights:
            self.city_incoming_list[flight.end_city].append((flight,flight.flight_no))
        for flight in flights:
            for out_going_flights in self.city_outgoing_list[flight.end_city]:
                if out_going_flights[0].departure_time>=flight.arrival_time+20:
                    self.flight_adj_list[flight.flight_no].append((out_going_flights[0],out_going_flights[0].flight_no))
        # print(self.city_outgoing_list)      
        # print(self.flight_adj_list)      
        
    
    def least_flights_earliest_route(self, start_city, end_city, t1, t2):
        if start_city==end_city:
            return []
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        arrives the earliest
        """
        min_path=[None]*(len(self.flight_list)+1)
        for flights in self.city_outgoing_list[start_city]:
            if flights[0].departure_time>=t1 and flights[0].arrival_time<=t2:
                path = self.bfs(flights,end_city,t2)
                # if len(path)<= len(min_path):
                if len(path)==0:
                    continue
                last_flight=path[-1]
                if len(path)==len(min_path) and last_flight.arrival_time<min_path[-1].arrival_time:
                    min_path=path
                elif len(path)<len(min_path):
                    min_path=path  
        if min_path[-1] is None:
            return []  
        return min_path
        pass
     
    def bfs(self,flight,end_city,t2):
        visited = []      # To keep track of visited nodes
        queue = Queue() # Queue to store nodes to be explored
        queue.enqueue(flight) # Add the start node to the queue
        visited.append(flight)
        parent_list=[None]*len(self.flight_list)*2
        last_flight=None
        path=[]
        if flight[0].end_city==end_city:
            return [flight[0]]
        min_time= float('inf')
        while not queue.is_empty():
            node = queue.dequeue()
            # print(node, end=" ")  # Process the current node
            # if node==last_flight:
            #     break
            # Explore all adjacent nodes
            for flight in self.flight_adj_list[node[0].flight_no]:
                if flight not in visited and flight[0].arrival_time<=t2:
                    queue.enqueue(flight)
                    visited.append(flight)
                    parent_list[flight[0].flight_no]=node[0]
                    if flight[0].arrival_time<=t2 and flight[0].end_city==end_city and flight[0].arrival_time<min_time:
                        last_flight=flight[0]
                        min_time = flight[0].arrival_time
            if last_flight!=None:
                break     
        if last_flight is None:
            return path       
        current = last_flight
        while current is not None:
            path.append(current)
            current = parent_list[current.flight_no]

        # If we couldn't reach the target from the start, return an empty path
        # if path[-1] != flight:
        #     return []

        return path[::-1]
    
    def cheapest_route(self, start_city, end_city, t1, t2):
        if start_city==end_city:
            return []
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route is a cheapest route
        """
        min_price_path=[None]*(len(self.flight_list)+1)
        min_price=float('inf')
        for flights in self.city_outgoing_list[start_city]:

            for flight in self.flight_list:
                flight.set_cost_of_reach()
                
            if flights[0].departure_time>=t1 and flights[0].arrival_time<=t2:
                path,price = self.dijaktra(flights,end_city,t2)
                # if len(path)<= len(min_price_path):
                # last_flight=path[-1]
                if len(path)==0:
                    continue
                if price<min_price:
                    min_price=price
                    min_price_path=path
        if min_price_path[-1] is None:
            return []
        return min_price_path        
        pass
    def comparator_function(self,a,b):
        if a[0]<b[0]:
            return 1
        elif a[0]>b[0]:
            return -1
        else:
            return 0
        
    def dijaktra(self,flight,end_city,t2):
        # flight.cost_of_reach=flight.fare
        # heap = Heap(self.comparator_function,[(flight.fare,flight)])
        # while len(heap):
        #     node = heap.extract()
        #     if node.cost_of_reach > 
       
    # Initialize distances from start to each node as infinity, except the start node itself
        # distances = {node: float('inf') for node in graph}
        # distances[start] = 0
        flight[0].cost_of_reach=flight[0].fare
        visited = [False] * len(self.flight_list)*2
        # visited[flight[0].flight_no]=True
        heap = Heap(self.comparator_function,[(flight[0].fare,flight[0])])
        # Priority queue to explore the closest node with the minimum distance
        # priority_queue = [(0, start)]  # (distance, node)
        parent_list=[None]*len(self.flight_list)*2
        while len(heap)>0:
            current_price, current_node = heap.extract()
            
            if visited[current_node.flight_no]:
                continue
            visited[current_node.flight_no]=True
            # If the popped node has a distance greater than the recorded shortest distance, skip it
            if current_price > current_node.cost_of_reach:
                continue

            # Explore each neighbor of the current node
            for neighbor in self.flight_adj_list[current_node.flight_no]:
                price = current_price + neighbor[0].fare

                # Only consider this new path if it’s better
                if price < neighbor[0].cost_of_reach:
                    neighbor[0].cost_of_reach = price
                    heap.insert((price, neighbor[0]))
                    visited[neighbor[0].flight_no]=False
                    parent_list[neighbor[0].flight_no]=current_node
        min_price = float('inf')   
        last_flight=None
        total_price=0
        path=[] 
        for flights in self.city_incoming_list[end_city]:
            if flights[0].arrival_time<=t2 and flights[0].cost_of_reach<min_price:
                min_price=flights[0].cost_of_reach
                last_flight=flights[0]
        if last_flight is None:
            return path,0       
        current = last_flight
        while current is not None:
            path.append(current)
            total_price+=current.fare
            current = parent_list[current.flight_no]

        # If we couldn't reach the target from the start, return an empty path
        # if path[-1] != flight:
        #     return []

        return path[::-1],total_price
                
    # def bfs2(self,flight,end_city,t2):
    #     visited = []      # To keep track of visited nodes
    #     queue = Queue() # Queue to store nodes to be explored
    #     queue.enqueue(flight) # Add the start node to the queue
    #     visited.append(flight)
    #     parent_list=[None]*len(self.flight_list)
    #     last_flight=None
    #     path=[]
    #     # min_time= float('inf')
    #     min_price = float('inf')
    #     while not queue.is_empty():
    #         node = queue.dequeue()
    #         # print(node, end=" ")  # Process the current node
    #         # if node==last_flight:
    #         #     break
    #         # Explore all adjacent nodes
    #         for flight in self.flight_adj_list[node[0].flight_no]:
    #             if flight not in visited:
    #                 queue.enqueue(flight)
    #                 visited.append(flight)
    #                 parent_list[flight[0].flight_no]=node[0]
    #                 if flight[0].arrival_time<=t2 and flight[0].end_city==end_city and flight[0].arrival_time<min_time:
    #                     last_flight=flight[0]
    #                     min_time = flight[0].arrival_time
    #         if last_flight!=None:
    #             break     
    #     if last_flight is None:
    #         return path       
    #     current = last_flight
    #     while current is not None:
    #         path.append(current)
    #         current = parent_list[current.flight_no]

    #     # If we couldn't reach the target from the start, return an empty path
    #     # if path[-1] != flight:
    #     #     return []

    #     return path[::-1]
    
    def least_flights_cheapest_route(self, start_city, end_city, t1, t2):
        if start_city==end_city:
            return []
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        is the cheapest
        """
        # min_path=[None]*(len(self.flight_list)+1)
        # min_price=float('inf')
        # for flights in self.city_outgoing_list[start_city]:
        #     if flights[0].departure_time>=t1 and flights[0].arrival_time<=t2:
        #         path,price = self.bfs3(flights,end_city,t2)
        #         # if len(path)<= len(min_path):
        #         # last_flight=path[-1]
        #         if len(path)==0:
        #             continue
        #         if len(path)==len(min_path) and price<min_price:
        #             min_path=path
        #             min_price=price
        #         elif len(path)<len(min_path):
        #             min_path=path  
        #             min_price=price  
        # if min_path[-1] is None:
        #     return []
        # return min_path
        
        min_path=[None]*(len(self.flight_list)+1)
        min_price=float('inf')
        for flights in self.city_outgoing_list[start_city]:
            if flights[0].departure_time>=t1 and flights[0].arrival_time<=t2:
                for a in self.flight_list:
                    a.set_cost_of_reach2()
                path,price = self.bfs3(flights,end_city,t2)
                # if len(path)<= len(min_path):
                # last_flight=path[-1]
                if len(path)==0:
                    continue
                if len(path)==len(min_path) and price<min_price:
                    min_path=path
                    min_price=price
                elif len(path)<len(min_path):
                    min_path=path  
                    min_price=price  
        if min_path[-1] is None:
            return []
        return min_path
        pass
    
    # def bfs3(self,flight,end_city,t2):
    #     visited = []      # To keep track of visited nodes
    #     queue = Queue() # Queue to store nodes to be explored
    #     queue.enqueue(flight) # Add the start node to the queue
    #     visited.append(flight)
    #     parent_list=[None]*len(self.flight_list)
    #     last_flight=None
    #     path=[]
    #     if flight[0].end_city==end_city:
    #         return [flight[0]],flight[0].fare
    #     price=0
    #     min_fare= float('inf')
    #     while not queue.is_empty():
    #         node = queue.dequeue()
    #         # print(node, end=" ")  # Process the current node
    #         # if node==last_flight:
    #         #     break
    #         # Explore all adjacent nodes
    #         for flight in self.flight_adj_list[node[0].flight_no]:
    #             if flight not in visited and flight[0].arrival_time<=t2:
    #                 queue.enqueue(flight)
    #                 visited.append(flight)
    #                 if parent_list[flight[0].flight_no] is not None:
    #                     if parent_list[flight[0].flight_no].fare>node[0].fare:
    #                         parent_list[flight[0].flight_no]=node[0]
    #                 else:
    #                     parent_list[flight[0].flight_no]=node[0]
    #                 if flight[0].arrival_time<=t2 and flight[0].end_city==end_city and flight[0].fare<min_fare:
    #                     last_flight=flight[0]
    #                     min_fare = flight[0].fare
    #         if last_flight!=None:
    #             break     
    #     if last_flight is None:
    #         return path,0       
    #     current = last_flight
    #     while current is not None:
    #         path.append(current)
    #         current = parent_list[current.flight_no]
    #     for flight in path:
    #         price+=flight.fare
    #     # If we couldn't reach the target from the start, return an empty path
    #     # if path[-1] != flight:
    #     #     return []

    #     return path[::-1],price
    
     
    def bfs3(self,flight,end_city,t2):
        visited = []      # To keep track of visited nodes
        queue = Queue() # Queue to store nodes to be explored
        queue.enqueue(flight) # Add the start node to the queue
        flight[0].cost_of_reach2=flight[0].fare
        visited.append(flight)
        parent_list=[None]*len(self.flight_list)
        last_flight=None
        path=[]
        if flight[0].end_city==end_city:
            return [flight[0]],flight[0].fare
        price=0
        min_fare= float('inf')
        while not queue.is_empty():
            node = queue.dequeue()
            # print(node, end=" ")  # Process the current node
            # if node==last_flight:
            #     break
            # Explore all adjacent nodes
            for flight in self.flight_adj_list[node[0].flight_no]:
                if flight not in visited and flight[0].arrival_time<=t2:
                    queue.enqueue(flight)
                    visited.append(flight)
                    flight[0].cost_of_reach2=node[0].cost_of_reach2+flight[0].fare
                    if parent_list[flight[0].flight_no] is not None:
                        if parent_list[flight[0].flight_no].cost_of_reach2>node[0].cost_of_reach2:
                            parent_list[flight[0].flight_no]=node[0]
                            flight[0].cost_of_reach2=node[0].cost_of_reach2+flight[0].fare
                    else:
                        parent_list[flight[0].flight_no]=node[0]
                        flight[0].cost_of_reach2=node[0].cost_of_reach2+flight[0].fare
                    if flight[0].arrival_time<=t2 and flight[0].end_city==end_city and flight[0].cost_of_reach2<min_fare:
                        last_flight=flight[0]
                        min_fare = flight[0].cost_of_reach2
            if last_flight!=None:
                break     
        if last_flight is None:
            return path,0       
        current = last_flight
        while current is not None:
            path.append(current)
            current = parent_list[current.flight_no]
        for flight in path:
            price+=flight.fare
        # If we couldn't reach the target from the start, return an empty path
        # if path[-1] != flight:
        #     return []

        return path[::-1],price
    
    
    
    
    
# flights = [Flight(0, 0, 0, 1, 30, 50),      # City 0 to 1
#                Flight(1, 0, 0, 3, 80, 200),     # City 0 to 3
               
#                Flight(2, 1, 40, 2, 60, 20),     # City 1 to 2
#                Flight(3, 1, 50, 2, 100, 120),   # City 1 to 2
               
#                Flight(4, 2, 120, 4, 200, 100),  # City 2 to 4
               
#                Flight(5, 3, 100, 4, 150, 500),  # City 3 to 4
#                Flight(6, 3, 100, 4, 250, 300)   # City 3 to 4
#                ]
    
# flight_planner = Planner(flights)
# flights = [Flight(0,0,10,1,10,10),
#            Flight(1,1,30,2,30,90),
#            Flight(2,0,10,3,10,50),
#            Flight(3,3,30,2,30,60),
#            Flight(4,2,50,4,50,60)
#            ]
# flight_planner = Planner(flights)
# route = flight_planner.least_flights_cheapest_route(0,4,0,700)
# for i in route :
#     print(i.flight_no)