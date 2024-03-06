def complete_sequence_a():
    sequence_a = [1, 3, 5, 7]
    next_number = sequence_a[-1] + 2
    return next_number

def complete_sequence_b():
    sequence_b = [2, 4, 8, 16, 32, 64]
    next_number = sequence_b[-1] * 2
    return next_number

def complete_sequence_c():
    sequence_c = [0, 1, 4, 9, 16, 25, 36]
    next_number = sequence_c[-1] + (len(sequence_c) * 2)
    return next_number

def complete_sequence_d():
    sequence_d = [4, 16, 36, 64]
    next_number = sequence_d[-1] + (len(sequence_d) * 4)
    return next_number

def complete_sequence_e():
    sequence_e = [1, 1, 2, 3, 5, 8]
    next_number = sequence_e[-1] + sequence_e[-2]
    return next_number

def complete_sequence_f():
    sequence_f = [2, 10, 12, 16, 17, 18, 19]
    next_number = sequence_f[-1] + 2
    return next_number

print("Sequência a:", complete_sequence_a())
print("Sequência b:", complete_sequence_b())
print("Sequência c:", complete_sequence_c())
print("Sequência d:", complete_sequence_d())
print("Sequência e:", complete_sequence_e())
print("Sequência f:", complete_sequence_f())
