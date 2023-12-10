# Instawork Full-stack Take-home Assignment
#### Time Estimate: 14 hours




## Project Structure

### Directories

- **Instawork/:** Main project directory
  - **main/:** Django app directory
    - **static/:** Static files (CSS and Images)
    - **templates/main/:** HTML templates
    - **models.py:** Database "List" Model
    - **urls.py:** URL patterns
    - **views.py:** Views
  - **web/:**
    - **settings.py:** Project settings
    - **urls.py:** Project level URL patterns
  - **manage.py:** Django Management Script

## Installation

### Prerequisites

Before setting up the project, make sure you have the following prerequisites installed:

- Python (version 3.7 or higher)
- pip

### Local Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/seoluke7203/Instawork.git
    ```

2. **Change the directory to Instawork:**
    ```bash
    cd Instawork
    ```


## Running the Project

After finishing the set up, **Run the server using this command:**
    ```
    python manage.py runserver
    ```


## Models

### List Model
The `List` model represents a contact with specific information such as first name, last name, phone number, email, and role.

#### Fields

- `fname`: CharField with a maximum length of 100 characters, representing the first name of the contact.
- `lname`: CharField with a maximum length of 100 characters, representing the last name of the contact.
- `phone`: CharField with a maximum length of 15 characters, representing the phone number of the contact.
- `email`: CharField with a maximum length of 100 characters, representing the email address of the contact.
- `role`: CharField with a maximum length of 10 characters, representing the role of the contact.
#### Methods

- `__str__(self)`: Returns the email address of the contact when the model instance is converted to a string.

### Example

```python
# Import the List model
from main.models import List

# Create a new contact
new_contact = List.objects.create(
    fname="Luke",
    lname="Seo",
    phone="123-456-7890",
    email="seoluke7203@gmail.com",
    role="Regular"
)

```

## Views

### 1. 'addContact' View
#### Purpose
The `addContact` view is responsible for rendering the form to add a new contact. It handles both GET and POST requests. In case of a POST request, it processes the form data, creates a new contact, and redirects the user to the list page. If the email already exists, it displays an error message on the form.

#### Interactions with Models
- Creates a new contact instance in the 'List' Model

### 2. 'editContact' View
#### Purpose
The editContact view renders the form to edit contact information. It handles both GET and POST requests. In case of a POST request, it updates the contact details and redirects to the list page.

#### Interactions with Models
- Updates the existing contact instance in the List model.

### 3. 'index' View
#### Purpose
Redirects users to 'listpage' View

### 4. 'listPage' View
#### Purpose
The listpage view is responsible for rendering the list of contacts. It handles only GET requests and renders the list page with contact details.

#### Interactions with Models
- Retrieves all contact instances from the List model.



In Ho (Luke) Seo

