from loading import load_directory
from kmers import stream_kmers, kmer2str



def similarity(A, inter, B):
    # --- To complete ---
        #inter, A, B [int] : nombre de kmer inter
    return inter / (A + inter), inter / (B + inter)


def jaccard(A, inter, B):
    # --- To complete ---
    return inter / (A + inter + B)

def mymethod() : 



if __name__ == "__main__":
    # Load all the files in a dictionary
    files = load_directory("data")
    k = 21
    
    filenames = list(files.keys())
    for i in range(len(files)):
        for j in range(i+1, len(files)):
            
            # --- Complete here ---

            # mymethod : récupère les kmers de A et B, et les kmer intersection entre A et B
            A, inter, B = my_method(indexes[filenames[i]], files[filenames[j]], k)  
            print(filenames[i], filenames[j], jaccard(A, inter, B), similarity(A, inter, B))



