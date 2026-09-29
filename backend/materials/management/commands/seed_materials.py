from django.core.management.base import BaseCommand
from materials.models import Material


MATERIALS = [
    ("Plastic", "Mixed recyclable plastic", 500),
    ("Aluminium", "Aluminium scrap", 2000),
    ("Copper", "Copper scrap", 5000),
    ("Brass", "Brass scrap", 4000),
    ("Steel", "Steel scrap", 1500),
    ("Iron", "Iron scrap", 1000),
    ("Other Scrap", "Other eligible scrap materials", 800),
]


class Command(BaseCommand):
    help = "Create or update the initial MMAMBA recyclable material catalog."

    def handle(self, *args, **options):
        for name, description, price in MATERIALS:
            material, created = Material.objects.update_or_create(
                name=name,
                defaults={
                    "description": description,
                    "current_price_per_kg": price,
                    "is_active": True,
                },
            )
            action = "Created" if created else "Updated"
            self.stdout.write(
                self.style.SUCCESS(
                    f"{action}: {material.name} — UGX {material.current_price_per_kg}/kg"
                )
            )

        self.stdout.write(self.style.SUCCESS("MMAMBA material catalog seeded successfully."))
