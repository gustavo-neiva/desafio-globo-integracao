
class TextParser:
    def __blocks(self, files, size=65536):
        while True:
            b = files.read(size)
            if not b: break
            yield b

    def count_lines(self, file_path):
        with open(file_path, "r", encoding="utf-8", errors='ignore') as f:
            n_lines = sum(bl.count("\n") for bl in self.__blocks(f))
            return n_lines