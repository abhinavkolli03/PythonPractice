import functools

user = {'username': 'jose123', 'access_level': 'user'}


def user_has_permission(func):
    @functools.wraps(func)
    def secure_func(*args, **kwargs):
       if user.get('access_level') == 'admin':
         return func(*args, **kwargs)
    return secure_func


@user_has_permission
def my_function(panel):
    return f'Password for {panel} panel is 1234.'

@user_has_permission
def another():
    pass


print(my_function.__name__)
print(my_function('movies'))
print(another())


def get_current_user_role() -> int:
    # return the current user's role, represented by an int
    # for example, 0 - admin, 1 - user, 2 - guest
    # You don't need to change this function, we will replace it with a real function that returns the user's role
    return 0


def access_control(func, access_level: int):
    # You code starts here:
    def outer(func):
        @functools(func)
        def inner(*args, **kwargs):
            if get_current_user_role <= access_level:
                return func(*args, **kwargs)
            else:
                raise PermissionError('You do not have the proper access level.')
        return inner
    return outer

@access_control
def delete_some_file(filename):
    print('{} is deleted!'.format(filename))