from django import template
from menu.models import Menu

register = template.Library()


@register.filter
def hash(h, key):
    return h.get(key)


@register.inclusion_tag('templatetags/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    """Draw menu by menu_name."""
    menu_items = Menu.objects.select_related(
        'parent', 'group'
    ).filter(group__name=menu_name)
    child_items = {}
    parent_items = {}
    start_items = []
    menu_slug = context.get('menu_slug')

    for item in menu_items:
        parent_items[item] = item.parent
        if menu_slug and item.slug == menu_slug:
            current_menu = item
        if item.parent is not None:
            if not child_items.get(item.parent):
                child_items[item.parent] = [item]
            else:
                child_items[item.parent].append(item)
        else:
            start_items.append(item)

    activated_items = []
    if menu_slug:
        parent = parent_items.get(current_menu)
        activated_items.append(current_menu)
        while parent:
            activated_items.append(parent)
            parent = parent_items[parent]

    return {
        "start_items": start_items,
        'child_items': child_items,
        'activated_items': activated_items
    }
