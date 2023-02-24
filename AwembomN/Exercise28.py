#Calculate the sum of first 100 prime numbers and return them in an array

def prime_function():

    import array as crazy
    prime_nums = crazy.array("i", [])
    for Pnumbers in range(100):
        if Pnumbers == 1 or Pnumbers == 2 or Pnumbers == 3:
            prime_nums.append(Pnumbers)
            continue
        else:
            for divisor in range(2, Pnumbers):
                if Pnumbers % divisor == 0:
                    break
                elif(divisor == Pnumbers - 1):
                    prime_nums.append(Pnumbers)
    print(sum(prime_nums))
    return prime_nums

answer = prime_function()
print(answer)
