from datetime import datetime

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Imaginary function to handle an uploaded file.
from .utils import get_digital_data


@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        started_at = datetime.now()
        data = get_digital_data(request.FILES['file'])
        ended_at = datetime.now()
        data['time_taken_upload'] = str((ended_at - started_at).seconds) + 'seconds'
        return JsonResponse(data)