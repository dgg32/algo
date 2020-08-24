
import heapq
from multiprocessing import Pool
import multiprocessing

def cal_toys(package):

    case, toys = package[0], package[1]
    
    SUM_enjoyment_time = sum([x[0] for x in toys])

    cur_time = SUM_enjoyment_time

    max_time = SUM_enjoyment_time

    remove_count = 0
    remove_count_when_max = 0

    toy_used = []
    #toy_reformat = [(toy[0] + toy[1], toy[0]) for toy in toys]

    for index, add_toy in enumerate(toys):
        cur_time += add_toy[0]
        
        toy_used.append((add_toy[0] + add_toy[1], add_toy[0]))

        keep_running = True

        while keep_running == True and len(toy_used) > 0:
            keep_running = False
            
            big_guy = heapq.nlargest(1, toy_used)[0]

            if big_guy[0] > SUM_enjoyment_time:
                cur_time -= 2 * big_guy[1]
                SUM_enjoyment_time -= big_guy[1]
                remove_count += 1 

                heapq._heapify_max(toy_used) 

                heapq._heappop_max(toy_used)

                keep_running = True

            #print ("before", index, cur_time, max_time, remove_count, remove_count_when_max)
            if cur_time > max_time:
                max_time = cur_time

                remove_count_when_max = remove_count
            #print ("after", index, cur_time, max_time, remove_count, remove_count_when_max, "\n\n")

    if len(toy_used) > 0:
        print("Case #", case, ": ",  len(toys) - len(toy_used), " ", "INDEFINITELY", sep="")
    else:
        #print ("toy_used", toy_used)
        #max_time += sum([x[0] for x in toy_used])
        print("Case #", case, ": ", remove_count_when_max, " ", max_time, sep="")
        #pass
    

n = int(input())

queue = []

for i in range(n):
    total_toys = int(input())
    toys = []
    
    for _ in range(total_toys):
        toys.append([int(s) for s in input().split(" ")])
        
    case = i + 1 


    queue.append((case, toys))

num_of_cpu = multiprocessing.cpu_count()

with Pool(num_of_cpu) as P:

    P.map(cal_toys, queue)