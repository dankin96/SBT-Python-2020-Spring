class Repeat:

    def execute(self, c, **kwargs):
        if kwargs['repeat']:
            return {key: c[key] for key in c if c[key] > 1}
        return c