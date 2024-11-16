from django.shortcuts import render, redirect
from medicSearch.models import Profile
from django.db.models import Q
from django.core.paginator import Paginator

def home_view(request):
    return render(request, 'home/home.html', status=200)

def list_profile_view(request, medic_id=None):
    if medic_id is None and request.user.is_authenticated:
        medic_id = request.user.medic_id
    if not request.user.is_authenticated:
        medic_id = 0

def list_medics_view(request):
    name = request.GET.get('name')
    speciality = request.GET.get('speciality')
    neighborhood = request.GET.get('neighborhood')
    city = request.GET.get('city')
    state = request.GET.get('state')

    medics = Profile.objects.filter(role=2)

    if name is not None and name != '':
        medics = medics.filter(Q(user__first_name__contains=name) | Q(user__username__contains=name))

    if speciality is not None:
        medics = medics.filter(specialties__id=speciality)

    if neighborhood is not None:
        medics = medics.filter(addresses__neighborhood=neighborhood)
    else:
        if city is not None:
            medics = medics.filter(addresses__neighborhood__city=city)
        elif state is not None:
            medics = medics.filter(addresses__neighborhood__city__state=state)

    if len(medics) > 0:
        paginator = Paginator(medics, 8)
        page = request.GET.get('page')
        medics = paginator.get_page(page)

    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()    

    context = {
       'medics': medics,
       'parameters': parameters
    } 

    return render(request, 'medic/medics.html', context)

def add_favorite_view(request):
    page = request.POST.get('page')
    name = request.POST.get('name')
    speciality = request.POST.get('speciality')
    neighborhood = request.POST.get('neighborhood')
    city = request.POST.get('city')
    state = request.POST.get('state')
    medic_id = request.POST.get('medic_id')

    try:
        profile = Profile.objects.filter(user=request.user).first()
        medic = Profile.objects.filter(user__medic_id=id).first()
        profile.favorites.add(medic.user)
        profile.save()
        msg = 'Favorito adicionado com sucesso'
        _tipe = 'Success'
    except Exception as e:
        msg = 'Um erro ao salvar o médico nos favoritos'
        _tipe = 'danger'

    if page:
        arguments = '?page=%s' % (page)
    else:
        arguments = '?page=1'

    if name:
        arguments += '&name=%s' % name

    if speciality:
        arguments += '&speciality=%s' % speciality

    if neighborhood:
        arguments += '&neighborhood=%s' % neighborhood

    if city:
        arguments += '&city=%s' % city

    if state:
        arguments += '&state=%s' % state

    arguments += '&msg=%s&type=%s' % (msg, _tipe)

    return redirect(to='/medic/%s' % arguments)    
