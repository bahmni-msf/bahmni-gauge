Patient Validation Scenarios
============================
Created by swarup on 9/17/16

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
     
First Stage Validation
---------------------
Tags: regression

* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on registration app
* Click on create new patient link
* Enter Patient Details
| firstName | lastName | givenNameArabic | familyNameArabic | gender | age | governorate | country | phoneNumber1 | spokenLanguages | nationality1 |
| Gaman     | Sayed    | أل              | حسن              | Male   | 12  | Amman       | Jordan  | +9898989898  | English         | Egyptian     |
* Start "First Stage Validation" visit and navigate to Programs page
* Register the patient to following program
| name                   | dateOfRegistration | programStatus  |
| Reconstructive Surgery | 01/01/2016         | Identification |
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Medical History" from observation page and fill details
| FIELD                        | VALUE          |
| Name of MLO                  | Dr. Feras Nasr |
| Referred by                  | adsadasdsad    |
| Network Area                 | Sana'a Network |
| Date of injury               | 01/01/2016     |
| Cause of injury              | Burns          |
| If caretaker is needed, why? | Under 18 years |

* Select template "First Stage Validation" from observation page and fill details
| FIELD                                     | VALUE      |
| Is the medical file complete?             | Yes        |
| Specialty                                 | Orthopedic |
| Outcome for 1st stage surgical validation | Valid      |
| Priority                                  | Low        |
* Save the consultation


Follow up Validation
---------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Search and select patient "Gaman Sayed" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Follow-up Validation" from observation page and fill details
| FIELD                                     | VALUE      |
| Date of presentation                      | 07/07/2016 |
| Stage                                     | 2          |
| Outcome for follow-up surgical validation | MBA        |
* Save the consultation


Verify Display Controls on dashboard
---------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Search and select patient "Gaman Sayed" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Verify following details of "Medical History" in Patient Dashboard
| FIELD           | VALUE          |
| Name of MLO     | Dr. Feras Nasr |
| Network Area    | Sana'a Network |
| Date of injury  | 01 Jan 16      |
| Cause of injury | Burns          |
| Stage           | 2              |
| Stage           | 2              |
| Specialty       | Orthopedic     |
* Verify following details of "First Stage Validation" in Patient Dashboard
| FIELD                                     | VALUE     |
| Date of presentation                      | 07 Jul 16 |
| Outcome for 1st stage surgical validation | Valid     |
| Priority                                  | Low       |
* Verify following details of "Followup Validation" in Patient Dashboard
| FIELD                                     | VALUE     |
| Date of presentation                      | 07 Jul 16 |
| Outcome for follow-up surgical validation | MBA       |
