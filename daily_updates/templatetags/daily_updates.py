from django import template

register = template.Library()


def humanize_hours(min):
    hours = min // 60
    minutes = min % 60

    return "{} hours {} minutes".format(hours, minutes)


@register.simple_tag
def relative_url(value, field_name, urlencode=None):
    url = "?{}={}".format(field_name, value)
    if urlencode:
        querystring = urlencode.split("&")
        filtered_querystring = filter(
            lambda p: p.split("=")[0] != field_name, querystring
        )
        encoded_querystring = "&".join(filtered_querystring)
        url = "{}&{}".format(url, encoded_querystring)
    return url


register.filter("humanize_hours", humanize_hours)
