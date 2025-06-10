class FileHandler:
    @staticmethod
    def read_file(file: str) -> str:
        with open(file) as f:
            lyrics = f.read()
        return lyrics