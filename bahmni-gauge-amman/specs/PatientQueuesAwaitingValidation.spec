Scenarios for awaiting validation queues
========================================
Created by swarup, jaseena on 12/23/16

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

Test for queue when Medical File is required
--------------------------------------------
* Create patient "Ameer Medical File" using API with "First Stage Validation" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_OPD_MO" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Verify patient "Ameer Medical File" is present only in "Awaiting Validation - 1st Stage" queue
* Search and select patient "Ameer Medical File" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "First Stage Validation" from observation page and fill details 

   |FIELD                        |VALUE     |
   |-----------------------------|----------|
   |Date Received                |10/10/2016|
   |Is the medical file complete?|Yes       |

* Save the consultation
* Navigate to queues
* Verify patient "Ameer Medical File" is present only in "Awaiting Validation - 1st Stage" queue

Test for queue when Date of presentation of First stage validation is captured
------------------------------------------------------------------------------
* Create patient "Sarah Fstg" using API with "First Stage Validation" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_OPD_MO" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Sarah Fstg" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "First Stage Validation" from observation page and fill details 

   |FIELD               |VALUE     |
   |--------------------|----------|
   |Date of presentation|10/10/2016|

* Save the consultation
* Navigate to queues
* Verify patient "Sarah Fstg" is not present in any queue except Programs and All queues
* End visit for previously created patient using API
* Refresh the queues page
* Verify patient "Sarah Fstg" is not present in any queue except Programs and All queues

Test for queue when Date of presentation of Final validation is captured in "First Stage Validation" visit
----------------------------------------------------------------------------------------------------------
* Create patient "Azeez Final" using API with "First Stage Validation" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_OPD_MO" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Azeez Final" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Final Validation" from observation page and fill details 

   |FIELD               |VALUE     |
   |--------------------|----------|
   |Date of Presentation|10/10/2016|

* Save the consultation
* Navigate to queues
* Verify patient "Azeez Final" is not present in any queue except Programs and All queues
* End visit for previously created patient using API
* Refresh the queues page
* Verify patient "Azeez Final" is not present in any queue except Programs and All queues

Test for queue when Date of presentation of Follow-up validation is captured
----------------------------------------------------------------------------
* Create patient "Halah Fup" using API with "Follow-Up Validation" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_OPD_MO" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Verify patient "Halah Fup" is not present in any queue except Programs and All queues
* Search and select patient "Halah Fup" from "Programs" queue
* Edit "Reconstructive Surgery" Program with following details 

   |programStatus    |
   |-----------------|
   |Network Follow-up|

* Navigate to queues
* Verify patient "Halah Fup" is present only in "Awaiting Validation - Follow Up Stage" queue
* Search and select patient "Halah Fup" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Follow-up Validation" from observation page and fill details 

   |FIELD               |VALUE     |
   |--------------------|----------|
   |Date of presentation|10/10/2016|

* Save the consultation
* Navigate to queues
* Verify patient "Halah Fup" is not present in any queue except Programs and All queues
* End visit for previously created patient using API
* Refresh the queues page
* Verify patient "Halah Fup" is not present in any queue except Programs and All queues

Test for queue when Date of Presentation of Final validation is captured in "Follow-Up Validation" visit
--------------------------------------------------------------------------------------------------------
* Create patient "Yahya Final" using API with "Follow-Up Validation" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_OPD_MO" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Verify patient "Yahya Final" is not present in any queue except Programs and All queues
* Search and select patient "Yahya Final" from "Programs" queue
* Edit "Reconstructive Surgery" Program with following details 

   |programStatus    |
   |-----------------|
   |Network Follow-up|

* Navigate to queues
* Verify patient "Yahya Final" is present only in "Awaiting Validation - Follow Up Stage" queue
* Search and select patient "Yahya Final" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Final Validation" from observation page and fill details 

   |FIELD               |VALUE     |
   |--------------------|----------|
   |Date of Presentation|10/10/2016|

* Save the consultation
* Navigate to queues
* Verify patient "Yahya Final" is not present in any queue except Programs and All queues
* End visit for previously created patient using API
* Refresh the queues page
* Verify patient "Yahya Final" is not present in any queue except Programs and All queues
