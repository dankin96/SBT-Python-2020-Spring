import click
import reader
import ignore_case
import unique
import repeat
import count
import writer

FILE_INPUT_NAME = 'Homework_3/src/input_3.txt'
FILE_OUTPUT_NAME = 'Homework_3/src/output.txt'


@click.command()
@click.option('-c', '--count', help="выводить число повторов в начале каждой строки;", default=False, is_flag=True)
@click.option('-d', '--repeat', help="выводить только повторяющиеся строки;", default=False, is_flag=True)
@click.option('-i', '--ignore-case', help="игнорировать регистр при сравнении;", default=False, is_flag=True)
@click.option('-u', '--unique', help="выводить только неповторяющиеся строки;", default=False, is_flag=True)
def cli(**kwargs):
    print(type(kwargs))
    r = reader.Reader()
    clean_lines = r.read(FILE_INPUT_NAME)
    i = ignore_case.IgnoreCase()
    dict_counter = i.execute(clean_lines, **kwargs)
    d = repeat.Repeat()
    dict_counter = d.execute(dict_counter, **kwargs)
    u = unique.Unique()
    dict_counter = u.execute(dict_counter, **kwargs)
    c = count.Count()
    out = c.execute(dict_counter, **kwargs)
    w = writer.Writer()
    w.write(FILE_OUTPUT_NAME, out)


if __name__ == "__main__":
    cli()
