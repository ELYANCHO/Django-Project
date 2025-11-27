from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  miembros = Member.objects.all().values()
  column_firstname = Member.objects.all().values('firstname')
  records_elyan = Member.objects.filter(firstname = 'Elyan').values()
  records_AND_name_id = Member.objects.filter(firstname = 'Elyan', id=1).values()
  records_OR_name_id = Member.objects.filter(Q(firstname = 'Jimy') | Q(firstname = 'Ana')).values()
  records_like_start = Member.objects.filter(firstname__startswith = 'M').values()
  records_like_end = Member.objects.filter(firstname__endswith = 'l').values()
  records_like_contains = Member.objects.filter(firstname__contains = 'mi').values()
  order_by_asc = Member.objects.all().order_by('firstname').values()
  order_by_desc = Member.objects.all().order_by('-firstname').values()

  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
    'miembros': miembros, 
    'column_firstname': column_firstname,
    'records_elyan': records_elyan,
    'records_AND_name_id': records_AND_name_id,
    'records_OR_name_id': records_OR_name_id,
    'records_like_start': records_like_start,
    'records_like_end': records_like_end,
    'records_like_contains': records_like_contains,
    'order_by_asc': order_by_asc,
    'order_by_desc': order_by_desc,
  }
  return HttpResponse(template.render(context, request))

def styled_page(request):
  template = loader.get_template('styled_page.html')
  return HttpResponse(template.render())