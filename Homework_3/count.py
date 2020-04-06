from collections import Counter

class Count:

    def execute(self, c, **kwargs):
        c = Counter(c)
        if kwargs['count']:
            return "\n".join(["{0} {1}".format(item[1], item[0]) for item in c.most_common()])
        else:
            return "\n".join(c.elements())