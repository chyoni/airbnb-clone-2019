from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    # help = "This command creates amenities"

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times", help="How many times do you want me to tell you that i love you?"
    #     )

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]

        for fac in facilities:
            Facility.objects.create(name=fac)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} facilities creates "))
