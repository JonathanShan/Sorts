import random
import time

def selection_sort(list_s):
    comparison = 0
    for i in range(len(list_s)-1):
        minimum = list_s[i]
        min_index = i
        j = i + 1
        while j in range(len(list_s)):
            if list_s[j] < minimum:
                minimum = list_s[j]
                min_index = j
            comparison += 1
            j += 1
        temp = list_s[i]
        list_s[i] = minimum
        list_s[min_index] = temp
    return comparison
    
def insertion_sort(list_i):
    comparison = 0
    for static in range(1,len(list_i)):
        moving = static
        if list_i[moving] >= list_i[moving-1] and moving > 0:
            comparison +=1
        while list_i[moving] < list_i[moving-1] and moving > 0:
            temp = list_i[moving]
            list_i[moving] = list_i[moving-1]
            list_i[moving-1] = temp
            moving -= 1
            comparison += 1
    return comparison

   

def main():
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 1000)
    start_time = time.time() 
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()

