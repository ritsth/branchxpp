
# branchxpp
#back-end for my web app https://branchapp.xyz/ (currently down because of payment due)</br>
#(Django REST API) deployed through heroku

# BranchXPP Backend

Backend service for the Branch social media app, a plant-focused platform helping users track plant care, share updates, and interact with the community. This backend powers the mobile app built with React Native.

## Overview
This project provides a **Django REST API** that manages user accounts, plant data, reminders, notifications, and social features. It was deployed on **Heroku**.

The backend integrates with **AWS S3** for media storage and supports sensor-based plant care reminders through Arduino and Bluetooth modules.

## Features

### Plant Management
- Create, update, and manage user plants  
- Store plant images in AWS S3  
- Designed to work with a TensorFlow image classifier on the frontend  

### Smart Care Reminders
- Endpoints for scheduling and retrieving watering and care reminders  
- Bluetooth-based notifications supported via sensor integration  

### Social Features
- Upload plant photos  
- Likes, comments, and user interactions  
- User profiles and authentication  

### Hardware Integration
- Compatible with Arduino humidity sensor data  
- Supports Bluetooth notifications to alert users about plant care  

## Tech Stack
- **Backend:** Django, Django REST Framework
- **Storage:** AWS S3  
- **Deployment:** Heroku  
- **Integration:** Arduino + Bluetooth humidity sensor  
- **Frontend:** React Native app (linked below)

## Setup Instructions

### Prerequisites
- Python 3.9 or later  
- pip / virtualenv / pipenv
- AWS credentials for S3  

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ritsth/branchxpp.git
   cd branchxpp
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```
## Deployment
The backend was deployed on **Heroku** using:
- gunicorn  
- whitenoise  
- Heroku Postgres  
- AWS S3 buckets for static and media files  

To redeploy, push changes to Heroku or use a CI/CD pipeline.

## Related Projects
- **Frontend Repository:**  
  https://github.com/ritsth/ReactNativeApp-Branch  

- **Live App:**  
  https://branchapp.xyz/ *(currently offline)*

## License
This project is licensed under the MIT License.







