"""Views for the farms app."""

from django.http import HttpResponse, JsonResponse
from django.views.generic import CreateView, DetailView

from .forms import AddressForm
from .models import Address


def get_places(request):

    # context = RequestContext(request)
#     cat_id = None
    if request.method == 'GET':
        postal_code = request.GET['postal_code']
#
    data = {'postal_code': postal_code}
#     likes = 0
#     if cat_id:
#         category = Category.objects.get(id=int(cat_id))
#         if category:
#                         likes = category.likes + 1
#             category.likes =  likes
#             category.save()
#
    return JsonResponse(data)


class AddressDetailView(DetailView):
    pass


class AddressCreateView(CreateView):

    model = Address
    form_class = AddressForm
