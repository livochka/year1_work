# Created to get information from World Bank API

import wbdata


def get_available_sources():
    """
    Helps to get all available topics
    return: list of tuples: (id of topic of indicators,
                             description of topic of indicators)
    """
    available_info = wbdata.get_source()
    return [(x['id'], x['name']) for x in available_info]


def get_topic_indicators(topic_id):
    """
    Get information about indicators on this topic
    id: if of the topic
    return: list with indicators (id and name)
    """
    inclusion_indicators = wbdata.get_indicator(source=topic_id)
    return [(x['id'], x['name']) for x in inclusion_indicators]


def get_info_country(id, country, year=False):
    """
    Specific indicator value for specific country in specific year
    id: indicator id
    country: country name
    return: if year was specified - value of indicator for this year and
    country, else - list with tuples (year, value) for all years
    """
    cpi = wbdata.get_data(id, country)
    if year:
        return [x for x in cpi if x['date'] == str(year)][0]['value']
    else:
        return [(x['date'], x['value']) for x in cpi]


if __name__ == "__main__":
    print(get_available_sources())
    print(get_topic_indicators(1))

    # Indicator 'CPTOTSAXN', description: 'The consumer price index
    # reflects the change in prices for the average consumer of a constant
    # basket of consumer goods. Data is in nominal terms and seasonally
    # adjusted.'
    print(get_info_country('CPTOTSAXN', 'USA'))
