def format_to_readable_name(contact):
    if not contact or not contact.get("name"):
        return "No name listed"

    return f'{contact["name"]["title"]}. {contact["name"]["first"]} {contact["name"]["last"]}'


def format_to_readable_address(contact):
    if not contact or not contact.get("location"):
        return "No address listed"

    return f'{contact["location"]["street"]["number"]} {contact["location"]["street"]["name"]}, {contact["location"]["city"]}, {contact["location"]["postcode"]}'