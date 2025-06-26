from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from deploy.models import AppLink
from django.db.models import Count
from django.db import transaction

# Create your views here.

def home(request):
    return render(request, 'deploy/appdeploy_full_ui.html')


def get_stats(request):
    total = AppLink.objects.filter(used=True).count()
    remaining = AppLink.objects.filter(used=False).count()

    return JsonResponse({
        "total_installs": total,
        "installs_remaining": remaining,
    })


@csrf_exempt
def get_download_link(request):
    if request.method == 'GET':
        with transaction.atomic():
            link = AppLink.objects.select_for_update(skip_locked=True).filter(
                used = False
            ).first()

            if not link:
                return JsonResponse({"error":"No unused links available"}, status = 404)
            
            link.used = True
            link.save()
            return JsonResponse({"download_link":link.download_link})
        