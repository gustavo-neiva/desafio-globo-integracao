import datetime
import time

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

    def parse_content(self, file_path, start_line = 0):
        with open(file_path, 'r', encoding="utf-8", errors='ignore') as f:
            result_list = []
            # definir a linha onde iniciar o parseamento da string
            for i, line in enumerate(f):
                if i == start_line:
                    break
            for line in f:
                # selecionar pedaços da string a partir do indice
                start_time = line[6:28]
                end_time = line[29:50]
                title = line[106:138].rstrip()
                duration = line[184:195]
                reconcile_key = line[279:298].rstrip()
                dictionary = { 'start_time': start_time, 
                            'end_time': end_time, 
                            'title': title,
                            'duration':duration,
                            'reconcile_key': reconcile_key
                            }
                duration_string = duration.split(';', 1)[0]
                dt = time.strptime(duration_string,'%H:%M:%S')
                duration_seconds = datetime.timedelta(hours=dt.tm_hour,minutes=dt.tm_min,seconds=dt.tm_sec).total_seconds()
                if duration_seconds > 30:
                    result_list.append(dictionary)
            return(result_list)