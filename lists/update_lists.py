def list_append(container):
    """
    Appends an item to the end of a list.

    Args:
        container (list): The list to which the item will be appended.
        item: The item to append to the list.

    Returns:
        container (list): The updated list with the appended item.
    """
    container.append("item")
    return container
result1 = list_append([])
result2 = list_append([])
print(result1, result2)
# prints result1 and result2 as ['item'] ['item'] because the function appends "item" to a new list each time it is called, resulting in two separate lists with the same content.