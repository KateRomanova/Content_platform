from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework.generics import CreateAPIView

from users.forms import UserRegisterForm
from users.models import User
from users.services import create_stripe_price, create_stripe_session


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")


class NewPasswordView(PasswordResetView):
    form_class = PasswordResetForm
    template_name = "users/new_password.html"
    success_url = reverse_lazy("users:login")


@login_required
def redirect_to_payment(request):
    price = create_stripe_price()
    session_id, payment_link = create_stripe_session(price)
    user = request.user
    user.payment_id = session_id
    user.save()
    return redirect(payment_link)

# class PaymentCreateAPIView(CreateAPIView):
#     serializer_class = PaymentSerializer
#     queryset = Payment.objects.all()
#
#     def perform_create(self, serializer):
#         payment = serializer.save(user=self.request.user)
#         amount = payment.amount
#         price = create_stripe_price(amount)
#         session_id, payment_link = create_stripe_session(price)
#         payment.session_id = session_id
#         payment.payment_link = payment_link
#         payment.save()
