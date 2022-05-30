ts = [-4, -9, 1]

def compute_closet_to_zero():
    positive = []
    negative = []
    if len(ts) == 0:
        return 0
    else:
        for t in ts:
            if all(t > 0 for t in ts):
                return min(t for t in ts)
            elif all(t > 0 for t in ts):
                return max(t for t in ts)
            else:
                for t in ts:
                    if t >= 0:
                        positive.append(t)
                    else:
                        negative.append(t)
                if min(positive) + max(negative) < 0:
                    return min(positive)
                elif min(positive) + max(negative) == 0:
                    return min(positive)
                else:
                    return max(negative)

print(compute_closet_to_zero())