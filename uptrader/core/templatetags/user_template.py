from django import template
from menu.models import Menu

register = template.Library()


def get_childes(menu_item):
    pass


def add_childes(menu_item, items):
    childes = menu_item.childes
    print(childes)
    # if childes:
    #     for child in childes:
    #         items.append(child)
    #         add_childes(menu_item, items)
    return items


def get_items(menu_items, current_menu):
    items = []
    for menu_item in menu_items:
        if menu_item.first_level:
            items.append(menu_item)
            items = add_childes(menu_item, items)
    return items


@register.inclusion_tag('templatetags/menu.html')
def draw_menu(menu_name, current_menu=None):
    menu_items = Menu.objects.select_related(
        'parent', 'group'
    ).prefetch_related(
        'childes'
    ).filter(group__name=menu_name)
    items = get_items(menu_items, current_menu)
    return {
        "menu_items": items,
    }
