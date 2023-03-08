import random
import math
import matplotlib.pyplot as plot
from tqdm import tqdm
import bst as BST
import lab6 as RBT

def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L

def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

def exp2():
    total_heights = []
    bst_heights = []
    rbt_heights = []
    trial_num = 10
    list_length = 100
    total_swaps = int((list_length*math.log(list_length)/2)//1)
    for num_of_swaps in tqdm(range(total_swaps)):
        bst_avg_height = 0
        rbt_avg_height = 0
        for _ in range(trial_num):
            list = create_near_sorted_list(list_length, list_length, num_of_swaps)
            bst = BST.BSTree()
            rbt = RBT.RBTree()
            for node in list:
                bst.insert(node)
                rbt.insert(node)
            bst_avg_height += bst.get_height()
            rbt_avg_height += rbt.get_height()
        bst_avg_height /= trial_num
        rbt_avg_height /= trial_num
        bst_heights.append(bst_avg_height)
        rbt_heights.append(rbt_avg_height)
    total_heights.append(bst_heights)
    total_heights.append(rbt_heights)
    return total_heights

def multi_graph(times):
    plot.plot(times[0], label="BST Heights")
    plot.plot(times[1], label="RBT Heights")
    plot.legend()
    plot.title("BST vs RBT Heights")
    plot.xlabel("Number of Swaps")
    plot.ylabel("Height")
    plot.show()

list = exp2()
multi_graph(list)