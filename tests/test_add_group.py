import re


def test_add_group(app, xlsx_groups):
    group = xlsx_groups
    old_list = app.groups.get_group_list()
    app.groups.add_new_group(group)
    new_list = app.groups.get_group_list()
    if len(normalize_name(group)) == 0:
        group = "New group"
    old_list.append(group)
    assert sorted(old_list) == sorted(new_list)


def normalize_name(name):
    if name is not None:
        name = re.sub('\s+', ' ', name)
        name = name.strip()
    else:
        name = ""
    return name
