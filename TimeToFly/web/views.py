from django.contrib.auth import mixins as auth_mixins
from django.views import generic as views
from django.urls import reverse_lazy
from TimeToFly.web.models import Flight, Passenger
from TimeToFly.auth_app.models import AppUser
from django.shortcuts import redirect


class IndexView(views.TemplateView):
    template_name = 'index.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect('show flights')
    #
    #     return super().dispatch(request, *args, **kwargs)


class AboutView(views.TemplateView):
    template_name = 'about.html'


class NotFoundView(views.TemplateView):
    template_name = '404.html'


class FlightsListView(views.ListView):
    paginate_by = 5
    model = Flight
    template_name = 'flights-list.html'


class ChooseFlightView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Passenger
    template_name = 'flights/book-flight.html'
    fields = ('bookings',)
    success_url = reverse_lazy('show flights')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CreateFlightView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Flight
    template_name = 'create-flight.html'
    fields = '__all__'
    success_url = reverse_lazy('show flights')


class EditFlightView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Flight
    template_name = 'update-flight.html'
    fields = ('flight_code', 'flight_from', 'flight_to', 'flight_cost', 'flight_time',)
    context_object_name = 'flight'
    success_url = reverse_lazy('show flights')


class DeleteFlightView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Flight
    template_name = 'delete-flight.html'
    fields = ('flight_code', 'flight_from', 'flight_to', 'flight_cost', 'flight_time',)
    context_object_name = 'flight'
    success_url = reverse_lazy('show flights')


class CurrentFlightView(views.DetailView):
    model = Flight
    template_name = 'view-booking.html'
    context_object_name = 'flight'
