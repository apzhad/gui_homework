import random


def test_remove_group(app):
    if app.groups.get_group_list() == 0:
        app.groups.add_new_group("group name")
    old_list = app.groups.get_group_list()
    group = random.choice(old_list)
    app.groups.remove_group(group)
    new_list = app.groups.get_group_list()
    old_list.remove(group)
    assert sorted(old_list) == sorted(new_list)
