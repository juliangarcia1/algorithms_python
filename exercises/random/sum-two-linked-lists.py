def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    a=l1; b=l2
    carrie=0
    res = ListNode(0)
    res_org=res
    while 1:# Change this to not be inifinite incase something goes wrong
        curr_sum = a.val + b.val + carrie
        carrie = 1 if curr_sum >= 10 else 0
        curr_sum = curr_sum if curr_sum < 10 else curr_sum - 10
        res.val = curr_sum
        res.next =ListNode(carrie)
        res = res.next
        if a.next==None and b.next==None:
            break
        a=a.next; b=b.next
        
    return res_org

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

l1=ListNode(2)
l1.next=ListNode(4)
l1.next.next=ListNode(3)
l2=ListNode(5)
l2.next=ListNode(6)
l2.next.next=ListNode(4)
input =[(l1,l2), (ListNode(5), ListNode(5))]
for L1, L2 in input:
    res = addTwoNumbers(l1,l2)
    import pdb; pdb.set_trace()

    # print(f'L1:  {L1.val} -> {L1.next.val} -> {L1.next.next.val}')
    # print(f'L2:  {L2.val} -> {L2.next.val} -> {L2.next.next.val}')
    # print(f'Res: {res.val} ->  {res.next.val} -> {res.next.next.val}')