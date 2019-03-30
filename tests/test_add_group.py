import string
import random
import pytest


def random_string(max_length):
    symbols = string.ascii_letters + string.digits + ' '*10
    return "".join([random.choice(symbols) for i in range(random.randrange(max_length))])


test_data = [random_string(10) for i in range(5)]


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    old_list = app.groups.get_group_list()
    app.groups.add_new_group(group)
    new_list = app.groups.get_group_list()
    if len(group) == 0:
        group = "New group"
    old_list.append(group)
    assert sorted(old_list) == sorted(new_list)
