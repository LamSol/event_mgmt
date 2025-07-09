# Even Management App (Frappe Framework)

A custom Frappe app built for managing events and attendees with streamlined. Developed as a part of technical Assessment.

## Overview
**Event Management** is a Frappe-based ERP application to manage events, track attendees, and assigned statuses such as confirmed, Pending or cancelled. Dessigned to demostrate full-stack capability using Frappe's Doctypes, modules, and workspace configuration.

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

  # Install requirements
  bench get-app event-mgmt

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

  
