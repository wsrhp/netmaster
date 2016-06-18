from django.shortcuts import render
from computers.models import Computer


def index(request):
    return render(request, 'computers/index.html')


def computer(request):
    com_dict = {}
    computers = Computer.objects.all()
    for computer in computers:
        com_dict['com' + str(computer.positionID)] = Computer.objects.get(positionID=computer.positionID)
    return render(request, 'computers/computer_1.html', com_dict)
