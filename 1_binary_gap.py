def solution(N):
    # a binary to string looks like this: 0b01001100
    bin_str = str(bin(N))[2:] # cut the prefix
    found_one = False # to discard the first zeros before the first one
    highest_count = 0 # the highest group
    counter = 0 # partial count
    for char in bin_str:
        if char == '1':
            if highest_count < counter:
                highest_count = counter
            found_one = True
            counter = 0
        elif found_one:
            counter += 1
    return highest_count