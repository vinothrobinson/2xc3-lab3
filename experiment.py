import lab6 as r
import bst as b
import random
import math
from tqdm import tqdm
import matplotlib.pyplot as plot
# -------------- Experiment Helper Functions ------------
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

def multi_graph(times):
    plot.plot(times[0], label="BST Heights")
    plot.plot(times[1], label="RBT Heights")
    plot.legend()
    plot.title("BST vs RBT Heights")
    plot.xlabel("Number of Swaps")
    plot.ylabel("Height")
    plot.show()

#----------------------- Experiment 1 -------------------
def experiment1(list_size, max_value):
    TRIAL_NUM = 100
    height_list1 = []
    height_list2 = []
    for _ in tqdm(range(TRIAL_NUM)):
        L = create_random_list(list_size, max_value)
        rb = r.RBTree()
        bst = b.BSTree()
        for i in L:
            rb.insert(i)
            bst.insert(i)
        height_list1.append(rb.get_height())
        height_list2.append(bst.get_height())
    rb_height = 0
    bst_height = 0
    for height in range(TRIAL_NUM):
        rb_height += height_list1[height]
        bst_height += height_list2[height]
    print("Average RBTree height is: " + str(rb_height/TRIAL_NUM))
    print("Average BSTree height is: " + str(bst_height/TRIAL_NUM))
    return

def experiment2(list_size, max_value):
    total_heights = []
    bst_heights = []
    rbt_heights = []
    trial_num = 10
    total_swaps = int((list_size*math.log(list_size)/2)//1)
    for num_of_swaps in tqdm(range(total_swaps)):
        bst_avg_height = 0
        rbt_avg_height = 0
        for _ in range(trial_num):
            list = create_near_sorted_list(list_size, max_value, num_of_swaps)
            bst = b.BSTree()
            rbt = r.RBTree()
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

"""
def experiment_test():
    values = [1, 50, 26, 54, 99, 80, 56, 19, 51, 35, 14, 15, 73, 23, 76, 43]
    rb = r.RBTree()
    bst = b.BSTree()
    for value in values:
        rb.insert(value)
        bst.insert(value)
    rb_height = rb.get_height()
    bst_height = bst.get_height()
    print("RBTree height is: " + str(rb_height))
    print("BSTree height is: " + str(bst_height))
    return

experiment_test()
"""

# experiment1(10000,10000)

multi_graph(experiment2(100, 100))