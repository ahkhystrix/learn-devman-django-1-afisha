import json
from django.http import HttpResponse
from django.template import loader

from places.models import Feature


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
                "detailsUrl": "/static/places/" + qs.placeId + ".json"
            }
        }
        features.append(feature)
    context = {"features": json.dumps(features, ensure_ascii=False)}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
