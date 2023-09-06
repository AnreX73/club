from django import template

from therapy.models import Graphics, ServiceCategory, Contacts

register = template.Library()


@register.inclusion_tag('therapy/components/header.html')
def header():
    logo = Graphics.objects.get(title='логотип')
    no_photo = Graphics.objects.get(title='нет фото')
    service_category = ServiceCategory.objects.exclude(title='Запасной порт').order_by('pk')
    contact_phone = Contacts.objects.get(title='Телефон')
    
   

    return {
        "logo": logo,
        'no_photo': no_photo,
        'service_category':service_category,
        'contact_phone':contact_phone,   
    }
