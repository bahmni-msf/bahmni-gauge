Patient Admit, Movement and Transfer Home Scenarios
===================================================


Verify Admit to RC flow through Disposition
-------------------------------------------
* Create patient "Sid rc" using API with "Hospital" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Search and select patient "Sid rc" from "Programs" queue
* Edit "Reconstructive Surgery" Program with following details
| programStatus |
| Surgical      |

* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Disposition" tab
* Select "Admit to RC" disposition with notes "Admit this patient to RC"
* Save the consultation
* Navigate to patient dashboard
* Open the current visit
* Verify details on visit page "Disposition" display control
* Navigate to dashboard
* Click on bed management app
* Verify patient "Sid rc" is present only in "Admit to RC" queue

Admit Patient in RC
-------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on bed management app
* Search patient "Sid rc" from "Admit to RC" queue
* Verify patient details of "Sid rc" in queue
|Name           | Age   | Gender    |
|Sid rc Hasan   | 11	| M         |

* Click on "Admit To RC" link
* Click on "Rehabilitation Center" button
* Navigate to "Rehabilitation Center 4th floor"
* Assign an empty bed to the patient
* Navigate to patient ADT queues
Verify patient "Sid rc" is present only in "Admitted" queue

Verify Admit to Ward flow through Disposition
---------------------------------------------
* Create patient "Sid ward" using API with "Hospital" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Search and select patient "Sid ward" from "Programs" queue
* Edit "Reconstructive Surgery" Program with following details
| programStatus |
| Surgical      |

* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Disposition" tab
* Select "Admit to Ward" disposition with notes "Admit this patient to Ward"
* Save the consultation
* Navigate to patient dashboard
* Open the current visit
* Verify details on visit page "Disposition" display control
* Navigate to dashboard
* Click on bed management app
* Verify patient "Sid ward" is present only in "Admit to Ward" queue

Admit Patient in Ward
---------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on bed management app
* Search patient "Sid ward" from "Admit to Ward" queue
* Verify patient details of "Sid ward" in queue
|Name           | Age   | Gender    |
|Sid ward Hasan   | 11	| M         |
* Click on "Admit To Ward" link
* Click on "Ward" button
* Navigate to "Ward 2nd floor"
* Assign an empty bed to the patient
* Navigate to patient ADT queues
Verify patient "Sid ward" is present only in "Admitted" queue

Verify Admit to Kahramana Patient flow through Disposition
----------------------------------------------------------
* Create patient "Sid kahramana" using API with "Hospital" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Search and select patient "Sid kahramana" from "Programs" queue
* Edit "Reconstructive Surgery" Program with following details
| programStatus |
| Surgical      |
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Disposition" tab
* Select "Admit to Kahramana" disposition with notes "Admit this patient to Kahramana"
* Save the consultation
* Navigate to patient dashboard
* Open the current visit
* Verify details on visit page "Disposition" display control
* Navigate to dashboard
* Click on bed management app
* Verify patient "Sid kahramana" is present only in "Admit to Kahramana" queue

Admit Patient in Kahramana
--------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on bed management app
* Search patient "Sid kahramana" from "Admit to Kahramana" queue
* Verify patient details of "Sid kahramana" in queue
|Name           | Age   | Gender    |
|Sid kahramana Hasan   | 11	| M         |
* Click on "Admit to Kahramana" link
* Click on "Kahramana" button
* Navigate to "Kahramana 1st floor"
* Assign an empty bed to the patient
* Navigate to patient ADT queues
Verify patient "Sid kahramana" is present only in "Admitted" queue