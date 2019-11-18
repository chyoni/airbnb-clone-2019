import random
from django.contrib.admin.utils import flatten
from django.core.management.base import BaseCommand
from django_seed import Seed
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):

    # help = "This command creates many rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many rooms do you want to create ? ",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        house_rules = room_models.HouseRule.objects.all()

        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 8),
                "price": lambda x: random.randint(10, 250),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        # seeder를 사용해서 만들어진 레코드의 pk를 얻음
        created_room = seeder.execute()
        created_flatten = flatten(list(created_room.values()))

        # 그 pk를 통해서 해당 룸에 대한 레코드를 찾고 그 룸에 photo들을 생성해 집어넣는 for 문
        for pk in created_flatten:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 15)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1,31)}.webp",
                )
            for a in amenities:
                random_number = random.randint(0, 15)
                if random_number % 2 == 0:
                    room.amenities.add(a)
            for f in facilities:
                random_number = random.randint(0, 15)
                if random_number % 2 == 0:
                    room.facilities.add(f)
            for h in house_rules:
                random_number = random.randint(0, 15)
                if random_number % 2 == 0:
                    room.house_rules.add(h)

        self.stdout.write(self.style.SUCCESS(f"{number} rooms create !"))
