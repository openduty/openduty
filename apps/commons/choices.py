from django.utils.translation import gettext as _  # pragma: no cover


class Status:  # pragma: no cover
    choice_1, choice_2, choice_3 = 0, 1, 2

    choices = (
        (choice_1, _("Choice 1")),
        (choice_2, _("Choice 2")),
        (choice_3, _("Choice 3"))
    )
