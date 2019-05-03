try:  # pragma: no cover
    from functools import wraps
except ImportError:  # pragma: no cover
    from django.utils.functional import wraps
import inspect  # pragma: no cover


def disable_for_loaddata(signal_handler):  # pragma: no cover
    @wraps(signal_handler)
    def wrapper(*args, **kwargs):
        for fr in inspect.stack():
            if inspect.getmodulename(fr[1]) == 'loaddata':
                return
        signal_handler(*args, **kwargs)
    return wrapper
