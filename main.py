from loading import load_directory
from kmers import stream_kmers, kmer2str
from collections import Counter


def index_file(sequences, k):
    return Counter(list_kmers(sequences, k))


def intersect_index(index, sequences, k):
    index_uniq = index.copy()
    query_uniq = {}
    intersection = {}

    for seq in sequences:
        for kmer, rkmer in stream_kmers(seq, k):
            minmer = min(kmer, rkmer)

            # Query not in index
            if minmer not in index_uniq:
                if minmer not in query_uniq:
                    query_uniq[minmer] = 0
                query_uniq[minmer] += 1
            # Query in index => intersection
            else:
                if minmer not in intersection:
                    intersection[minmer] = 0
                intersection[minmer] += 1
                index_uniq[minmer] -= 1
                if index_uniq[minmer] == 0:
                    del index_uniq[minmer]

    return index_uniq, intersection, query_uniq


def list_kmers(sequences, k):
    kmers = []
    for seq in sequences:
        kmers.extend([min(kmer, rkmer) for kmer, rkmer in stream_kmers(seq, k)])
    return kmers


def similarity(A, inter, B):
    inter_total =  sum(inter.values())
    A_similarity = inter_total / (inter_total + sum(A.values()) + 1)
    B_similarity = inter_total / (inter_total + sum(B.values()) + 1)

    return A_similarity, B_similarity


def jaccard(A, inter, B):
    inter_total =  sum(inter.values())
    total = inter_total + sum(A.values()) + sum(B.values())

    return inter_total / total



if __name__ == "__main__":
    # Load all the files in a dictionary
    files = load_directory("data")

    k = 13

    # indexes = {f:index_file(files[f], k) for f in files}
    lists = {f:sorted(list_kmers(files[f], k)) for f in files}
    
    filenames = list(files.keys())
    for i in range(len(files)):
        for j in range(i+1, len(files)):
            A, inter, B = intersect_index(indexes[filenames[i]], files[filenames[j]], k)
            print(filenames[i], filenames[j], jaccard(A, inter, B), similarity(A, inter, B))
