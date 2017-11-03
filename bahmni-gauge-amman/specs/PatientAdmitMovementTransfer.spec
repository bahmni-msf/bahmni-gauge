Patient Admit, Movement and Transfer Home Scenarios
===================================================


Verify Admit to RC flow through Disposition
-------------------------------------------
* Create patient "Bed Mngmt" using API with "Hospital" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Search and select patient "Bed Mngmt" from "Programs" queue
* Edit "Reconstructive Surgery" Program with following details 

   |programStatus             |
   |--------------------------|
   |Surgical / Hospitalisation|

* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Disposition" tab
* Select "Admit to RC" disposition with notes "Admit this patient to RC"
* Save the consultation
* Navigate to patient dashboard
* Open the current visit
* Verify details on visit page "Disposition" display control
* Navigate to dashboard
* Click on "bed management" module
* Verify patient "Bed Mngmt" is present only in "Admit to RC" queue

Admit Patient in RC
-------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "bed management" module
* Search patient "Bed Mngmt" from "Admit to RC" queue
* Verify patient details of "Bed Mngmt" in queue 

   |Name          |Age|Gender|
   |--------------|---|------|
   |Bed Mngmt Hasan|11 |M     |

* Click on "Admit To RC" link
* Click on "Rehabilitation Center" button
* Navigate to "Rehabilitation Center 4th floor"
* Assign an empty bed to the patient
* Navigate to patient ADT queues
* Verify patient "Bed Mngmt" is present only in "Admitted" queue

Verify Admit to Ward flow through Disposition
---------------------------------------------
* Create patient "Bed Mngmt ward" using API with "Hospital" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Search and select patient "Bed Mngmt ward" from "Programs" queue
* Edit "Reconstructive Surgery" Program with following details 

   |programStatus             |
   |--------------------------|
   |Surgical / Hospitalisation|

* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Disposition" tab
* Select "Admit to Ward" disposition with notes "Admit this patient to Ward"
* Save the consultation
* Navigate to patient dashboard
* Open the current visit
* Verify details on visit page "Disposition" display control
* Navigate to dashboard
* Click on "bed management" module
* Verify patient "Bed Mngmt ward" is present only in "Admit to Ward" queue

Admit Patient in Ward
---------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "bed management" module
* Search patient "Bed Mngmt ward" from "Admit to Ward" queue
* Verify patient details of "Bed Mngmt ward" in queue 

   |Name               |Age|Gender|
   |-------------------|---|------|
   |Bed Mngmt ward Hasan|11 |M     |

* Click on "Admit To Ward" link
* Click on "Ward" button
* Navigate to "Ward 2nd floor"
* Assign an empty bed to the patient
* Navigate to patient ADT queues
* Verify patient "Bed Mngmt ward" is present only in "Admitted" queue

Verify Admit to Kahramana Patient flow through Disposition
----------------------------------------------------------
* Create patient "Bed Mngmt kahramana" using API with "Hospital" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Search and select patient "Bed Mngmt kahramana" from "Programs" queue
* Edit "Reconstructive Surgery" Program with following details 

   |programStatus              |
   |---------------------------|
   |Surgical / Hospitalisation|

* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Disposition" tab
* Select "Admit to Kahramana" disposition with notes "Admit this patient to Kahramana"
* Save the consultation
* Navigate to patient dashboard
* Open the current visit
* Verify details on visit page "Disposition" display control
* Navigate to dashboard
* Click on "bed management" module
* Verify patient "Bed Mngmt kahramana" is present only in "Admit to Kahramana" queue

Admit Patient in Kahramana
--------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "bed management" module
* Search patient "Bed Mngmt kahramana" from "Admit to Kahramana" queue
* Verify patient details of "Bed Mngmt kahramana" in queue 

   |Name                    |Age|Gender|
   |------------------------|---|------|
   |Bed Mngmt kahramana Hasan|11 |M     |

* Click on "Admit to Kahramana" link
* Click on "Kahramana" button
* Navigate to "Kahramana 1st floor"
* Assign an empty bed to the patient
* Navigate to patient ADT queues
* Verify patient "Bed Mngmt kahramana" is present only in "Admitted" queue

Verify Movement to RC flow through Disposition
----------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Search and select patient "Bed Mngmt ward" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Disposition" tab
* Select "Movement to RC" disposition with notes "Move this patient to RC"
* Save the consultation
* Navigate to patient dashboard
* Open the current visit
* Verify details on visit page "Disposition" display control
* Navigate to dashboard
* Click on "bed management" module
* Verify patient "Bed Mngmt ward" is present only in "Movement to RC" queue

