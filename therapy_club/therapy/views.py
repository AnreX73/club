from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from therapy.models import Services, Coaches, Post, ServiceCategory, Gallery, Contacts, Commercial, Graphics, \
    Abonements, ServicesGallery


def index(request):
    logo = Graphics.objects.get(title='логотип')
    contacts = Contacts.objects.exclude(title='Карта').exclude(title='средняя карта').exclude(
        title='мини карта').exclude(title='микро карта')
    contacts_map = Contacts.objects.get(title='Карта')
    contacts_midi_map = Contacts.objects.get(title='средняя карта')
    contacts_mini_map = Contacts.objects.get(title='мини карта')
    contacts_micro_map = Contacts.objects.get(title='микро карта')
    main_image = Graphics.objects.get(title='картинка на главную')
    commerc = Commercial.objects.filter(is_published=True).order_by('-pk')[:1]
    commerc_count = Commercial.objects.filter(is_published=True).count()
    service_cats = ServiceCategory.objects.exclude(title='Запасной порт').order_by('pk')
    favicon = Graphics.objects.get(title='фавикон')
    news = Post.objects.filter(title='Внимание !')

    context = {
        'title': 'THERAPY CLUB',
        'service_cats': service_cats,
        'contacts': contacts,
        'contacts_map': contacts_map,
        'main_image': main_image,
        'commerc': commerc,
        'logo': logo,
        'contacts_midi_map': contacts_midi_map,
        'contacts_mini_map': contacts_mini_map,
        'contacts_micro_map': contacts_micro_map,
        'commerc_count': commerc_count,
        'favicon': favicon,
        'news': news

    }

    return render(request, 'therapy/index.html', context=context)


def service(request, slug):
    favicon = Graphics.objects.get(title='фавикон')
    service_item = get_object_or_404(Services, slug=slug)
    service_abo = Abonements.objects.filter(service_link_id=service_item.id)
    logo = Graphics.objects.get(title='логотип')
    gallery = ServicesGallery.objects.filter(gallery_service_link_id=service_item.id)
    service_links = Services.objects.filter(cat_id=service_item.cat_id).filter(is_published=True).exclude(
        id=service_item.id).values('title', 'slug')
    if service_item.cat_id == 2:
        word = 'одного занятия'
    elif service_item.cat_id == 4:
        word = 'одной программы'
    else:
        word = 'одного сеанса'
    context = {
        'title': service_item.title,
        'service': service_item,
        'service_abo': service_abo,
        'word': word,
        'logo': logo,
        'gallery': gallery,
        'service_links': service_links,
        'favicon': favicon
    }
    return render(request, 'therapy/service.html', context=context)


def rules(request):
    favicon = Graphics.objects.get(title='фавикон')
    rules = Post.objects.get(title='Правила посещения')

    context = {
        'title': 'Правила посещения',
        'rules': rules,
        'favicon': favicon

    }

    return render(request, 'therapy/rules.html', context=context)


class Coaches(ListView):
    favicon = Graphics.objects.get(title='фавикон')
    logo = Graphics.objects.get(title='логотип')
    model = Coaches
    template_name = 'therapy/coach_list.html'
    context_object_name = 'coaches'
    extra_context = {
        'title': 'Наша команда',
        'logo': logo,
        'favicon': favicon

    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def actions_page(request):
    favicon = Graphics.objects.get(title='фавикон')
    actions = Commercial.objects.filter(is_published=True).order_by('-pk')
    logo = Graphics.objects.get(title='логотип')
    context = {
        'title': 'Акции',
        'logo': logo,
        'actions': actions,
        'favicon': favicon
    }

    return render(request, 'therapy/actions.html', context=context)


def prices(request):
    favicon = Graphics.objects.get(title='фавикон')
    services = Services.objects.exclude(title='х-запасной порт')
    cats = ServiceCategory.objects.exclude(title='Запасной порт').order_by('pk')
    abonements = Abonements.objects.all().order_by('pk')

    context = {
        'title': 'Цены',
        'services': services,
        'cats': cats,
        'abonements': abonements,
        'favicon': favicon

    }

    return render(request, 'therapy/prices.html', context=context)


def category_page(request, slug):
    category = get_object_or_404(ServiceCategory, slug=slug)
    title = category.title
    unselected_categories = ServiceCategory.objects.exclude(id=category.id)
    cat_services = Services.objects.filter(cat_id=category.id).filter(is_published=True)
    logo = Graphics.objects.get(title='логотип')
    favicon = Graphics.objects.get(title='фавикон')
    services_count = cat_services.count()
    service_video = Services.objects.exclude(video='').filter(cat_id=category.id).filter(is_published=True).order_by(
        '-pk')[:1]
    service_posts = Post.objects.filter(post_cat_id__cat_id=category.id)
    category_gallery = ServicesGallery.objects.filter(gallery_service_link_id__cat_id=category.id)

    context = {
        'title': title,
        'services': cat_services,
        'category': category,
        'unselected_categories': unselected_categories,
        'logo': logo,
        'favicon': favicon,
        'services_count': services_count,
        'service_video': service_video,
        'service_posts': service_posts,
        'category_gallery': category_gallery
    }
    return render(request, 'therapy/category_page.html', context=context)


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    unselected_posts = Post.objects.exclude(id=post.id).exclude(post_cat__title='х-запасной порт').filter(is_published=True)

    context = {
        'post': post,
        'unselected_posts': unselected_posts

    }
    return render(request, 'therapy/post_page.html', context=context)
