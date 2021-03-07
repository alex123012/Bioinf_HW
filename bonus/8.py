import pickle
import fastaparser
import time


def kmers_make(k, fasta='4.fna'):
    with open(fasta) as fasta_file:
        parser = fastaparser.Reader(fasta_file, parse_method='quick')
        genome = ''.join([seq.sequence.upper() for seq in parser])

    kmers = {}

    for i in range(len(genome) - k + 1):
        tmp = genome[i:i + k]
        t_s = kmers.get(tmp, set())
        t_s.add(i)
        kmers[tmp] = t_s

    with open('kmers.pickle', 'wb+') as f:
        pickle.dump(kmers, f)


def carting(fasta='4.fna', k=30, trans='transcript.fna', kmers=None):

    if not kmers:
        kmers_make(k, fasta)
        kmers = 'kmers.pickle'

    with open(kmers, 'rb') as f:
        kmers = pickle.load(f)

    with open(trans) as fasta_file:
        parser = fastaparser.Reader(fasta_file, parse_method='quick')
        transcript = [seq.sequence.upper() for seq in parser]

    with open(fasta) as fasta_file:
        parser = fastaparser.Reader(fasta_file, parse_method='quick')
        genome = ''.join([seq.sequence.upper() for seq in parser])

    res = {}
    for tr in transcript:
        tmp = tr[:k]
        dc_tmp = kmers.get(tmp, '')
        if dc_tmp:
            for j in dc_tmp:
                end = j + len(tr)
                if tr == genome[j:end]:
                    t = res.get(tr, (len(tr), set()))
                    t[1].add(j)
                    res[tr] = t
    return res


def main():
    # for i in range(5, 56, 10):
    start = time.time()
    kmers_make(k=30)
    print('time:', time.time() - start)
    print()
    start = time.time()
    result = carting(k=30, kmers='kmers.pickle')
    print(result, 'time:', time.time() - start)
    print()
    start = time.time()
    result = carting(k=30)#, kmers='kmers.pickle')
    print(result, 'time:', time.time() - start)


if __name__ == '__main__':
    main()
