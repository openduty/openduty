from django.template.defaultfilters import stringfilter, register
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe


@register.filter(needs_autoescape=True)
@stringfilter
def wbr(value, what, autoescape=None):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x

    parts = str(value).split(what)

    safe_parts = map(esc, parts)

    result = f'{what}<wbr/>'.join(safe_parts)

    return mark_safe(result)

register.filter('wbr', wbr)
