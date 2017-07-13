Patient Medical Doc Upload Scenarios
====================================

Upload Medical documents
------------------------

* Create patient "Nisa" using API with "First Stage Validation" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "radiology upload" app
* Select patient "Nisa" in tab "Active Patients"
* Upload following images in visit "1" 

     |image    |name       |
     |---------|-----------|
     |xray.jpeg|X-ray      |
     |xray2.jpg|MRI (photo)|
     
* Save radiology upload
* Create new visit on radiology upload page 

     |type                  |startDate |endDate   |
     |----------------------|----------|----------|
     |First Stage Validation|01-03-2017|02-03-2017|
     
* Upload following images in visit "0" 

     |image    |name |
     |---------|-----|
     |xray.jpeg|X-ray|
     
* Save radiology upload
* Expand current visit
* Remove image no "1" on current visit
* Remove image no "2" on current visit
* Undo Remove image no "1" on current visit
* Upload following images in visit "1" 

     |image    |name        |
     |---------|------------|
     |xray.jpeg|X-ray       |
     |ecg.jpeg |Cardiac Echo|
     
* Save radiology upload
