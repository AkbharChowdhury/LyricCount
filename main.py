from collections import defaultdict, Counter
from io import StringIO
from file_handler import FileHandler
from song import Song

songs: dict[str, str] = {
    'rockabye': 'lyrics/rockabye.txt',
    'ciao-adios': 'lyrics/ciao-adios.txt',
}
rockabye, ciao_adios = songs.values()


def lyric_stats(path: str):
    data = FileHandler.read_file(path)
    lyrics_lowered: list[str] = data.lower().split()
    word_mapping: dict[str, set[str]] = defaultdict(set)
    [word_mapping[word[0]].add(word) for word in lyrics_lowered]
    counter = Counter(lyrics_lowered)
    show_word_occurrences(counter)


def show_word_occurrences(word_map: dict[str, int]):
    for word, count in word_map.items():
        print(f'{word}: {count}')


def show_lyrics(word_mappings: dict[str, set[str]]):
    for letter, words in word_mappings.items():
        print(f'{letter}: {' '.join(words)}')


def find_keyword_occurrences(words: list[str], lyric_path: str) -> str:
    lyrics = FileHandler.read_file(lyric_path).lower()
    occurrences = StringIO()

    for word in words:
        occurrences.write(f'"{word}" appeared {lyrics.count(word.lower())} times\n')
    return occurrences.getvalue()


def find_keywords(song: Song, keywords: list[str]) -> str:
    keyword_occurrences: str = song.find_keyword_occurrences(keywords)
    return keyword_occurrences


def main():
    rockabye_keywords: list[str] = [
        'rockabye',
        'love',
        "I'm gonna give you all of my love", "I'm gonna rock you"
    ]

    ciao_adios_keywords: list[str] = [
      "I'm not your number one"
    ]
    rockabye_results = find_keywords(Song(rockabye), rockabye_keywords)
    ciao_adios_results = find_keywords(Song(ciao_adios), ciao_adios_keywords)

    print(rockabye_results)
    print(ciao_adios_results)


if __name__ == '__main__':
    main()
