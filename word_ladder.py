from collections import deque


def read_lexicon(path: str) -> set[str]:
    with open(path, 'r') as f:
        lexicon = {line.strip() for line in f}
    return lexicon


def get_hops(word1: str, word2: str) -> int:
    """
    assume that len(word1) == len(word2)
    :return: number of different characters between word1 and word2
    """
    return sum(1 for i, j in zip(word1, word2) if i != j)


def get_neighbors(word: str, lexicon: set[str]) -> [str]:
    """
    assume that all words in "lexicon" has the same length as "word"
    """
    return sorted([item for item in lexicon if get_hops(word, item) == 1])


def generate(from_: str, to_: str, lexicon: set[str]) -> [str]:
    queue = deque([(from_, [from_])])
    visited = set()
    list_of_ladders = []

    # keep words with the same length as "from_"/"to_"
    filtered_lexicon = {word for word in lexicon if len(word) == len(from_)}

    # run bfs
    while queue:
        word, path = queue.popleft()
        if word not in visited:
            visited.add(word)
            if word == to_:
                list_of_ladders.append(path)
                continue
            for neighbor in get_neighbors(word, filtered_lexicon):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return list_of_ladders
