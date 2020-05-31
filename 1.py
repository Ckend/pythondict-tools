import fire
 
def order_by_value(*items):
    """
    根据数字大小排序
    """
    sorted_items = sorted(items, key=lambda item: item)
    return sorted_items
 
if __name__ == '__main__':
    fire.Fire(order_by_value)
