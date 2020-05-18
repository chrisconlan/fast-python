from collections import Counter
from joblib import Parallel, delayed
import math

def _counter_fast_count(
    the_words: List[str]) -> Dict[str, int]:
    return Counter(the_words)

N_JOBS = 8

def parallel_fast_count(
    the_words: List[str]) -> Dict[str, int]:
    """
    Count words in parallel using joblib, then aggregate the
    results. This is still O(n+m) complexity for constant k,
    or O(n+km) for variable k.
    """

    # Figure out chunk sizes
    s = chunk_size = math.ceil(len(the_words) / N_JOBS)
    chunk_slices = [(i*s, (i+1)*s) for i in range(N_JOBS)]

    # Set up parallel wrapper and functions
    parallel = Parallel(n_jobs=N_JOBS)
    delayed_count = delayed(_counter_fast_count)
    
    # Dispatch parallel computation
    counters: List[Dict[str, int]] = parallel(
        delayed_count(the_words[i:j]) for \
        i, j in chunk_slices
    )

    # Aggregate result
    result_count: Dict[str, int] = Counter()
    for counter in counters:
        # Counter.update sums counts
        result_count.update(counter)

    return result_count