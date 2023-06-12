def apply_filters(initial_state, gender_filter, alphabetical_filter):
    filtered_list = list(filter(lambda contact: (
        (contact['gender'] == 'female' and gender_filter['female']) or
        (contact['gender'] == 'male' and gender_filter['male'])
    ) and contact['name']['last'][0].lower() in alphabetical_filter, initial_state))

    return filtered_list