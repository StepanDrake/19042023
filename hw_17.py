def make_html(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        title = func.__name__

        html = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>{title}</title>
            </head>
            <body>
            RESULT: <b>{result}</b>
            </body>
            </html>
        """
        with open(f'index_{func.__name__}.html', mode='w', encoding='utf-8') as new_file:
            new_file.write(html)

        return result
    return wrapper


@make_html
def some_work() -> str:
    return 'some result'
@make_html
def some_work2(argument) -> str:
    return 'some result2 ' + argument


res1 = some_work()
res2 = some_work2('111111')

print(res1)
print(res2)
