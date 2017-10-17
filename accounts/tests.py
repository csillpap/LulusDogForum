# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from views import profile, login, logout, register
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response, redirect


# Testing the views

# Profile page tests

class ProfilePageTest(TestCase):
    def test_profile_page_resolves(self):
        profile_page = resolve('/account/profile/')
        self.assertEqual(profile_page.func, profile)

    def test_profile_page_status_code_is_ok(self):
        profile_page = self.client.get('/account/profile/')
        self.assertEqual(profile_page.status_code, 200)

    def test_check_content_is_correct(self):
        profile_page = self.client.get('/account/profile/')
        self.assertTemplateUsed(profile_page, "profile.html")
        profile_page_template_output = render_to_response("profile.html").content
        self.assertEqual(profile_page.content, profile_page_template_output)


# Registration page tests

class RegistrationPageTest(TestCase):
    def test_registration_page_resolves(self):
        registration_page = resolve('/account/register/')
        self.assertEqual(registration_page.func, register)

    def test_registration_page_status_code_is_ok(self):
        registration_page = self.client.get('/account/register/')
        self.assertEqual(registration_page.status_code, 200)

    def test_registration_page_uses_right_template(self):
        registration_page = self.client.get('/account/register/')
        self.assertTemplateUsed(registration_page, "register.html")


# Login page tests

class LoginPageTest(TestCase):
    def test_login_page_resolves(self):
        login_page = resolve('/account/login/')
        self.assertEqual(login_page.func, login)

    def test_login_page_status_code_is_ok(self):
        login_page = self.client.get('/account/login/')
        self.assertEqual(login_page.status_code, 200)

    def test_login_page_uses_right_template(self):
        login_page = self.client.get('/account/login/')
        self.assertTemplateUsed(login_page, "login.html")


# Logout view tests

class LogoutViewTest(TestCase):
    def test_logout_request_resolves(self):
        logout_request = resolve('/account/logout/')
        self.assertEqual(logout_request.func, logout)

    def test_logout_request_status_code_is_ok(self):
        logout_request = self.client.get('/account/logout/')
        self.assertEqual(logout_request.status_code, 302)

    def test_logout_redirects_to_homepage(self):
        response = self.client.get('/account/logout/')
        self.assertRedirects(response, "/")


