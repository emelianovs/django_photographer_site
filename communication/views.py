from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views.generic import ListView, CreateView

from .models import Review, Contact


class ReviewsList(ListView):
    model = Review
    context_object_name = 'reviews'
    ordering = ['-date_posted']
    paginate_by = 5


class ReviewAdd(SuccessMessageMixin, CreateView):
    model = Review
    fields = ['name', 'email', 'message_body']
    template_name = 'communication/review_add.html'
    success_url = reverse_lazy('reviews')
    success_message = _('Your review has been added. Thank you!')


class ContactPage(SuccessMessageMixin, CreateView):
    model = Contact
    fields = ['name', 'email', 'phone', 'message_body']
    template_name = 'communication/contacts.html'
    success_url = reverse_lazy('home')
    success_message = _('Your message has been sent. We will get in touch with you as soon as possible. Thank you!')

    def form_valid(self, form):
        data = form.cleaned_data

        field_name = 'date_posted'
        obj = Contact.objects.first()
        date = getattr(obj, field_name)

        email_message = f'From {data["name"]}, {data["email"]}, {data["phone"]}. ' \
                        f'A message: {data["message_body"]}. Received on {date}'

        send_mail(
            'A new message received',
            email_message,
            'from@example.com',
            ['slaveg@mail.ru'],
            fail_silently=False,
        )
        return super().form_valid(form)
