from collections import defaultdict, Counter

word_mapping: dict[str, set[str]] = defaultdict(set)
word_count = defaultdict(int)
songs: dict[str, str] = {
    'rockabye': 'lyrics/rockabye.txt',
    'ciao-adios': 'lyrics/ciao-adios.txt',

}
rockabye, ciao_adios = songs.values()


def lyric_stats(path: str):
    with open(path) as f:
        data = f.read()
    lyrics_lowered: list[str] = data.lower().split()
    [word_mapping[word[0]].add(word) for word in lyrics_lowered]
    counter = Counter(lyrics_lowered)
    show_word_occurrences(counter)


def show_word_occurrences(word_map: dict[str, int]):
    for word, count in word_map.items():
        print(f'{word}: {count}')


def show_lyrics(word_mappings: dict[str, set[str]]):
    for letter, words in word_mappings.items():
        print(f'{letter}: {' '.join(words)}')


def find_keyword_occurrences(words: list[str], lyric_path: str):
    with open(lyric_path) as f:
        lyric = f.read().lower()
        for word in words:
            print(f'"{word}" appeared {lyric.count(word.lower())} times')


def main():
    find_keyword_occurrences(words=['rockabye', 'love'], lyric_path=rockabye)

    print('----rockabye lyric stats ')
    lyric_stats(rockabye)
    print('----cio adios lyric stats ')
    lyric_stats(ciao_adios)


if __name__ == '__main__':
    main()
