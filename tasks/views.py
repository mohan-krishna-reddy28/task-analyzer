from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .scoring import calculate_task_score

@csrf_exempt
def analyze_tasks(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST allowed")

    tasks = json.loads(request.body.decode("utf-8"))
    for task in tasks:
        task["score"] = calculate_task_score(task)

    tasks = sorted(tasks, key=lambda x: x["score"], reverse=True)
    return JsonResponse(tasks, safe=False)
@csrf_exempt
def suggest_tasks(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST allowed")

    tasks = json.loads(request.body.decode("utf-8"))
    for task in tasks:
        task["score"] = calculate_task_score(task)

    tasks = sorted(tasks, key=lambda x: x["score"], reverse=True)
    top3 = tasks[:3]

    suggestions = []
    for t in top3:
        suggestions.append(
            f"'{t['title']}' is recommended because its importance is {t['importance']} "
            f"and it is due on {t['due_date']} with estimated time {t['estimated_hours']} hours."
        )

    return JsonResponse({"top_tasks": top3, "explanations": suggestions}, safe=False)
