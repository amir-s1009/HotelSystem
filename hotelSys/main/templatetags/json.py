from django import template
import json

register = template.Library()

@register.simple_tag
def jsonToPython(value):
    return json.loads(value)