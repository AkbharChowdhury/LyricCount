from io import StringIO

from file_handler import FileHandler


class Song:
    def __init__(self, lyric_path: str):
        self.__lyric_path = lyric_path

    def find_keyword_occurrences(self, words: list[str]) -> str:
        lyrics = FileHandler.read_file(self.__lyric_path).lower()
        occurrences = StringIO()

        for word in words:
            occurrences.write(f'"{word}" appeared {lyrics.count(word.lower())} times\n')
        return occurrences.getvalue()
