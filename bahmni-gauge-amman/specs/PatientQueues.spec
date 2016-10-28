Patient Queues
=====================
Created by swarup on 10/24/16

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
     
Create Patient and Verify Programs Queue
-----------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on registration app
* Click on create new patient link
* Enter Patient Details
| firstName | lastName | givenNameArabic | familyNameArabic | gender | age | governorate | country | phoneNumber1 | spokenLanguages | nationality1 | expectedDateofArrival |
| Al Madasd | Hassan   | أل              | حسن              | Male   | 12  | Amman       | Jordan  | +9898989898  | English         | Egyptian     | r 11-11-2016          |
* Start "Follow-Up Validation" visit and navigate to Programs page
* Register the patient to following program
| name                   | dateOfRegistration | programStatus  |
| Reconstructive Surgery | 01/01/2016         | Identification |
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search patient "Al Madasd Hassan" from "Programs" queue
* Verify patient details in queue
| Name             |
| Al Madasd Hassan |

Patient In Medical File incomplete queue
----------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Al Madasd Hassan" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Medical History" from observation page and fill details
| FIELD           | VALUE          |
| Name of MLO     | Dr. Feras Nasr |
| Network Area    | Sana'a Network |
| Referred by     | adsadasdsad    |
| Date of injury  | 01/01/2016     |
| Cause of injury | Burns          |
* Select template "First Stage Validation" from observation page and fill details
| FIELD                             | VALUE      |
| Date Received                     | 10/10/2016 |
| Is the medical file complete?     | No         |
| Document(s) needed to be complete | Sample     |
| Specialty                         | Orthopedic |
| Stage                             | 1          |
* Save the consultation
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search patient "Al Madasd Hassan" from "Incomplete Medical File" queue
* Verify patient details in queue
| Date Of File Received | Name             | Name Of MLO    | Documents Needed To Be Complete |
| 10/10/2016            | Al Madasd Hassan | Dr. Feras Nasr | Sample                          |


Patient In Awaiting 1st stage validation queue
----------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Al Madasd Hassan" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "First Stage Validation" from observation page and fill details
| FIELD                         | VALUE      |
| Date Received                 | 10/10/2016 |
| Is the medical file complete? | Yes        |
* Save the consultation
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search patient "Al Madasd Hassan" from "Awaiting Validation - 1st Stage " queue
* Verify patient details in queue
| Date Of File Received | Name             | Name Of MLO    | Nationality | Specialty  |
| 10/10/2016            | Al Madasd Hassan | Dr. Feras Nasr | Egyptian    | Orthopedic |



Patient In MoreInformation/ Postponed queue
----------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Al Madasd Hassan" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "First Stage Validation" from observation page and fill details
| FIELD                                     | VALUE                   |
| Date of presentation                      | 11/11/2016              |
| Outcome for 1st stage surgical validation | Postponed               |
| Postpone Reason                           | P2: Waiting for healing |
* Save the consultation
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search patient "Al Madasd Hassan" from "More Information / Postponed " queue
* Verify patient details in queue
| Date Of Presentation | Name             | Outcomes For 1st Stage Surgical Validation | Postponed Reason        |
| 11/11/2016           | Al Madasd Hassan | Postponed                                  | P2: Waiting for healing |



Patient In Awaiting Follow up validation queue
----------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Al Madasd Hassan" from "Programs" queue
* Edit created Program with following details
| programStatus     |
| Network follow-up |
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search patient "Al Madasd Hassan" from "Awaiting Validation - 1st Stage " queue
* Verify patient details in queue
| Name             | Name Of MLO    | Nationality | Specialty  |
| Al Madasd Hassan | Dr. Feras Nasr | Egyptian    | Orthopedic |



Patient In Continue Follow up validation queue
----------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Al Madasd Hassan" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Follow-Up Validation" from observation page and fill details
| FIELD                                      | VALUE                    |
| Date of presentation                       | 12/12/2016               |
| Outcome for follow-up surgical validation  | Continue under follow-up |
| Time for next medical follow-up to be done | 1 month                  |
| Comments about next follow-up              | Followup After 1 month   |
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search patient "Al Madasd Hassan" from "Awaiting Validation - 1st Stage " queue
* Verify patient details in queue
| Name             | Time For Next Medical Follow-up | Comments               |
| Al Madasd Hassan | 1 month                         | Followup After 1 month |


Patient In Expected arrival queue
---------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Final Validation" from observation page and fill details
| FIELD                                     | VALUE                    |
| Does the Patient need Accommodation?      | Yes                      |
| Outcome for follow-up surgical validation | Continue under follow-up |
| Type of Admission Recommended             | Normal admission         |
* Search and select patient "Al Madasd Hassan" from "Expected Arrival" queue
* Verify patient details in queue
| Name             | Country | Expected Date Of Arrival | Does The Patient Need Accommodation? | Type of Admission Recommended |
| Al Madasd Hassan | Jordan  | 11/11/2016               | Yes                                  | Normal Admission              |


