from django.core.management.base import BaseCommand  # pragma: no cover
from django.core import management  # pragma: no cover


class Command(BaseCommand):  # pragma: no cover
    help = 'Populate application with dummy data to see for yourself what it can do and how it looks like'

    def handle(self, *args, **options):

        self.stdout.write(self.style.SUCCESS('Running Migrating on DB.....'))
        management.call_command('migrate', '--verbosity=1')

        self.stdout.write(self.style.SUCCESS('Preparing to clear the db.....'))
        management.call_command('flush', '--verbosity=1', interactive=False)

        self.stdout.write(self.style.SUCCESS('All is clean, installing new data...'))
        management.call_command('loaddata', 'demodata', '--verbosity=1')

        self.stdout.write(self.style.SUCCESS('Successfully installed dummy environment'))
