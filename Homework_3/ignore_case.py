from collections import Counter


class IgnoreCase:

    def execute(self, clean_lines, **kwargs):
        if kwargs['ignore_case']:
            for i in range(len(clean_lines) - 1):
                line = clean_lines[i]
                lower_lines = [line.lower() for line in clean_lines[i + 1:]]
                if line.lower() in lower_lines:
                    clean_lines[lower_lines.index(line.lower()) + i + 1] = line
        c = Counter(clean_lines)
        return c