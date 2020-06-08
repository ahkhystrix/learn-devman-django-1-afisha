import json
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse

from places.models import Feature, Image


def show_index(request):
    template = loader.get_template('index.html')
    features = []
    for qs in Feature.objects.all():
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [qs.coordinates_lng, qs.coordinates_lat]
            },
            "properties": {
                "title": qs.description_short,
                "placeId": qs.placeId,
                "detailsUrl": reverse('get_place', kwargs={'id': qs.id})
            }
        }
        features.append(feature)
    context = {"features": json.dumps(features, ensure_ascii=False)}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def get_place(request, id):
    qs = get_object_or_404(Feature, id=id)
    images = []
    for item in Image.objects.filter(feature_id=id):
        images.append(item.image.url)
    feature = {
        "title": qs.title,
        "imgs": images,
        "description_short": qs.description_short,
        "description_long": qs.description_long,
        "coordinates": {
            "lng": qs.coordinates_lng,
            "lat": qs.coordinates_lat,
        }
    }
    return JsonResponse(
        feature,
        safe=False,
        json_dumps_params={'ensure_ascii': False}
    )
