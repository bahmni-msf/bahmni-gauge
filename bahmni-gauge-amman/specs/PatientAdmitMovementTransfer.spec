Patient Admit, Movement and Transfer Home Scenarios
===================================================

Verify Admit to RC, Movement to Kahramana and Transfer Home flow through Disposition - Admit Patient in RC -> Move Patient to Kahramana -> Transfer Home the patient
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
* Create patient "Bed RC" using API with "Hospital" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Search and select patient "Bed RC" from "Programs" queue
* Edit "Reconstructive Surgery" Program with following details 

   |programStatus |
   |--------------|
   |Rehabilitation|

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
* Verify patient "Bed RC" is present only in "Admit to RC" queue
* Search patient "Bed RC" from "Admit to RC" queue
* Verify patient details of "Bed RC" in queue 

   |Name        |Age|Gender|
   |------------|---|------|
   |Bed RC Hasan|11 |M     |

* Click on "Admit To RC" link
* Click on "Rehabilitation Center" button
* Navigate to "Rehabilitation Center 5th floor"
* Assign an empty bed to the patient
* Navigate to patient ADT queues
* Verify patient "Bed RC" is present only in "Admitted" queue
* Search patient "Bed RC" from "Admitted" queue
* Click on "Enter Disposition" link
* Select "Movement to Kahramana" disposition with notes "Move this patient to Kahramana"
* Save the consultation
* Navigate to patient dashboard
* Open the current visit
* Verify details on visit page "Disposition" display control
* Navigate to dashboard
* Click on "bed management" module
* Verify patient "Bed RC" is present only in "Movement to Kahramana" queue
* Search patient "Bed RC" from "Movement to Kahramana" queue
* Verify patient details of "Bed RC" in queue 

   |Name        |Age|Gender|Department           |
   |------------|---|------|---------------------|
   |Bed RC Hasan|11 |M     |Rehabilitation Center|

* Click on "Movement to Kahramana" link
* Click on "Kahramana" button
* Navigate to "Kahramana 2nd floor"
* Assign an empty bed to the patient
* Navigate to patient ADT queues
* Search patient "Bed RC" from "Admitted" queue
* Verify patient details of "Bed RC" in queue 

   |Name        |Age|Gender|Department|
   |------------|---|------|----------|
   |Bed RC Hasan|11 |M     |Kahramana |

* Verify patient "Bed RC" is present only in "Admitted" queue
* Search patient "Bed RC" from "Admitted" queue
* Click on "Enter Disposition" link
* Select "Transfer Home" disposition with notes "Transfer Home this patient"
* Save the consultation
* Navigate to patient dashboard
* Open the current visit
* Verify details on visit page "Disposition" display control
* Navigate to dashboard
* Click on "bed management" module
* Verify patient "Bed RC" is present only in "Transfer Home" queue
* Search patient "Bed RC" from "Transfer Home" queue
* Verify patient details of "Bed RC" in queue 

   |Name        |Age|Gender|Department|
   |------------|---|------|----------|
   |Bed RC Hasan|11 |M     |Kahramana |

* Click on "Transfer Home" link
* Discharge the patient
* Navigate to patient ADT queues
* Verify patient "Bed RC" is not present in any queues

Verify Admit to Ward, Movement to RC and Transfer Home flow through Disposition - Admit Patient in Ward -> Move Patient to RC -> Transfer Home the patient
----------------------------------------------------------------------------------------------------------------------------------------------------------
* Create patient "Bed ward" using API with "Hospital" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Search and select patient "Bed ward" from "Programs" queue
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
* Verify patient "Bed ward" is present only in "Admit to Ward" queue
* Search patient "Bed ward" from "Admit to Ward" queue
* Verify patient details of "Bed ward" in queue 

   |Name          |Age|Gender|
   |--------------|---|------|
   |Bed ward Hasan|11 |M     |

* Click on "Admit To Ward" link
* Click on "Ward" button
* Navigate to "Ward (3rd floor)"
* Assign an empty bed to the patient
* Navigate to patient ADT queues
* Verify patient "Bed ward" is present only in "Admitted" queue
* Search patient "Bed ward" from "Admitted" queue
* Click on "Enter Disposition" link
* Select "Movement to RC" disposition with notes "Move this patient to RC"
* Save the consultation
* Navigate to patient dashboard
* Open the current visit
* Verify details on visit page "Disposition" display control
* Navigate to dashboard
* Click on "bed management" module
* Verify patient "Bed ward" is present only in "Movement to RC" queue
* Search patient "Bed ward" from "Movement to RC" queue
* Verify patient details of "Bed ward" in queue 

   |Name          |Age|Gender|Department|
   |--------------|---|------|----------|
   |Bed ward Hasan|11 |M     |Ward      |

