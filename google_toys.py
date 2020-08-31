
import heapq

import time

#start = time.time()

    

n = int(input())


for i in range(n):
    total_toys = int(input())
    toys = []
    
    SUM_enjoyment_time = 0
    for _ in range(total_toys):
        toy = [int(s) for s in input().split(" ")]
        toys.append(toy)
        SUM_enjoyment_time += toy[0]
        
    case = i + 1 

    cur_time = SUM_enjoyment_time

    max_time = SUM_enjoyment_time

    remove_count = 0
    remove_count_when_max = 0

    toy_used = []

    for add_toy in toys:
        
        if (add_toy[0] + add_toy[1]) > SUM_enjoyment_time:
            SUM_enjoyment_time -= add_toy[0]
            remove_count += 1
            cur_time -= add_toy[0]

            #keep_running = True
            
            while len(toy_used) > 0 and -1 * toy_used[0][0] > SUM_enjoyment_time:
                big_guy_enjoyment_time = toy_used[0][1]
                cur_time -= 2 * big_guy_enjoyment_time
                SUM_enjoyment_time -= big_guy_enjoyment_time
                remove_count += 1 

                heapq.heappop(toy_used)
            
        else:


            heapq.heappush(toy_used, (-1 * (add_toy[0] + add_toy[1]), add_toy[0]))
            cur_time += add_toy[0]
                #print ("before", index, cur_time, max_time, remove_count, remove_count_when_max)
            if cur_time > max_time:
                max_time = cur_time

                remove_count_when_max = remove_count
            #print ("after", index, cur_time, max_time, remove_count, remove_count_when_max, "\n\n")

    if len(toy_used) > 0:
        print("Case #", case, ": ",  len(toys) - len(toy_used), " ", "INDEFINITELY", sep="")
    else:
        print("Case #", case, ": ", remove_count_when_max, " ", max_time, sep="")


#end = time.time()
#print(end - start)