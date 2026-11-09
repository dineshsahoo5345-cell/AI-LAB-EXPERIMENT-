def object_function(x):
    return -(x**2)+10

def hill_climing(start,step_size,max_iteration):
    current=start
    current_value=object_function(current)

    for i in range(max_iteration):
        left=current-step_size
        right=current+step_size

        left_value=object_function(left)
        right_value=object_function(right)

        #move to better neghibour
        if left_value > current_value:
            current=left
            current_value=left_value
        elif right_value > current_value:
            current=right
            current_value=right_value
        else:
            break
    return current,current_value
#main programm
start=float(input("enter the starting value : "))
step_size=float(input("enter the step size : "))
max_iteration=int(input("enter the max iteration : "))

best_position,best_value=hill_climing(start,step_size,max_iteration)
print("\nbest position=",best_position)
print("maximum value=",best_value)
