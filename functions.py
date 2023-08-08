def hello_func(greeting, name='you'):
    return f'{greeting} {name}'

print(hello_func('hello','john'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('math','art', name='john', age='25')
student_info('math','art', 'jerry','24')

courses = ['math','science']
info = {'name':'harsha','age':'25'}
student_info(*courses,**info)