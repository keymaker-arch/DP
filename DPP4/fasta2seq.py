file_in = 'C:\\Users\\dell\\Desktop\\random_peptide.fasta'
file_out = 'C:\\Users\\dell\\Desktop\\random_peptide_seq.txt'

f_in = open(file_in, 'r')
f_out = open(file_out, 'w')

raw_list = []
for line in f_in:
    if '>' in line:
        pass
    else:
        raw_list.append(line)

print(len(raw_list))

clean_list = list(set(raw_list))
print(len(clean_list))

for record in clean_list:
    f_out.write(record)

f_out.close()
f_in.close()