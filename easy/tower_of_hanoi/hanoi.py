

def Hanoi(no_of_disks):
    """ Tower of Hanoi """
    if no_of_disks == 1:
        return 1
    return 2 * Hanoi(no_of_disks - 1) + 1
