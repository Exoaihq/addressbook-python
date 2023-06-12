def sort_alphabetical(lst):
    if not lst:
        return []
    return sorted(lst, key=lambda x: x['name']['last'])

def get_local_storage_list_and_sort():
    from json import loads
    contact_list = localStorage.getItem("list")
    if not contact_list:
        return None
    parsed = loads(contact_list)
    sorted_list = sort_alphabetical(parsed)
    return sorted_list