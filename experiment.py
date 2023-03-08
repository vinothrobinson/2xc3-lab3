import lab6 as r
import bst as b
import random
# -------------- Experiment Helper Functions ------------
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]
#----------------------- Experiment 1 -------------------
def experiment1(list_size, max_value):
    TRIAL_NUM = 1
    height_list1 = []
    height_list2 = []
    for _ in range(TRIAL_NUM):
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

experiment1(10000,10000)
