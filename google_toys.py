
def cal_toys(case, toys):
    
    SUM_enjoyment_time = sum([x[0] for x in toys])

    cur_time = SUM_enjoyment_time

    max_time = SUM_enjoyment_time

    remove_count = 0
    remove_count_when_max = 0

    toy_used = []

    for index, add_toy in enumerate(toys):
        cur_time += add_toy[0]
        
        toy_used.append(add_toy)

        keep_running = True
        something_remove = False

        previous_remove_count = remove_count

        while keep_running == True and len(toy_used) > 0:
            
            max_violate_sum = -1
            max_violate_index = -1

            for index, toy in enumerate(toy_used):
                if toy[0] + toy[1] > SUM_enjoyment_time:
                    if toy[0] + toy[1] > max_violate_sum:
                        max_violate_sum = toy[0] + toy[1]
                        max_violate_index = index
            
            keep_running = False
            #print (toy_used, max_violate_index)

            if max_violate_sum != -1 and max_violate_index != -1:
                cur_time -= 2 * toy_used[max_violate_index][0]
                
                SUM_enjoyment_time -= toy_used[max_violate_index][0]
                remove_count += 1  
                keep_running = True
                something_remove = True
                del toy_used[max_violate_index]

            #print ("before", index, cur_time, max_time, remove_count, remove_count_when_max)
            if cur_time > max_time:
                max_time = cur_time
                remove_count_when_max = remove_count
            #print ("after", index, cur_time, max_time, remove_count, remove_count_when_max, "\n\n")



    #print (toy_time, add_order, remove_count, toy_used, cur_time)

    if len(toy_used) > 0:
        print("Case #", case, ": ",  len(toys) - len(toy_used), " ", "INDEFINITELY", sep="")
    else:
        #print ("toy_used", toy_used)
        #max_time += sum([x[0] for x in toy_used])
        print("Case #", case, ": ", remove_count_when_max, " ", max_time, sep="")
        #pass
    

n = int(input())

for i in range(n):
    total_toys = int(input())
    toys = []
    
    for _ in range(total_toys):
        toys.append([int(s) for s in input().split(" ")])
        
    case = i + 1 


    cal_toys(case, toys)

