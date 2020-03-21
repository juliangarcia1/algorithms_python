def numberOfSteps(num):
    steps = 0 # We need to keep track of how many steps this takes.
    while num > 0: # Remember, we're taking steps until num is 0.
        if num % 2 == 0: # Modulus operator tells us num is *even*.
            num = num // 2 # So we divide num by 2.
        else: # Otherwise, num must be *odd*.
            num = num - 1 # So we subtract 1 from num.
        steps = steps + 1 # We *always* increment steps by 1.
    return steps # And at the end, the answer is in steps so we return it.
num=43
rule=f'If the current number is even, you have to divide it by 2,'\
     f'otherwise, you have to subtract 1 from it.'
print(f'For {num} to be reduced to zero, '
      f'According to rule: \n{rule} \n'
      f'it is necessary {numberOfSteps(43)} steps'
      )