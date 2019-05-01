from django.contrib.auth.models import Group, User
from datetime import datetime
from django.utils import timezone
from schedule.periods import Day
from datetime import timedelta
from apps.policies.models import SchedulePolicyRule
from apps.services.models import Service


"""def get_current_events_users(calendar):
    now = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
    result = []
    day = Day(calendar.events.all(), now)
    for o in day.get_occurrences():
        if o.start <= now <= o.end:
            usernames = o.event.title.split(',')
            print usernames
            for username in usernames:
                result.append(User.objects.get(username=username.strip()))
    return result

"""


def get_current_events_users(calendar):
    now = timezone.now()
    result = []
    day = Day(calendar.events.all(), now)
    for o in day.get_occurrences():
        if o.start <= now <= o.end:
            items = o.event.title.split(',')
            for item in items:
                if Group.objects.filter(name=item.strip()).exists():
                    for user in User.objects.filter(groups__name=item.strip()):
                        user.came_from_group = item.strip()
                        result.append(user)
                else:
                    result.append(User.objects.get(username=item.strip()))
    return result


def get_events_users_inbetween(calendar, since, until):
    delta = until - since
    result = {}
    added_users = []
    for i in range(delta.days + 1):
        that_day = since + timedelta(days=i)
        if not timezone.is_aware(that_day):
            that_day = timezone.make_aware(that_day, timezone.get_current_timezone())
        day = Day(calendar.events.all(), that_day)
        for o in day.get_occurrences():
            if o.start <= that_day <= o.end:
                items = o.event.title.split(',')
                for item in items:
                    username = item.strip()
                    if Group.objects.filter(name=username):
                        for user in User.objects.filter(groups__name=username):
                            if user not in added_users:
                                result[username] = {
                                    "start": o.start,
                                    "person": user.username,
                                    "end": o.end,
                                    "email": user.email
                                }
                                added_users.append(user)
                    else:
                        if username not in result.keys():
                            user_instance = User.objects.get(username=username)
                            result[username] = {
                                "start": o.start,
                                "person": username,
                                "end": o.end,
                                "email": user_instance.email
                            }
    return result.values()


def get_escalation_for_service(service):
    result = []
    if service.notifications_disabled:
        return result
    rules = SchedulePolicyRule.get_rules_for_service(service)
    print(rules)
    for item in rules:
        print(item.schedule)
        print(item.user_id)
        print(item.group_id)
        if item.schedule:
            current_events_users = get_current_events_users(item.schedule)
            for user in current_events_users:
                if user not in result:
                    result.append(user)
        if item.user_id:
            if item.user_id not in result:
                result.append(item.user_id)
        if item.group_id:
            for user in item.group_id.user_set.all():
                if user not in result:
                    result.append(user)
    return result


def services_where_user_is_on_call(user):
    from django.db.models import Q
    services = Service.objects.filter(
        Q(policy__rules__user_id=user) | Q(policy__rules__schedule__event__title__icontains=user)
    )
    return services
