from django.http import JsonResponse
from .models import Project

def project_list(request):
    projects = Project.objects.filter(is_active=True)

    data = []

    for p in projects:
        data.append({
            "title": p.title,
            "description": p.description,
            "role": p.role,
            "tech_stack": p.tech_stack,
            "github_link": p.github_link,
            "live_link": p.live_link,
        })

    return JsonResponse(data, safe=False)