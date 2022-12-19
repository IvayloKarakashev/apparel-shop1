from django import forms
from django.contrib.auth import views as auth_views, forms as auth_forms, get_user_model, login
from django.forms import EmailField
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views

from firstProject.accounts.forms import UserRegistrationForm, ProfileCreationForm
from firstProject.accounts.models import Profile
from firstProject.utilities.mixins import PageTitleMixin
from firstProject.web.models import Order, WishList




