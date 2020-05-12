from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.urls import reverse
from django.views.generic import DetailView, TemplateView, UpdateView
from django.views.generic.edit import FormView

from froide.helper.utils import get_redirect

from .models import Donor
from .forms import DonationGiftForm, DonationFormFactory, DonorDetailsForm
from .services import confirm_donor_email


@require_POST
def make_order(request, category):
    form = DonationGiftForm(
        data=request.POST, category=category, request=request
    )
    if form.is_valid():
        form.save(request)
        return get_redirect(request)

    messages.add_message(request, messages.ERROR, 'Form-Fehler!')
    return get_redirect(request, next=request.META.get('HTTP_REFERER', '/'))


class DonationView(FormView):
    template_name = 'fds_donation/forms/donation.html'

    def get_form_action(self):
        return reverse('fds_donation:donate')

    def get_form(self, form_class=None):
        """Return an instance of the form to be used in this view."""

        form_kwargs = self.get_form_kwargs()
        form_factory = DonationFormFactory(
            reference=self.request.GET.get('pk_campaign', ''),
            keyword=self.request.GET.get('pk_keyword', '')
        )
        form = form_factory.make_form(
            user=self.request.user,
            action=self.get_form_action(),
            **form_kwargs
        )
        return form

    def form_valid(self, form):
        order, related_obj = form.save()
        method = form.cleaned_data['payment_method']
        return redirect(order.get_absolute_payment_url(method))


class DonationCompleteView(TemplateView):
    template_name = 'fds_donation/donation_complete.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['order'] = self.request.GET.get('order', '')
        ctx['subscription'] = self.request.GET.get('subscription', '')
        ctx['email'] = self.request.GET.get('email', '')
        return ctx


class DonorMixin:
    model = Donor
    slug_field = 'uuid'
    slug_url_kwarg = 'token'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        response = self.should_redirect_user()
        if response:
            return response
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        response = self.should_redirect_user()
        if response:
            return response
        return super().post(request, *args, **kwargs)

    def should_redirect_user(self):
        is_auth = self.request.user.is_authenticated
        if is_auth and self.object.user == self.request.user:
            # User is logged in and donor user, redirect to user view
            return redirect(self.get_user_url())
        return None

    def get_user_url(self):
        return reverse('fds_donation:donor-user')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.email_confirmed:
            confirm_donor_email(obj, request=self.request)

        return obj


class DonorView(DonorMixin, DetailView):
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        donations = self.object.donations.all()
        try:
            last_donation = donations[0]
        except IndexError:
            last_donation = None
        ctx.update({
            'subscription': self.object.subscription,
            'donations': donations,
            'last_donation': last_donation,
        })
        return ctx


class DonorUserMixin:
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object is None:
            return self.no_donor_found(request)
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object is None:
            return self.no_donor_found(request)
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def no_donor_found(self, request):
        messages.add_message(
            request, messages.INFO,
            _("We have no associated donations with your account. "
                "If you have donated, let us know! "
                "Otherwise feel free to donate below."
            )
        )
        return redirect('/spenden/')

    def get_object(self, queryset=None):
        try:
            return Donor.objects.get(
                user=self.request.user,
                email_confirmed__isnull=False
            )
        except Donor.DoesNotExist:
            return None


class DonorUserView(LoginRequiredMixin, DonorUserMixin, DonorView):
    pass


class DonorChangeView(DonorMixin, UpdateView):
    form_class = DonorDetailsForm

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.SUCCESS,
            _("Your donor info has been updated!")
        )
        return super().form_valid(form)

    def get_user_url(self):
        return reverse('fds_donation:donor-user-change')


class DonorChangeUserView(LoginRequiredMixin, DonorUserMixin, DonorChangeView):
    pass
