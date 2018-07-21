from datetime import datetime

import requests
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Imaginary function to handle an uploaded file.
from .utils import get_digital_data, get_all_droplets


@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        started_at = datetime.now()
        file_object = request.FILES['file']
        data = get_digital_data(file_object)
        ended_at = datetime.now()
        data['time_taken_upload'] = str((ended_at - started_at).seconds) + 'seconds'

        best_droplet = data.pop('best_droplet')
        data['best_ip'] = best_droplet.ip_address
        # push_file(best_droplet, file_object)

        return JsonResponse(data)


@csrf_exempt
def upload(request):
    print(request.FILES)
    if request.method == 'POST' and 'upload_file' in request.FILES:
        myfile = request.FILES['upload_file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        return HttpResponse('File {} successfully uploaded'.format(filename))


@csrf_exempt
def push_upload(request):
    file_obj = request.FILES['file']
    print(request.POST)
    best_droplet = int(request.POST['best_droplet_index'][0])
    my_droplets = get_all_droplets()
    best_droplet = my_droplets[best_droplet]

    ip_address = best_droplet.ip_address
    files = {'upload_file': file_obj}

    upload_url = 'http://{}/upload_file:9000'.format(ip_address)
    r = requests.post(upload_url, files=files)
    response = {}
    response['status'] = r.status_code
    response['message'] = "Successfully submitted"
    return JsonResponse(response)
