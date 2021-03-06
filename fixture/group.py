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
        self.open_group_delete(group)
        del_tree = self.group_delete.window(auto_id="uxTreeView")
        del_tree.GetItem([to_group]).click()
        self.group_delete.window(auto_id="uxOKAddressButton").click()
        self.group_delete.wait_not("visible")
        self.group_editor.close

    def cancel_delete_group(self, group):
        self.open_group_editor()
        self.open_group_delete(group)
        self.group_delete.window(auto_id="uxCancelAddressButton").click()
        self.group_delete.wait_not("visible")
        self.group_editor.close

    def remove_group_with_contact(self, group):
        self.open_group_editor()
        self.open_group_delete(group)
        self.group_delete.window(auto_id="uxDeleteAllRadioButton").click()
        self.group_delete.window(auto_id="uxOKAddressButton").click()
        self.group_delete.wait_not("visible")
        self.group_editor.close

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()

    def open_group_delete(self, group):
        editor_tree = self.group_editor.window(auto_id="uxAddressTreeView")
        editor_root = editor_tree.tree_root()
        editor_tree.GetItem([editor_root.text(), group]).click()
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        self.group_delete = self.app.application.window(title="Delete group")
        self.group_delete.wait("visible")
