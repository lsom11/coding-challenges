

def luckBalance(k, contests):
    total_luck = 0
    contests = sorted(contests, reverse=True)

    for luck, is_important in contests:
        if not is_important:
            total_luck += luck
        else:
            if k > 0:
                k -= 1
                total_luck += luck
            else:
                total_luck -= luck

    return total_luck
