
def main() -> None:
    repeat = int(input())
    vectors = []
    #Collect inputs as strings
    for i in range(repeat):
        vector = input()
        vectors.append(vector)
    #Separate each input into its own list
    for i in range(len(vectors)):
        vectors[i] = vectors[i].split(" ")
        vectors[i] = [int(x) for x in vectors[i]]
    
    #Line up the list 
    lined_up_list = []
    inner = []
    for i in range(len(vectors[0])):
        if inner:
            lined_up_list.append(inner)
        inner = []
        for j in range(len(vectors)):
            inner.append(vectors[j][i]) #vectors [j][i]
    lined_up_list.append(inner) #Appends one extra time since the loop closes
    
    sums = [sum(x) for x in lined_up_list] #The sums of all the vectors
   
    if sums.count(0) == len(sums):
        print("YES")
    else:
        print("NO")
        
    

main()
