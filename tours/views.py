from django.http import Http404
from django.shortcuts import render
from django.views import View

from stepik_tours.data import departures, tours


class MainView(View):
    def get(self, request):
        context = {
            'tours': tours,
        }
        return render(request, 'tours/index.html', context=context)


class DepartureView(View):
    def get(self, request, departure):
        dep_tours = {id: tour for id, tour in tours.items()
                     if tour['departure'] == departure}

        context = {
            'tours': dep_tours,
            'departure': departures[departure],
            'min_price': min([tour['price'] for tour in dep_tours.values()]),
            'max_price': max([tour['price'] for tour in dep_tours.values()]),
            'min_nights': min([tour['nights'] for tour in dep_tours.values()]),
            'max_nights': min([tour['nights'] for tour in dep_tours.values()])
        }
        return render(request, 'tours/departure.html', context=context)


class TourView(View):
    def get(self, request, id):
        if id not in tours:
            raise Http404
        current_tour = tours[id]
        context = {
            'tour': current_tour,
            'departure': departures[current_tour['departure']]
        }
        return render(request, 'tours/tour.html', context=context)
