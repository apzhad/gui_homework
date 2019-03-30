import random


def test_remove_group(app):
    if app.groups.get_group_list() == 0:
        app.groups.add_new_group("group name")
        app.groups.add_new_group("group name2")
        app.groups.add_new_group("group name3")
    old_list = app.groups.get_group_list()
    group = random.choice(old_list)
    move_to_group = random.choice(old_list)
    while move_to_group == group:
        move_to_group = random.choice(old_list)
    app.groups.remove_group(group, move_to_group)
    new_list = app.groups.get_group_list()
    old_list.remove(group)
    assert sorted(old_list) == sorted(new_list)


def test_cancel_remove_group(app):
    if app.groups.get_group_list() == 0:
        app.groups.add_new_group("group name")
        app.groups.add_new_group("group name2")
        app.groups.add_new_group("group name3")
    old_list = app.groups.get_group_list()
    group = random.choice(old_list)
    app.groups.cancel_delete_group(group)
    new_list = app.groups.get_group_list()
    assert sorted(old_list) == sorted(new_list)
