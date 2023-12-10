from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from .models import List


def index(request):
    """
    Redirects to the listpage view.
    """
    return redirect('/listpage/')


def listpage(request):
    """
    Renders the listpage template with a list of contacts.
    """    
    contactlist = List.objects.all()
    return render(request, 'main/listpage.html', {'contactlist': contactlist})

def editContact(request, pk):
    """
    Renders the editContact template with the details of a specific contact.
    
    Parameters:
    - request: HttpRequest object
    - pk: Primary key of the contact to be edited
    """

    contact = List.objects.get(pk=pk)
    return render(request, 'main/editContact.html', {'contact': contact})

def update(request, pk):
    """
    Updates the details of a contact and redirects to the listpage.

    Parameters:
    - request: HttpRequest object
    - pk: Primary key of the contact to be updated
    """
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
    """
    Adds a new contact to the database and redirects to the listpage.

    Parameters:
    - request: HttpRequest object
    """
    if request.method == 'POST':
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        role = request.POST.get('role', '')

        # Check if all required fields are present
        if fname and lname and phone and email and role:
            if List.objects.filter(email=email).exists():
                # Handle the case where the email already exists, if exists, redirect to the same page with an error message
                return render(request, 'main/addContact.html', {'error_Dup_Email': 'Email already exists'})

            List.objects.create(
                fname=fname,
                lname=lname,
                phone=phone,
                email=email,
                role=role
            )
            return redirect('/listpage/')
        
    return render(request, 'main/addContact.html')


def delete_contact(request, email):
    """
    Deletes a contact by email and redirects to the listpage.

    Parameters:
    - request: HttpRequest object
    - email: Email of the contact to be deleted
    """
    try:
        # Attempt to get the contact by email
        contact = List.objects.get(email=email)
        contact.delete()
        messages.success(request, 'Contact deleted successfully.')
    except List.DoesNotExist:
        messages.error(request, 'Contact does not exist.')
    return redirect('listpage')