Move Patient to RC
------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "bed management" module
* Search patient "Bed Mngmt ward" from "Movement to RC" queue
* Verify patient details of "Bed Mngmt ward" in queue 

   |Name               |Age|Gender|Department|
   |-------------------|---|------|----------|
   |Bed Mngmt ward Hasan|11 |M     |Ward      |

* Click on "Movement to RC" link
* Click on "Rehabilitation Center" button
* Navigate to "Rehabilitation Center 4th floor"
* Assign an empty bed to the patient
* Navigate to patient ADT queues
* Search patient "Bed Mngmt ward" from "Admitted" queue
* Verify patient details of "Bed Mngmt ward" in queue 

   |Name               |Age|Gender|Department           |
   |-------------------|---|------|---------------------|
   |Bed Mngmt ward Hasan|11 |M     |Rehabilitation Center|

* Verify patient "Bed Mngmt ward" is present only in "Admitted" queue

Verify Movement to Ward flow through Disposition
------------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Search and select patient "Bed Mngmt kahramana" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Disposition" tab
* Select "Movement to Ward" disposition with notes "Move this patient to Ward"
* Save the consultation
* Navigate to patient dashboard
* Open the current visit
* Verify details on visit page "Disposition" display control
* Navigate to dashboard
* Click on "bed management" module
* Verify patient "Bed Mngmt kahramana" is present only in "Movement to Ward" queue

Move Patient to Ward
--------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "bed management" module
* Search patient "Bed Mngmt kahramana" from "Movement to Ward" queue
* Verify patient details of "Bed Mngmt kahramana" in queue 

   |Name                    |Age|Gender|Department|
   |------------------------|---|------|----------|
   |Bed Mngmt kahramana Hasan|11 |M     |Kahramana |

* Click on "Movement to Ward" link
* Click on "Ward" button
* Navigate to "Ward 2nd floor"
* Assign an empty bed to the patient
* Navigate to patient ADT queues
* Search patient "Bed Mngmt kahramana" from "Admitted" queue
* Verify patient details of "Bed Mngmt kahramana" in queue 

   |Name                    |Age|Gender|Department|
   |------------------------|---|------|----------|
   |Bed Mngmt kahramana Hasan|11 |M     |Ward      |

* Verify patient "Bed Mngmt kahramana" is present only in "Admitted" queue

Verify Movement to Kahramana flow through Disposition
-----------------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Search and select patient "Bed Mngmt" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Disposition" tab
* Select "Movement to Kahramana" disposition with notes "Move this patient to Kahramana"
* Save the consultation
* Navigate to patient dashboard
* Open the current visit
* Verify details on visit page "Disposition" display control
* Navigate to dashboard
* Click on "bed management" module
* Verify patient "Bed Mngmt" is present only in "Movement to Kahramana" queue

Move Patient to Kahramana
-------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "bed management" module
* Search patient "Bed Mngmt" from "Movement to Kahramana" queue
* Verify patient details of "Bed Mngmt" in queue 

   |Name          |Age|Gender|Department           |
   |--------------|---|------|---------------------|
   |Bed Mngmt Hasan|11 |M     |Rehabilitation Center|

* Click on "Movement to Kahramana" link
* Click on "Kahramana" button
* Navigate to "Kahramana 1st floor"
* Assign an empty bed to the patient
* Navigate to patient ADT queues
* Search patient "Bed Mngmt" from "Admitted" queue
* Verify patient details of "Bed Mngmt" in queue 

   |Name          |Age|Gender|Department|
   |--------------|---|------|----------|
   |Bed Mngmt Hasan|11 |M     |Kahramana |

* Verify patient "Bed Mngmt" is present only in "Admitted" queue

Verify Transfer Home flow through Disposition
---------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Search and select patient "Bed Mngmt ward" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Disposition" tab
* Select "Transfer Home" disposition with notes "Transfer Home this patient"
* Save the consultation
* Navigate to patient dashboard
* Open the current visit
* Verify details on visit page "Disposition" display control
* Navigate to dashboard
* Click on "bed management" module
* Verify patient "Bed Mngmt ward" is present only in "Transfer Home" queue

Transfer Home the patient
-------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "bed management" module
* Search patient "Bed Mngmt ward" from "Transfer Home" queue
* Verify patient details of "Bed Mngmt ward" in queue 

   |Name               |Age|Gender|Department           |
   |-------------------|---|------|---------------------|
   |Bed Mngmt ward Hasan|11 |M     |Rehabilitation Center|

* Click on "Transfer Home" link
* Discharge the patient
* Navigate to patient ADT queues
* Verify patient "Bed Mngmt ward" is not present in any queues
