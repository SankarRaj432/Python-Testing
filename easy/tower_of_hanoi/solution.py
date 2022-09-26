

def Hanoi(no_of_disks = 0):
    """ Tower of Hanoi """
    if no_of_disks == None or type(no_of_disks) != int:
        if type(no_of_disks) == float:
            return 0
        try:
            no_of_disks = int(no_of_disks)
        except ValueError:
            return 0

    if no_of_disks < 1:
        return 0

    if no_of_disks == 1:
        return 1
    return 2 * Hanoi(no_of_disks - 1) + 1
