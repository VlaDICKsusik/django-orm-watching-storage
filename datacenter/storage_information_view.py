from datacenter.models import Visit
from django.shortcuts import render, get_list_or_404


def storage_information_view(request):
    non_closed_visits = []
    visits_not_leaved = get_list_or_404(Visit, leaved_at=None)
    for visit in visits_not_leaved:

        non_closed_visits.append(
            {
                "who_entered": visit.passcard,
                "entered_at": visit.entered_at,
                "duration": visit.format_duration(),
                "is_strange": visit.is_visit_long(),
            }
        )

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, "storage_information.html", context)
