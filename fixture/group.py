class GroupHelper:

    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return group_list

    def add_new_group(self, name):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(name)
        input.type_keys("\n")
        self.close_group_editor()

    def remove_group(self, group, to_group):
        self.open_group_editor()
        editor_tree = self.group_editor.window(auto_id="uxAddressTreeView")
        editor_root = editor_tree.tree_root()
        editor_tree.GetItem([editor_root.text(), group]).click()
        self.open_delete_choise()
        del_tree = self.delete_choise.window(auto_id="uxTreeView")
        del_tree.GetItem([to_group]).click()
        self.delete_choise.window(auto_id="uxOKAddressButton").click()
        self.delete_choise.wait_not("visible")
        self.group_editor.close

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()

    def open_delete_choise(self):
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        self.delete_choise = self.app.application.window(title="Delete group")
        self.delete_choise.wait("visible")
