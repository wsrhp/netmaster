from django.shortcuts import render
from django.http import HttpResponse
from computers.models import Computer
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'computers/index.html')


def computer(request):
    com_dict = {}
    computers = Computer.objects.all()
    for computer in computers:
        com_dict['com' + str(computer.positionID)] = Computer.objects.get(positionID=computer.positionID)
    return render(request, 'computers/computer_1.html', com_dict)


@csrf_exempt
def com_modify(request):

    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    c_name = None
    c_user = None
    c_occupied = None
    c_pos = None
    ret = "0"
    if request.method == 'POST':
        c_name = request.POST.get("com_name", '')
        c_user = request.POST.get("com_user", '')
        c_occupied = request.POST.get("com_occupied", '')
        c_pos = request.POST.get("com_pos", '')
        if c_occupied == 'true':
            c_occupied = True
        else:
            c_occupied = False

    if c_pos:
        com_m = Computer.objects.get(positionID=c_pos)
        com_m.name = c_name
        com_m.user = c_user
        com_m.occupied = c_occupied
        com_m.save()
        ret = "1"
    else:
        ret = "2"
    response.write(ret)
    return response

