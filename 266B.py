'''
Attempt at implementing problem 266B at codeforces (ACCEPTED)

During the break the schoolchildren, boys and girls, formed a queue of n people in the canteen. Initially the children stood in the order they entered the canteen. However, after a while the boys started feeling awkward for standing in front of the girls in the queue and they started letting the girls move forward each second.

Let's describe the process more precisely. Let's say that the positions in the queue are sequentially numbered by integers from 1 to n, at that the person in the position number 1 is served first. Then, if at time x a boy stands on the i-th position and a girl stands on the (i + 1)-th position, then at time x + 1 the i-th position will have a girl and the (i + 1)-th position will have a boy. The time is given in seconds.

You've got the initial position of the children, at the initial moment of time. Determine the way the queue is going to look after t seconds.

Input
The first line contains two integers n and t (1 ≤ n, t ≤ 50), which represent the number of children in the queue and the time after which the queue will transform into the arrangement you need to find.

The next line contains string s, which represents the schoolchildren's initial arrangement. If the i-th position in the queue contains a boy, then the i-th character of string s equals "B", otherwise the i-th character equals "G".

Output
Print string a, which describes the arrangement after t seconds. If the i-th position has a boy after the needed time, then the i-th character a must equal "B", otherwise it must equal "G".


'''


def swap(some_list: list, index_one, index_two) -> list:
    temp = some_list[index_one]
    some_list[index_one] = some_list[index_two]
    some_list[index_two] = temp
    return some_list

def get_input() -> list:
    user_inputs = []
    processed_inputs = []
    for i in range(2):
        user_input = input()
        user_inputs.append(user_input)
    split_nums = user_inputs[0].split(" ")
    #Add the split string to a new list
    for elem in split_nums:
        processed_inputs.append(int(elem))
    processed_inputs.append(user_inputs[1])
    return processed_inputs

def main() -> None:
    user_inputs = get_input()
    length = user_inputs[0]
    time = user_inputs[1]
    queue_str = user_inputs[-1]
    #queue as a list
    queue = [char for char in queue_str]

    for i in range(time):
        swap_indicies = [] #This will store tuples, of the indicies that need to be swapped. It is cleared every run.
        for index in range(length):
            #if the person is a boy AND they aren't at the end of the line AND they are in front of a girl
            if queue[index] == "B" and index < length-1 and queue[index+1] == "G":
                swap_indicies.append((index,index+1)) #Add the two indicies as a tuple to the list.
        for indicies in swap_indicies:
            queue = swap(queue, indicies[0], indicies[1])
    result_queue = ''.join(queue) 

    print(result_queue)

main()