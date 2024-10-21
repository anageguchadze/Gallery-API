# Art Gallery API

## Overview

The Art Gallery API is a RESTful web service built with Django and Django Rest Framework. It provides endpoints for managing artists, artworks, and exhibitions. This API includes filtering options for artworks based on artist and creation date, as well as role-based permissions for enhanced security.

## Features

- **Manage Artists**: Create, read, update, and delete artist profiles.
- **Manage Artworks**: Upload and manage artwork information, including title, description, creation date, and image URL.
- **Manage Exhibitions**: Organize exhibitions and associate multiple artworks.
- **Filtering**: Filter artworks by artist and creation date using Django Filter.
- **Permissions**: Role-based access control to ensure only authorized users can perform specific actions.

## Technologies Used

- Django
- Django Rest Framework
- Django Filter
- Python 3.x
- SQLite (or any other database of your choice)
- Django Admin for managing models

## Installation

### Prerequisites

- Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
- pip (Python package installer).

### Clone the Repository

1. **Clone the repository**:
   ```bash
   git clone https://github.com/anageguchadze/Gallery-API
