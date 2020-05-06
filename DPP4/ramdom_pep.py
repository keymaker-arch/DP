import random


# extra rate of pro in second position of N terminal
extra_rate_pro = 0.45
# extra rate of hydrophobic, basic and big R aa in first position of N terminal
extra_rate_N1 = 0.45

file_out_order = 'C:\\Users\\dell\\Desktop\\random_pep_order.txt'
file_out_shuffle = 'C:\\Users\\dell\\Desktop\\random_pep_shuffle.txt'
all_aa = ['G', 'A', 'V', 'L', 'I', 'P', 'F', 'Y', 'W', 'S', 'T', 'C', 'M', 'N', 'Q', 'D', 'E', 'R', 'H']
hydrophobic = ['G', 'A', 'V', 'L', 'I', 'P', 'F']
basic = ['K', 'R', 'H']
big_R = ['F', 'W', 'Y', 'K', 'R', 'H']
aa_N1 = [hydrophobic, hydrophobic, basic, big_R]

def generate_inhibitor(aa_len, aa_num):
    aa_list = []

    while len(aa_list) < aa_num:
        aa_str = ''

        if random.random() < extra_rate_N1:
            N1_list = random.choice(aa_N1)
            aa_str = aa_str + random.choice(N1_list)
        else:
            aa_str = aa_str + random.choice(all_aa)

        if random.random() < extra_rate_pro:
            aa_str = aa_str + 'P'
        else:
            aa_str = aa_str + random.choice(all_aa)

        while len(aa_str) < aa_len:
            aa_str = aa_str + random.choice(all_aa)

        if aa_str in aa_list:
            continue
        else:
            aa_list.append(aa_str)

    return aa_list

if __name__ == '__main__':
    f_order = open(file_out_order, 'w')
    f_shuffle = open(file_out_shuffle, 'w')

    aa4 = generate_inhibitor(4, 500)
    aa5 = generate_inhibitor(5, 500)
    aa6 = generate_inhibitor(6, 500)
    aa7 = generate_inhibitor(7, 500)

    aa_4_7 = aa4 + aa5 + aa6 + aa7


    for aa in aa_4_7:
        f_order.write(aa + '\n')

    random.shuffle(aa_4_7)
    for aa in aa_4_7:
        f_shuffle.write(aa + '\n')

    f_order.close()
    f_shuffle.close()