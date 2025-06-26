import pandas as pd
from django.core.management.base import BaseCommand
from deploy.models import AppLink
from django.utils import timezone

class Command(BaseCommand):
    help = 'Load new app links from Excel file'

    def handle(self, *args, **kwargs):
        filepath = "ABM_Redemption_Codes_Sample.xlsx"
        try:
            df = pd.read_excel(filepath)
        except Exception as e:
            self.stderr.write(f"Excel read error: {e}")
            return

        existing_links = set(AppLink.objects.values_list('download_link', flat=True))
        new_links = []

        for _, row in df.iterrows():
            link = row['Redeem Link']
            if pd.isna(link) or link in existing_links:
                continue
            new_links.append(AppLink(
                app_name=row.get('App Name', 'Unknown'),
                download_link=link,
                created_at=timezone.now()
            ))

        AppLink.objects.bulk_create(new_links, batch_size=500)
        self.stdout.write(self.style.SUCCESS(f"Imported {len(new_links)} new links."))
