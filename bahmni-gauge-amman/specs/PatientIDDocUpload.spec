Patient ID Doc Upload Scenarios
===============================

Upload ID documents
-------------------

* Create patient "Alaa" using API with "First Stage Validation" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "ID doc upload" module
* Select patient "Alaa Hasan" in tab "Active Patients"
* Upload following documents in visit "1" 

     |image    |name             |
     |---------|-----------------|
     |xray2.jpg|National Document|
     |ecg.jpeg |Passport         |

* Save ID Doc upload
* Create new visit on radiology upload page 

     |type                  |startDate |endDate   |
     |----------------------|----------|----------|
     |First Stage Validation|03-03-2017|03-03-2017|

* Upload following documents in visit "0" 

     |image    |name             |
     |---------|-----------------|
     |xray.jpeg|National Document|

* Save ID Doc upload
* Expand current visit
* Remove image no "1" on current visit
* Remove image no "2" on current visit
* Undo Remove image no "1" on current visit
* Upload following documents in visit "1" 

     |image   |name    |
     |--------|--------|
     |ecg.jpeg|Passport|

* Save ID Doc upload

