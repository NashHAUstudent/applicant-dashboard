# dashboard/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from portfolio.models import Portfolio

def applicant_list(request):
    """
    Displays a list of all applicants (Users with portfolios).
    """
    # We only want to show users who have actually created a portfolio
    users_with_portfolios = User.objects.filter(portfolio__isnull=False)
    context = {
        'applicants': users_with_portfolios
    }
    return render(request, 'dashboard/applicant_list.html', context)

def applicant_detail(request, user_id):
    """
    Displays the detailed portfolio page for a single applicant.
    """
    applicant = get_object_or_404(User, id=user_id)
    # The portfolio and its projects are accessed via the 'applicant' object in the template
    context = {
        'applicant': applicant
    }
    return render(request, 'dashboard/applicant_detail.html', context)

def applicant_delete(request, user_id):
    """
    Deletes user and their associated portfolio/projects.
    """
    # For a real-world app, use a POST request here for safety.
    # For this project, a direct GET request is fine.
    applicant = get_object_or_404(User, id=user_id)
    applicant.delete()
    return redirect('applicant_list') # Redirect back to the main list