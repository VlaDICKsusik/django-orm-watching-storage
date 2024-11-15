from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_list_or_404


def active_passcards_view(request):
    visits_not_leaved = get_list_or_404(Visit, leaved_at=None)
    all_passcards = get_list_or_404(Passcard, pk=1)
    pass_users = get_list_or_404(Passcard, is_active=True)

    context = {
        "active_passcards": pass_users,  # люди с активными пропусками
    }
    return render(request, "active_passcards.html", context)
