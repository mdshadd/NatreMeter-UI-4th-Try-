from django.shortcuts import render
import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Reading

# Create your views here.

# @permission_required('admin.can_add_log_entry')
def csv_upload(request):
    template = "Result/csv_upload.html"

    prompt = {
        'order': 'Order of the CSV file should be Intensity > Sodium Level'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please select a CSV file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Reading.objects.update_or_create(
            intensity = column[0],
            level = column[1]
        )

    context = {}
    return render(request, template, context)
