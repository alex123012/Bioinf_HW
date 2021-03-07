with open('5.fasta', 'r') as f:
    proteom = {}
    ls = f.readlines()
    for i in range(len(ls)):
        tmp = ls[i].strip()
        if tmp.startswith('>'):
            j = i + 1
            proteom[tmp] = ''
            while not ls[j].startswith('>') and j < len(ls) - 1:
                proteom[tmp] += ls[j].strip().upper()
                j += 1

with open('4.fna', 'r') as f:
    genome = f.read()

# for i in proteom:
#     print(i)
print(len(proteom))

k = 8
kmers = {i: [proteom[i][j:j + k] for j in range(
    len(proteom[i]) - k + 1)] for i in proteom}
# print(kmers)
# print(len(proteom['>tr|A0A663DJA2|QHI42199']), len(kmers['>tr|A0A663DJA2|QHI42199']))

with open('result', 'w') as f:
    for key in kmers:
        for j in kmers[key]:
            f.write(f"{key} {j[0:4]}\n{j}\n")

# result = {}
# for key in kmers:
#     for i in kmers[key]:
#         if i in genome:
#             print('kkk')
#             result[i] = result.get(i, 0) + 1
# print(result)
