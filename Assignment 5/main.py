# from flight import Flight
# from planner2 import Planner

# def main():
#     flights = [Flight(0, 0, 0, 1, 30, 50),      # City 0 to 1
#                Flight(1, 0, 0, 3, 80, 200),     # City 0 to 3
               
#                Flight(2, 1, 40, 2, 60, 20),     # City 1 to 2
#                Flight(3, 1, 50, 2, 100, 120),   # City 1 to 2
               
#                Flight(4, 2, 120, 4, 200, 100),  # City 2 to 4
               
#                Flight(5, 3, 100, 4, 150, 500),  # City 3 to 4
#                Flight(6, 3, 100, 4, 250, 300)   # City 3 to 4
#                ]
    
#     flight_planner = Planner(flights)
    
#     # The three tasks
#     route1 = flight_planner.least_flights_ealiest_route(0, 4, 0, 300)
#     route2 = flight_planner.cheapest_route(0, 4, 0, 300)
#     route3 = flight_planner.least_flights_cheapest_route(0, 4, 0, 300)
    
#     # model output
#     expected_route1 = [flights[1], flights[5]]                  # 0-3-4, 2 flights, arrives at t=150
#     expected_route2 = [flights[0], flights[3], flights[4]]      # 0-1-2-4, 270 fare
#     expected_route3 = [flights[1], flights[6]]                  # 0-3-4, 2 flights, 500 fare
    
#     # Note that for this given example there is a unique solution, but it may
#     # not be true in general
#     if route1 == expected_route1:
#         print("Task 1 PASSED")
        
#     if route2 == expected_route2:
#         print("Task 2 PASSED")
#     else :
#         print("Task 2 FAILED")    
#     if route3 == expected_route3:
#         print("Task 3 PASSED")
        

# if __name__ == "__main__":
#     main()




import sys
import time
from flight import Flight
from planner2 import Planner