* Click on "Movement to RC" link
* Click on "Rehabilitation Center" button
* Navigate to "Rehabilitation Center 5th floor"
* Assign an empty bed to the patient
* Navigate to patient ADT queues
* Search patient "Bed ward" from "Admitted" queue
* Verify patient details of "Bed ward" in queue 

   |Name          |Age|Gender|Department           |
   |--------------|---|------|---------------------|
   |Bed ward Hasan|11 |M     |Rehabilitation Center|

* Verify patient "Bed ward" is present only in "Admitted" queue
* Search patient "Bed ward" from "Admitted" queue
* Click on "Enter Disposition" link
* Select "Transfer Home" disposition with notes "Transfer Home this patient"
* Save the consultation
* Navigate to patient dashboard
* Open the current visit
* Verify details on visit page "Disposition" display control
* Navigate to dashboard
* Click on "bed management" module
* Verify patient "Bed ward" is present only in "Transfer Home" queue
* Search patient "Bed ward" from "Transfer Home" queue
* Verify patient details of "Bed ward" in queue 

   |Name          |Age|Gender|Department           |
   |--------------|---|------|---------------------|
   |Bed ward Hasan|11 |M     |Rehabilitation Center|

* Click on "Transfer Home" link
* Discharge the patient
* Navigate to patient ADT queues
* Verify patient "Bed ward" is not present in any queues

Verify Admit to Kahramana, Movement to Ward and Transfer Home flow through Disposition - Admit Patient in Kahramana -> Move Patient to Ward -> Transfer Home the patient
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
* Create patient "Bed kahramana" using API with "Hospital" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Search and select patient "Bed kahramana" from "Programs" queue
* Edit "Reconstructive Surgery" Program with following details 

   |programStatus|
   |-------------|
   |Pre-Operative|

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
* Verify patient "Bed kahramana" is present only in "Admit to Kahramana" queue
* Search patient "Bed kahramana" from "Admit to Kahramana" queue
* Verify patient details of "Bed kahramana" in queue 

   |Name               |Age|Gender|
   |-------------------|---|------|
   |Bed kahramana Hasan|11 |M     |

* Click on "Admit to Kahramana" link
* Click on "Kahramana" button
* Navigate to "Kahramana 2nd floor"
* Assign an empty bed to the patient
* Navigate to patient ADT queues
* Verify patient "Bed kahramana" is present only in "Admitted" queue
* Search patient "Bed kahramana" from "Admitted" queue
* Click on "Enter Disposition" link
* Select "Movement to Ward" disposition with notes "Move this patient to Ward"
* Save the consultation
* Navigate to patient dashboard
* Open the current visit
* Verify details on visit page "Disposition" display control
* Navigate to dashboard
* Click on "bed management" module
* Verify patient "Bed kahramana" is present only in "Movement to Ward" queue
* Search patient "Bed kahramana" from "Movement to Ward" queue
* Verify patient details of "Bed kahramana" in queue 

   |Name               |Age|Gender|Department|
   |-------------------|---|------|----------|
   |Bed kahramana Hasan|11 |M     |Kahramana |

* Click on "Movement to Ward" link
* Click on "Ward" button
* Navigate to "Ward 3rd floor"
* Assign an empty bed to the patient
* Navigate to patient ADT queues
* Search patient "Bed kahramana" from "Admitted" queue
* Verify patient details of "Bed kahramana" in queue 

   |Name               |Age|Gender|Department|
   |-------------------|---|------|----------|
   |Bed kahramana Hasan|11 |M     |Ward      |

* Verify patient "Bed kahramana" is present only in "Admitted" queue
* Search patient "Bed kahramana" from "Admitted" queue
* Click on "Enter Disposition" link
* Select "Transfer Home" disposition with notes "Transfer Home this patient"
* Save the consultation
* Navigate to patient dashboard
* Open the current visit
* Verify details on visit page "Disposition" display control
* Navigate to dashboard
* Click on "bed management" module
* Verify patient "Bed kahramana" is present only in "Transfer Home" queue
* Search patient "Bed kahramana" from "Transfer Home" queue
* Verify patient details of "Bed kahramana" in queue 

   |Name               |Age|Gender|Department|
   |-------------------|---|------|----------|
   |Bed kahramana Hasan|11 |M     |Ward      |

* Click on "Transfer Home" link
* Discharge the patient
* Navigate to patient ADT queues
* Verify patient "Bed kahramana" is not present in any queues
