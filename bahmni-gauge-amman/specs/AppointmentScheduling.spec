Appointment Scheduling
======================
Created by jaseenam on 01/08/17

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

Create a Service -> Edit a Service -> Delete a Service
------------------------------------------------------
Create a Service
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "Appointment Scheduling" module
* Navigate to Admin Tab
* Verify "Add New Service" button is "displayed"
* Click on "Add New Service" button
* Create new service with below details 

   |Service Name   |Description    |Duration|Start Time|End Time|Max Load|Location|
   |---------------|---------------|--------|----------|--------|--------|--------|
   |Servicename New|description new|20      |08:30 AM  |02:00 PM|10      |OPD     |

* Verify service details of "Servicename New" in Admin Service Page 

   |Service Name   |Location|Duration|Description    |Action     |
   |---------------|--------|--------|---------------|-----------|
   |Servicename New|OPD     |20      |description new|Edit Delete|

Edit a Service
* Edit service "Servicename New" with following details 

   |Service Name      |Description       |Duration|Start Time|End Time|Max Load|Location|
   |------------------|------------------|--------|----------|--------|--------|--------|
   |Servicename Edited|description edited|45      |10:00 AM  |3:00 PM |5       |OPD     |

* Verify service details of "Servicename Edited" in Admin Service Page 

   |Service Name      |Location|Duration|Description       |Action     |
   |------------------|--------|--------|------------------|-----------|
   |Servicename Edited|OPD     |45      |description edited|Edit Delete|

Delete a Service
* Delete service "Servicename Edited"

Create appointment and verify appointment details in List View
--------------------------------------------------------------
* Create patient "Mala Sinha" using API with "Hospital" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "Appointment Scheduling" module
* Navigate to Admin Tab
* Verify "Add New Service" button is "displayed"
* Click on "Add New Service" button
* Create new service with below details 

   |Service Name  |Description    |Duration|Start Time|End Time|Max Load|Location|
   |--------------|---------------|--------|----------|--------|--------|--------|
   |Service Physio|description new|20      |08:30 AM  |02:00 PM|10      |OPD     |

* Navigate to Manage Appointments Tab
* Click on link "Appointments List"
* Click on link "List view"
* Mark cancel if appointment with below details exists 

   |Patient Name|Service       |Provider |Start Time|End Time|Notes    |Status   |
   |------------|--------------|---------|----------|--------|---------|---------|
   |Mala Sinha  |Service Physio|Super Man|10:00 am  |10:20 am|Test note|Scheduled|

* Click on link "Calendar"
* Click on link "Add new appointment"
* Add appointment with below details 

   |Patient|Service       |Provider |Date          |Start Time|Notes    |
   |-------|--------------|---------|--------------|----------|---------|
   |Mala   |Service Physio|Super Man|NOW[dd MMM yy]|10:00 am  |Test note|

* Click on link "List view"
* Verify appointment with below details 

   |Patient Name|Service       |Provider |Start Time|End Time|Notes    |Status   |Location|
   |------------|--------------|---------|----------|--------|---------|---------|--------|
   |Mala Sinha  |Service Physio|Super Man|10:00 am  |10:20 am|Test note|Scheduled|OPD     |

making environment clean again
* Mark cancel if appointment with below details exists 

   |Patient Name|Service       |Provider |Start Time|End Time|Notes    |Status   |
   |------------|--------------|---------|----------|--------|---------|---------|
   |Mala Sinha  |Service Physio|Super Man|10:00 am  |10:20 am|Test note|Scheduled|

* Click on link "Calendar"
* Navigate to Admin Tab
* Delete service "Service Physio"

Conflict appointment
--------------------
* Create patient "Maya Appt" using API with "Hospital" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "Appointment Scheduling" module
* Navigate to Admin Tab
* Verify "Add New Service" button is "displayed"
* Click on "Add New Service" button
* Create new service with below details 

   |Service Name  |Description    |Duration|Start Time|End Time|Max Load|
   |--------------|---------------|--------|----------|--------|--------|
   |Service Physio|description new|20      |08:30 AM  |02:00 PM|10      |

* Navigate to Manage Appointments Tab
* Click on link "Appointments List"
* Click on link "List view"
* Mark cancel if appointment with below details exists 

   |Patient Name|Service       |Provider |Start Time|End Time|Notes    |Status   |
   |------------|--------------|---------|----------|--------|---------|---------|
   |Maya Appt   |Service Physio|Super Man|10:00 am  |10:20 am|Test note|Scheduled|

* Click on link "Calendar"
* Click on link "Add new appointment"
* Add appointment with below details 

   |Patient  |Service       |Provider |Date          |Start Time|Notes    |
   |---------|--------------|---------|--------------|----------|---------|
   |Maya Appt|Service Physio|Super Man|NOW[dd MMM yy]|10:00 am  |Test note|

* Click on link "Add new appointment"
* Add appointment with below details 

   |Patient  |Service       |Provider |Date          |Start Time|Notes    |
   |---------|--------------|---------|--------------|----------|---------|
   |Maya Appt|Service Physio|Super Man|NOW[dd MMM yy]|10:01 am  |Test note|

* Verify popup message as same as "This patient already has an appointment booked at this time. Would you like to proceed or edit the timings?"
* Click on "Back to edit" on popup

making environment clean again

* Click cancel on create appointment
* Click on "Don't save" on popup
* Click on link "List view"
* Mark cancel if appointment with below details exists 

   |Patient Name|Service       |Provider |Start Time|End Time|Notes    |Status   |
   |------------|--------------|---------|----------|--------|---------|---------|
   |Maya Appt   |Service Physio|Super Man|10:00 am  |10:20 am|Test note|Scheduled|
* Click on link "Calendar"
* Navigate to Admin Tab
* Delete service "Service Physio"

Miss appointment
----------------
* Create patient "Sana Appt" using API with "Hospital" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "Appointment Scheduling" module
* Navigate to Admin Tab
* Verify "Add New Service" button is "displayed"
* Click on "Add New Service" button
* Create new service with below details 

   |Service Name  |Description    |Duration|Start Time|End Time|Max Load|
   |--------------|---------------|--------|----------|--------|--------|
   |Service Cardio|description new|20      |08:30 AM  |02:00 PM|10      |
* Navigate to Manage Appointments Tab
* Click on link "Appointments List"
* Click on link "List view"
* Mark cancel if appointment with below details exists 

   |Patient Name|Service       |Provider |Start Time|End Time|Notes    |Status   |
   |------------|--------------|---------|----------|--------|---------|---------|
   |Sana Appt   |Service Cardio|Super Man|10:00 am  |10:20 am|Test note|Scheduled|

* Click on link "Calendar"
* Click on link "Add new appointment"
* Add appointment with below details 

   |Patient  |Service       |Provider |Date          |Start Time|Notes    |
   |---------|--------------|---------|--------------|----------|---------|
   |Sana Appt|Service Cardio|Super Man|NOW[dd MMM yy]|10:00 am  |Test note|

* Click on link "List view"
* Mark as missed appointment with below details 

   |Patient Name|Service       |Provider |Start Time|Notes    |Status   |
   |------------|--------------|---------|----------|---------|---------|
   |Sana Appt   |Service Cardio|Super Man|10:00 am  |Test note|Scheduled|

* Verify appointment with below details 

   |Patient Name|Service       |Provider |Start Time|End Time|Notes    |Status|
   |------------|--------------|---------|----------|--------|---------|------|
   |Sana Appt   |Service Cardio|Super Man|10:00 am  |10:20 am|Test note|Missed|
environment clean
* Navigate to Admin Tab
* Delete service "Service Cardio"
