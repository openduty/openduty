from django.template.defaultfilters import stringfilter, register  # pragma: no cover
from django.utils.html import conditional_escape  # pragma: no cover
from django.utils.safestring import mark_safe  # pragma: no cover


@register.filter(needs_autoescape=True)
@stringfilter
def wbr(value, what, autoescape=None):  # pragma: no cover
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x

    parts = str(value).split(what)

    safe_parts = map(esc, parts)

    result = f'{what}<wbr/>'.join(safe_parts)

    return mark_safe(result)


register.filter('wbr', wbr)
