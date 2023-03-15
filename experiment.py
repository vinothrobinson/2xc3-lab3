import lab6 as r
import bst as b
import random
import math
from tqdm import tqdm
import matplotlib.pyplot as plot
import xc3tree

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

def graph(times):
    plot.plot(times)
    plot.legend()
    plot.title("Number of Swaps vs Difference in Average Height (BST / RBT)")
    plot.xlabel("Number of Swaps")
    plot.ylabel("Difference in Average Height")
    plot.show()

def multi_graph(times):
    plot.plot(times[0], label = "BST")
    plot.plot(times[1], label = "RBT")
    plot.legend()
    plot.title("Number of Swaps vs Average Height (BST / RBT)")
    plot.xlabel("Number of Swaps")
    plot.ylabel("Average Height")
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
    total_heights_1 = []
    total_heights_2 = []
    bst_heights = []
    rbt_heights = []
    trial_num = 10
    total_swaps = int((list_size*math.log(list_size, 2)/2))
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
        total_heights_1.append(bst_avg_height - rbt_avg_height)
    total_heights_2.append(bst_heights)
    total_heights_2.append(rbt_heights)
    return [total_heights_1, total_heights_2]


def experiment3(max_degree):
    # Create tree with 1 node (since a 0-degree tree already has 1 node)
    X = xc3tree.XC3Tree()
    X.insert()
    heights = []

    while True:
        while not X.is_full():
            X.insert() # Insert until X is full
        heights.append(X.get_height())

        if X.get_degree() < max_degree:
            X.insert()
        else:
            break
    print(X)
    return heights


def experiment4(max_degree):
    # Create tree with 1 node (since a 0-degree tree already has 1 node)
    X = xc3tree.XC3Tree()
    X.insert()
    num_of_nodes = []

    while True:
        while not X.is_full():
            X.insert() # Insert until X is full
        num_of_nodes.append(X.get_size())

        if X.get_degree() < max_degree:
            X.insert()
        else:
            break
    print(X)
    return num_of_nodes


output = experiment3(25)
for i, height in enumerate(output):
    print(f"Degree : {i} | Height : {height}")


#output = experiment4(5)
#for i, size in enumerate(output):
#    print(f"Degree : {i} | Size : {size}")


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

# list = experiment2(100, 100)
# multi_graph(list[1])
# graph(list[0])