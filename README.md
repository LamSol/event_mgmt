# Even Management App (Frappe Framework)

A custom Frappe app built for managing events and attendees with streamlined. Developed as a part of technical Assessment.

## Overview
**Event Management** is a Frappe-based ERP application to manage events, track attendees, and assigned statuses such as confirmed, Pending or cancelled. Dessigned to demostrate full-stack capability using Frappe's Doctypes, modules, and workspace configuration.

## Brief Writeup
### Explaination for the assessment:
I built an Event Management System using the Frappe Framework as part of the technical assessment. The system includes two custom DocTypes: Event Management and Venue, both designed with clean form layouts, validations, and logical structuring. The Event Management form allows users to enter event details such as name, description, date range, capacity, and the linked venue. The Venue form includes name, address, contact info, coordinates, and venue capacity. I implemented Python-based validations to ensure the event end date is after the start date, venue capacity doesn’t exceed the event capacity, and that fields like email, phone number, and coordinates follow the correct formats. I also customized the list views with relevant filters for both DocTypes to enhance usability through the Frappe Desk.

### Challenges:
During development, I faced several challenges. First, setting up the Frappe environment from scratch involved configuring WSL, installing all dependencies, fixing permission issues, and updating the /etc/hosts file manually to access the desk. There was also some confusion when creating the Event DocType due to a naming conflict with an existing system DocType, which required renaming to “Event Management.” Another challenge was understanding the structure of Frappe’s file system and linking validations inside the correct Python files for each DocType. I also encountered syntax and indentation errors that caused system crashes and required careful debugging. Despite all this, the project gave me strong hands-on experience with Frappe and helped reinforce both my backend logic and version control workflow.

---
## Features
- Create and manage events with custom Doctypes
- Add multiple attendees via child table(Attendee)
- Track each attendee's status
- Modular structure following Frappe's best practices
- Custom Workspace setup
- Role-based permissions
- Build with Developer Mode enabled
---

## Tech Stack
- **Frappe Framework**
- **Python**
- **MariaDB**
- **Redis**
- **Node.js** & **Yarn**
- **Ubuntu WSL**

  ## Setup Instructions
  ### Prerequisites:
  - Linux(Ubuntu, use WSL for window users)
  - Python 3.12
  - Node.js
  - Yarn
  - Redis
  - Bench CLI (Frappe)
 
  ### Installation Steps:
  ```bash
  # Create bench environment
  bench init frappe-bench --frappe-branch version-14
  cd frappe-bench

  # Get your custom app
  git clone http://github.com/LamSol/event_mgmt.git apps/event_mgmt

  # Create new site
  bench new-site events.localhost

  # Install the app on site
  bench --site events.localhost install-app event_mgmt

  # Start the server
  bench start

  Then Open browser: http//events.locahost:8000

### Author
Solomon Lamkhothang
MSc Big Data Analytics
Contact: solomonlamkhothang@gmail.com

  
