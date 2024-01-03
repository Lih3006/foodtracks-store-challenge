from rules import add_perm

add_perm("branches.view_item", True)
add_perm("branches.change__item", rule="is_superuser or item.user == user")