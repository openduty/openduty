from django.utils import timezone  # pragma: no cover
from django.core.management.base import BaseCommand  # pragma: no cover
from apps.incidents.models import Incident  # pragma: no cover
import datetime  # pragma: no cover


class Command(BaseCommand):  # pragma: no cover
    help = 'Auto resolves stuck acknowledged incidents'

    def handle(self, *args, **options):
        limit = timezone.now() - datetime.timedelta(hours=12)
        entities = Incident.objects.filter(occurred_at__lte=limit).filter(event_type=Incident.ACKNOWLEDGE)
        for entity in entities:
            entity.event_type = Incident.RESOLVE
            entity.occured_at = timezone.now()
            entity.save()
            self.stdout.write('Stuck incident id:%s auto resolved because of 12 hours timeout' % entity.id)

        self.stdout.write('Stuck incidents autoresolved!')
