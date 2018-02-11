from datetime import datetime


def get_array(items, item_class):
    if items is not None:
        return [item_class(item) for item in items]
    return None


def get_item(item, item_class):
    if item is not None:
        return item_class(item)
    return None


def get_datetime(item):
    if item is not None:
        return datetime.strptime(item, '%Y-%m-%dT%X')
    return None


def get_bool(item):
    if item is not None:
        return item # test server
    return None


def set_datetime(item):
    if item is not None:
        return item.strftime('%Y-%m-%dT%X')
    return None
