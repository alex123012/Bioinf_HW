k = int(input('Enter k number: '))
# wget https://raw.githubusercontent.com/s-a-nersisyan/HSE_bioinformatics_2021/master/seminar4/homework/SARS-CoV-2.fasta

with open('SARS-CoV-2.fasta') as f:
    f.readline().strip()
    fasta = f.readline().strip()

hash_table = {}

for i in range(len(fasta) - k):
    j = i + k
    hash_table[fasta[i:j]] = hash_table.get(
        fasta[i:j], []) + [(i, j)]

for i in hash_table:

    print(i, end=': ')
    for j in hash_table[i]:
        print(j, end=', ')
    print('\n')
