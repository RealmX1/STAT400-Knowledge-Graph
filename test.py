import random
import math

def levenshtein_distance(seq1, seq2):
    """
    Compute the Levenshtein (edit) distance between two sequences seq1 and seq2.
    Allowed operations: insert, delete, substitute.
    """
    n, m = len(seq1), len(seq2)
    # dp[i][j] = edit distance between seq1[:i] and seq2[:j]
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = i  # cost of deleting i elements
    for j in range(m+1):
        dp[0][j] = j  # cost of inserting j elements
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = 0 if seq1[i-1] == seq2[j-1] else 1
            dp[i][j] = min(dp[i-1][j] + 1,      # deletion
                           dp[i][j-1] + 1,      # insertion
                           dp[i-1][j-1] + cost) # substitution (cost=0 if same, else 1)
    return dp[n][m]

def random_permutation(n):
    """Return a random permutation of [0, 1, 2, ..., n-1]."""
    arr = list(range(n))
    random.shuffle(arr)
    return arr

def experiment_average_edit_distance(n, num_samples=10_000):
    """
    1. Generate num_samples pairs of permutations of length n.
    2. Compute their edit distances.
    3. Return the average distance.
    """
    total_dist = 0
    for _ in range(num_samples):
        perm1 = random_permutation(n)
        perm2 = random_permutation(n)
        dist = levenshtein_distance(perm1, perm2)
        total_dist += dist
    return total_dist / num_samples

if __name__ == "__main__":
    N = 4         # length of each permutation
    SAMPLES = 5000 # number of pairs to sample
    avg_dist = experiment_average_edit_distance(N, SAMPLES)
    print(f"For N={N} over {SAMPLES} random pairs, average edit distance = {avg_dist:.3f}")
