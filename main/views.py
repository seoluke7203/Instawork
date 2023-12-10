from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from .models import List

def index(request):
    return redirect('/listpage/')

def listpage(request):
    contactlist = List.objects.all()
    return render(request, 'main/listpage.html', {'contactlist': contactlist})

def editContact(request, pk):
    contact = List.objects.get(pk=pk)
    return render(request, 'main/editContact.html', {'contact': contact})

def update(request, pk):
    list = List.objects.get(pk=pk)
    if request.method == 'POST':
        list.fname = request.POST['newFname']
        list.lname = request.POST['newLname']
        list.phone = request.POST['newPhone']
        list.email = request.POST['newEmail']
        list.role = request.POST['newRole']
        list.save()
        return redirect('/listpage/')
    else:
        return render(request, 'main/editContact.html', {'list': list})
    
def addContact(request):
    if request.method == 'POST':
        # Use get() method to safely retrieve values from the POST data
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        role = request.POST.get('role', '')

        # Check if all required fields are present
        if fname and lname and phone and email and role:
            if List.objects.filter(email=email).exists():
                # Handle the case where the email already exists
                return render(request, 'main/addContact.html', {'error_Dup_Email': 'Email already exists'})

            List.objects.create(
                fname=fname,
                lname=lname,
                phone=phone,
                email=email,
                role=role
            )
            return redirect('/listpage/')  # Redirect to the desired page after successful submission

    return render(request, 'main/addContact.html')


def delete_contact(request, email):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        try:
            # Attempt to get the contact by email
            contact = List.objects.get(email=email)
            contact.delete()
            messages.success(request, 'Contact deleted successfully.')
        except List.DoesNotExist:
            messages.error(request, 'Contact does not exist.')
    else:
        messages.error(request, 'You are not authenticated to delete contacts.')

    return redirect('listpage')