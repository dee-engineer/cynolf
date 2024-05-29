from django.shortcuts import render



def index(request):
    return render(request, 'index.html')


# for Favor, work on user login to user dashboard and admin dashboard
# email, password, remember_me



#for Uche, work on user registration
# first_name, last_name, email, password, confirm_password, address, phone_number, city, state, zip_code, country, date