Patient Validation Scenarios
============================
Created by swarup on 9/17/16

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
     
First Stage Validation
---------------------
Tags: regression
* Create patient "Gamansayed" using API with "First Stage Validation" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Search and select patient "Gamansayed" from "Programs" queue
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
* Search and select patient "Gamansayed" from "Programs" queue
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
* Search and select patient "Gamansayed" from "Programs" queue
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
