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
    queue = deque()
    queue.append([from_])
    ladders = []
    visited = set()

    # keep words with the same length as "from_"/"to_"
    filtered_lexicon = {word for word in lexicon if len(word) == len(from_)}

    # run bfs
    while queue:
        level_size = len(queue)
        found = False
        for i in range(level_size):
            cur_ladder = queue.popleft()
            cur_word = cur_ladder[-1]
            visited.add(cur_word)

            # Check if we reached the end word
            if cur_word == to_:
                ladders.append(cur_ladder)
                found = True

            for new_word in get_neighbors(cur_word, filtered_lexicon):
                if new_word not in visited:
                    new_ladder = cur_ladder + [new_word]
                    queue.append(new_ladder)
        if found:
            break

    shortest_length = min(ladders, key=lambda x: len(x))
    shortest_ladders = [ladder for ladder in ladders if len(ladder) == shortest_length]
    return shortest_ladders


if __name__ == '__main__':
    lexicon = read_lexicon("english.txt")
    print(generate("atlases", "cabaret", lexicon))
