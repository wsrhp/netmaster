from django import template
from computers.models import Computer

register = template.Library()


@register.inclusion_tag('computers/com.html')
def get_com(position):
    com = Computer.objects.get(positionID=position)
    name = com.name
    user = com.user
    occupied = com.occupied
    return {'com': com, 'positionID': position, 'name':name, 'user': user, 'occupied':occupied}