def main():
    flights = [
        # City 0 connections
        Flight(0, 0, 0, 1, 30, 100),  # City 0 to 1
        Flight(1, 0, 0, 2, 40, 200),  # City 0 to 2
        Flight(2, 0, 0, 3, 50, 150),  # City 0 to 3
        
        # City 1 connections with 20 min layover constraints
        Flight(3, 1, 55, 4, 90, 80),  # City 1 to 4 (20 mins after arrival)
        Flight(4, 1, 80, 2, 100, 90),  # City 1 to 2 (second flight to City 2)
        Flight(5, 1, 90, 5, 140, 200),  # City 1 to 5
        
        # City 2 connections (cycle back to 1)
        Flight(6, 2, 120, 3, 160, 140),  # City 2 to 3
        Flight(7, 2, 140, 1, 170, 50),  # City 2 to 1 (cycle, after 20 mins)
        Flight(8, 2, 170, 4, 230, 150),  # City 2 to 4
        
        # City 3 connections (cycle back to 0)
        Flight(9, 3, 180, 0, 220, 90),  # City 3 to 0 (cycle)
        Flight(10, 3, 200, 4, 250, 250),  # City 3 to 4
        Flight(11, 3, 170, 5, 230, 300),  # City 3 to 5
        
        # City 4 connections (cycle back to 2)
        Flight(12, 4, 240, 2, 280, 70),  # City 4 to 2 (cycle)
        Flight(13, 4, 260, 5, 300, 90),  # City 4 to 5
        Flight(14, 4, 300, 6, 340, 100),  # City 4 to 6
        
        # City 5 connections (cycle back to 3)
        Flight(15, 5, 310, 3, 360, 120),  # City 5 to 3 (cycle)
        Flight(16, 5, 340, 6, 390, 110),  # City 5 to 6
        Flight(17, 5, 370, 7, 420, 60),  # City 5 to 7
        
        # City 6 connections (cycle back to 4)
        Flight(18, 6, 390, 4, 440, 130),  # City 6 to 4 (cycle)
        Flight(19, 6, 430, 7, 470, 80),  # City 6 to 7
        
        # City 7 connections (multiple flights to City 8)
        Flight(20, 7, 450, 8, 500, 50),  # City 7 to 8
        Flight(21, 7, 470, 8, 530, 60),  # City 7 to 8 (second flight)
        Flight(22, 7, 500, 9, 550, 100),  # City 7 to 9
        
        # City 8 connections
        Flight(23, 8, 510, 10, 560, 70),  # City 8 to 10
        Flight(24, 8, 530, 11, 580, 80),  # City 8 to 11
        
        # City 9 connections (cycle back to 7 and multiple flights to City 10)
        Flight(25, 9, 560, 7, 610, 110),  # City 9 to 7 (cycle)
        Flight(26, 9, 580, 10, 630, 90),  # City 9 to 10
        Flight(27, 9, 590, 10, 640, 85),  # City 9 to 10 (second flight)
        
        # City 10 connections
        Flight(28, 10, 600, 11, 650, 60),  # City 10 to 11
        Flight(29, 10, 620, 12, 670, 70),  # City 10 to 12
        
        # City 11 connections
        Flight(30, 11, 640, 13, 690, 120),  # City 11 to 13
        Flight(31, 11, 650, 12, 700, 90),  # City 11 to 12
        
        # City 12 connections
        Flight(32, 12, 660, 13, 710, 95),  # City 12 to 13
        Flight(33, 12, 670, 14, 730, 60),  # City 12 to 14
        
        # City 13 connections
        Flight(34, 13, 700, 14, 750, 70),  # City 13 to 14
        Flight(35, 13, 710, 15, 760, 130),  # City 13 to 15
        
        # City 14 connections
        Flight(36, 14, 730, 15, 780, 120),  # City 14 to 15
        Flight(37, 14, 740, 16, 790, 90),  # City 14 to 16
        
        # City 15 connections
        Flight(38, 15, 780, 17, 830, 100),  # City 15 to 17
        Flight(39, 15, 800, 16, 850, 80),  # City 15 to 16 (second flight to 16)
        
        # City 16 connections
        Flight(40, 16, 820, 17, 870, 60),  # City 16 to 17
        Flight(41, 16, 830, 18, 890, 70),  # City 16 to 18
        
        # City 17 connections
        Flight(42, 17, 850, 18, 910, 50),  # City 17 to 18
        Flight(43, 17, 860, 19, 920, 100),  # City 17 to 19
        
        # City 18 connections
        Flight(44, 18, 880, 19, 940, 80),  # City 18 to 19
        Flight(45, 18, 890, 20, 950, 90),  # City 18 to 20
        
        # City 19 connections
        Flight(46, 19, 910, 20, 970, 60),  # City 19 to 20
        Flight(47, 19, 920, 0, 980, 150),  # City 19 to 0 (cycle back to 0)
        
        # Extra connections to increase complexity
        Flight(48, 5, 400, 7, 450, 200),  # City 5 to 7 (third path)
        Flight(49, 7, 450, 10, 510, 150),  # City 7 to 10 (alternate path to City 10)
        Flight(50, 3, 150, 6, 210, 400)    # City 3 to 6 (alternate route)
    ]

    flight_planner = Planner(flights)
    max_city = 20  # Define the maximum city index based on your dataset

    # Generate test cases for every pair of start and end cities
    test_cases = []
    for start in range(max_city + 1):
        for end in range(max_city + 1):
            if start != end:  # Avoid trivial cases where start == end
                test_cases.append({"start": start, "end": end, "start_time": 0, "time_limit": 1000})

    # Redirect the output to the file
    with open("received_output.txt", "w") as f:
        sys.stdout = f  # Redirect stdout to the file
        
        # Run each test case and print the routes
        for idx, test in enumerate(test_cases, 1):
            route1 = flight_planner.least_flights_earliest_route(test["start"], test["end"], test["start_time"], test["time_limit"])
            route2 = flight_planner.cheapest_route(test["start"], test["end"], test["start_time"], test["time_limit"])
            route3 = flight_planner.least_flights_cheapest_route(test["start"], test["end"], test["start_time"], test["time_limit"])

            # Print only if at least one route is found
            if route1 or route2 or route3:
                print(f"\n--- Test Case {idx}: Start {test['start']} -> End {test['end']} ---")
                if route1:
                    print("Task 1 (Least Flights, Earliest):", [f.flight_no for f in route1], f"value: {len(route1)}, {route1[-1].arrival_time}") 
                if route2:
                    print("Task 2 (Cheapest Route):", [f.flight_no for f in route2], "cumulative cost: ", sum(f.fare for f in route2))
                if route3:
                    print("Task 3 (Least Flights, Cheapest):", [f.flight_no for f in route3], f"value: {len(route3)}, {sum(f.fare for f in route3)}")

        # Reset stdout to its original value after writing to the file
        sys.stdout = sys.__stdout__

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter() 

    print(t2 - t1)
