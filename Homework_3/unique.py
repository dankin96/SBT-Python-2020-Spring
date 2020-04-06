class Unique:

    def execute(self, c, **kwargs):
        if kwargs['unique']:
            return {key: c[key] for key in c if c[key] == 1}
        return c