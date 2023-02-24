def maxNum(array):
    for elt in array:
        max = 0
        if isinstance(elt, list):
            maxIf = elt[0]
            for val in elt:
                if val > max:
                    maxIf = val
                else:
                        maxElse = elt
                        if elt >= maxElse:
                            maxElse = elt
                            if maxIf >= maxElse:
                                return maxIf
                            else:
                                return maxElse
                print(maxNum([2, 6, [200, 4], 8]))
