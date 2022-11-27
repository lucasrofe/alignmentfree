alphabet = {"A":0, "C" : 1, "T":2,"G":3}
complementaire = {"A" : "T", "T" : "A", "G" : "C", "C": "G"}

def kmer2str(val, k):
    """ Transform a kmer integer into a its string representation
    :param int val: An integer representation of a kmer
    :param int k: The number of nucleotides involved into the kmer.
    :return str: The kmer string formatted
    """
    letters = ['A', 'C', 'T', 'G']
    str_val = []
    for i in range(k):
        str_val.append(letters[val & 0b11])
        val >>= 2

    str_val.reverse()
    return "".join(str_val)


def stream_kmers(text, k):
    # --- To complete ---
    list_kmer = []
    kmer = 0
    reverse_kmer = 0
    alph = ['A', 'C', 'G', 'T']


    for i in range(k-1):
        kmer = kmer << 2  # décale à gauche de 2 bits
        kmer += alphabet[]



