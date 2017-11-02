Appointment Scheduling
======================
Created by jaseenam on 01/08/17

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

Create a Service
----------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "Appointment Scheduling" module
* Navigate to Admin Tab
* Verify "Add New Service" button is "displayed"
* Click on "Add New Service" button
* Create new service with below details 

   |Service Name   |Description    |Duration|Start Time|End Time|Max Load|
   |---------------|---------------|--------|----------|--------|--------|
   |Servicename New|description new|20      |08:30 AM  |02:00 PM|10      |

* Verify service details of "Servicename New" in Admin Service Page 

   |Service Name   |Duration|Description    |Action     |
   |---------------|--------|---------------|-----------|
   |Servicename New|20      |description new|Edit Delete|


Edit a Service
--------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "Appointment Scheduling" module
* Navigate to Admin Tab
* Edit service "Servicename New" with following details 

   |Service Name      |Description       |Duration|Start Time|End Time|Max Load|
   |------------------|------------------|--------|----------|--------|--------|
   |Servicename Edited|description edited|45      |10:00 AM  |3:00 PM |5       |

* Verify service details of "Servicename Edited" in Admin Service Page 

   |Service Name      |Duration|Description       |Action     |
   |------------------|--------|------------------|-----------|
   |Servicename Edited|45      |description edited|Edit Delete|

Delete a Service
----------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "Appointment Scheduling" module
* Navigate to Admin Tab
* Delete service "Servicename Edited"

Create appointment
------------------
* Create patient "Mala Sinha" using API with "Hospital" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "Appointment Scheduling" module
* Navigate to Admin Tab
* Verify "Add New Service" button is "displayed"
* Click on "Add New Service" button
* Create new service with below details 

   |Service Name   |Description    |Duration|Start Time|End Time|Max Load|
   |---------------|---------------|--------|----------|--------|--------|
   |Service Physio1|description new|20      |08:30 AM  |02:00 PM|10      |
* Navigate to Manage Appointments Tab
* Click on link "Appointments List"
* Click on link "Add new appointment"
* Add appointment with below details 

   |Patient|Service        |Provider      |Date      |Start Time|
   |-------|---------------|--------------|----------|----------|
   |Mala   |Service Physio1|Billing System|10/10/2017|10:00 am  |
