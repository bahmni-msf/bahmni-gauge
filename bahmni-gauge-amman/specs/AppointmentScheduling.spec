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

Verify user cannot create service with existing service name
------------------------------------------------------------
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
   |Servicename One|description One|20      |08:30 AM  |02:00 PM|10      |OPD     |

* Verify service details of "Servicename One" in Admin Service Page 

   |Service Name   |Location|Duration|Description    |Action     |
   |---------------|--------|--------|---------------|-----------|
   |Servicename One|OPD     |20      |description One|Edit Delete|

* Click on "Add New Service" button
* Verify user cannot create service with existing service name "Servicename One" 

   |Service Name   |Description    |Duration|Start Time|End Time|Max Load|Location|
   |---------------|---------------|--------|----------|--------|--------|--------|
   |Servicename One|description Two|30      |10:30 AM  |02:00 PM|10      |OPD     |

making environment clean again
* Cancel service creation

Verify user can create service with deleted service name
--------------------------------------------------------
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
   |Servicename Two|description Two|20      |08:30 AM  |02:00 PM|10      |OPD     |

* Verify service details of "Servicename Two" in Admin Service Page 

   |Service Name   |Location|Duration|Description    |Action     |
   |---------------|--------|--------|---------------|-----------|
   |Servicename Two|OPD     |20      |description Two|Edit Delete|

Delete a Service
* Delete service "Servicename Two"
* Click on "Add New Service" button
* Create new service with below details 

   |Service Name   |Description                          |Duration|Start Time|End Time|Max Load|Location|
   |---------------|-------------------------------------|--------|----------|--------|--------|--------|
   |Servicename Two|new service with deleted service name|30      |09:30 AM  |05:00 PM|10      |OPD     |

* Verify service details of "Servicename Two" in Admin Service Page 

   |Service Name   |Location|Duration|Description                          |Action     |
   |---------------|--------|--------|-------------------------------------|-----------|
   |Servicename Two|OPD     |30      |new service with deleted service name|Edit Delete|

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

   |Service Name |Description    |Duration|Start Time|End Time|Max Load|Location|
   |-------------|---------------|--------|----------|--------|--------|--------|
   |Service Ortho|description new|20      |08:30 AM  |02:00 PM|10      |OPD     |

* Navigate to Manage Appointments Tab
* Click on Appointments List link
* Click on Add new appointment link
* Add appointment with below details 

   |Patient|Service      |Date          |Start Time|Notes    |
   |-------|-------------|--------------|----------|---------|
   |Mala   |Service Ortho|NOW[dd MMM yy]|10:00 am  |Test note|

* Click on List view link
* Verify appointment with below details 

   |Patient Name|Service      |Start Time|End Time|Notes    |Status   |Location|
   |------------|-------------|----------|--------|---------|---------|--------|
   |Mala Sinha  |Service Ortho|10:00 am  |10:20 am|Test note|Scheduled|OPD     |

making environment clean again
* Mark cancel if appointment with below details exists 

   |Patient Name|Service      |Start Time|End Time|Notes    |Status   |
   |------------|-------------|----------|--------|---------|---------|
   |Mala Sinha  |Service Ortho|10:00 am  |10:20 am|Test note|Scheduled|

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
* Click on Appointments List link
* Click on Add new appointment link
* Add appointment with below details 

   |Patient  |Service       |Date          |Start Time|Notes    |
   |---------|--------------|--------------|----------|---------|
   |Maya Appt|Service Physio|NOW[dd MMM yy]|10:00 am  |Test note|

* Click on "Add new appointment" link
* Add appointment with below details 

   |Patient  |Service       |Date          |Start Time|Notes    |
   |---------|--------------|--------------|----------|---------|
   |Maya Appt|Service Physio|NOW[dd MMM yy]|10:01 am  |Test note|

* Verify popup message as same as "This patient already has an appointment booked at this time. Would you like to proceed or edit the timings?"
* Cancel appointment creation

making environment clean again
* Click on List view link
* Mark cancel if appointment with below details exists 

   |Patient Name|Service       |Start Time|End Time|Notes    |Status   |
   |------------|--------------|----------|--------|---------|---------|
   |Maya Appt   |Service Physio|10:00 am  |10:20 am|Test note|Scheduled|

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
* Click on Appointments List link
* Click on Add new appointment link
* Add appointment with below details 

   |Patient  |Service       |Date          |Start Time|Notes    |
   |---------|--------------|--------------|----------|---------|
   |Sana Appt|Service Cardio|NOW[dd MMM yy]|02:30 am  |Test note|

* Click on List view link
* Mark as missed appointment with below details 

   |Patient Name|Service       |Start Time|Notes    |Status   |
   |------------|--------------|----------|---------|---------|
   |Sana Appt   |Service Cardio|2:30 am   |Test note|Scheduled|

* Verify appointment with below details 

   |Patient Name|Service       |Start Time|End Time|Notes    |Status|
   |------------|--------------|----------|--------|---------|------|
   |Sana Appt   |Service Cardio|2:30 am   |2:50 am |Test note|Missed|
___________________________________
making environment clean again
* Navigate to Admin Tab
* Delete service "Servicename One" if it exists
* Delete service "Servicename Two" if it exists
* Delete service "Servicename New" if it exists
* Delete service "Service Ortho" if it exists
* Delete service "Service Physio" if it exists
* Delete service "Service Cardio" if it exists
* Delete service "Servicename Edited" if it exists
