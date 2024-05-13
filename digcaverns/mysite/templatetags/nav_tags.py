from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()

@register.simple_tag(takes_context=True)
def is_active(context, view_name):
    request = context['request']
    try:
        path = reverse(view_name)
    except NoReverseMatch:
        return ""
    return "active" if request.path == path else ""
