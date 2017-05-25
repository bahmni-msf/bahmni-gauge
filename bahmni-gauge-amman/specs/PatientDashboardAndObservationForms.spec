Patient Dashboard and Observation Forms
=======================================
Created by jaseena, swarup on 1/2/17

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

Verify the Patient Dashboard display controls visibility
--------------------------------------------------------
* Create patient "Safa" using API with "First Stage Validation" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Safa" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Verify the following display controls are visible 

     |Display Control Title      |
     |---------------------------|
     |Programs                   |
     |Edit forms                 |
     |Visits                     |
     |Patient Medical Documents  |
     |Patient Encounter Locations|

* Verify the following display controls are hidden 

     |Display Control Title |
     |----------------------|
     |Medical History       |
     |First Stage Validation|
     |Followup Validation   |
     |Final Validation      |

First Stage Validation and Medical History Forms
------------------------------------------------
tags: regression
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Search and select patient "Safa" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Medical History" from observation page and fill details 

     |FIELD                       |VALUE            |
     |----------------------------|-----------------|
     |Name of MLO                 |Dr. Wafa Al-Shawa|
     |Referred by                 |Local Doctor     |
     |Network Area                |Sana'a Network   |
     |Date of injury              |01/05/2016       |
     |Cause of injury             |Burns            |
     |Patient General Condition   |Walking Alone    |
     |If caretaker is needed, why?|Under 18 years   |

* Select template "First Stage Validation" from observation page and fill details 

     |FIELD                                                 |VALUE                    |
     |------------------------------------------------------|-------------------------|
     |Type of medical information received                  |New medical file         |
     |Date Received                                         |01 May 17                |
     |Is the medical file complete?                         |Yes                      |
     |Document(s) needed to be complete                     |all complete             |
     |Specialty                                             |Orthopedic               |
     |Stage                                                 |2                        |
     |Date of presentation                                  |10/25/2016               |
     |Outcome for 1st stage surgical validation             |Valid                    |
     |Priority                                              |Low                      |
     |Name of Surgeon 1                                     |Dr. Sofian Al-Qassab     |
     |Name of Surgeon 2                                     |Dr. Rasheed Al Samerai   |
     |Does the Patient need Surgical Final Validation?      |Yes                      |
     |Comments                                              |FSTG comments            |
     |Outcome for 1st stage Anaesthesia validation          |Fits anaesthesia criteria|
     |Name of Anaesthetist                                  |Dr. Hadeel Al-Ani        |
     |Type of medical information needed for next submission|all complete             |

* Save the consultation
* Navigate to patient dashboard
* Verify following details of "Medical History" in Patient Dashboard 

     |FIELD          |VALUE            |
     |---------------|-----------------|
     |Name of MLO    |Dr. Wafa Al-Shawa|
     |Network Area   |Sana'a Network   |
     |Date of injury |05 Jan 16        |
     |Cause of injury|Burns            |
     |Stage          |2                |
     |Specialty      |Orthopedic       |

* Verify following details of "First Stage Validation" in Patient Dashboard 

     |FIELD                                                 |VALUE                    |
     |------------------------------------------------------|-------------------------|
     |Type of medical information received                  |New medical file         |
     |Date of presentation                                  |25 Oct 16                |
     |Outcome for 1st stage surgical validation             |Valid                    |
     |Priority                                              |Low                      |
     |Does the Patient need Surgical Final Validation?      |Yes                      |
     |Comments                                              |FSTG comments            |
     |Outcome for 1st stage Anaesthesia validation          |Fits anaesthesia criteria|
     |Type of medical information needed for next submission|all complete             |

Final Validation form
---------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on registration app
* Search patient with name "Safa"
* Select the patient from the search results
* Start "First Stage Validation" visit and navigate to Programs page
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Final Validation" from observation page and fill details 

     |FIELD                               |VALUE                   |
     |------------------------------------|------------------------|
     |Date of Presentation                |05/01/2017              |
     |Outcome FV                          |Accepted                |
     |Comments on FV                      |FV comments             |
     |Does the Patient need Accommodation?|Yes                     |
     |Type of Admission Recommended       |Normal admission        |
     |Name of Surgeon 1                   |Dr. Ashraf Nabhan       |
     |Name of Surgeon 2                   |Dr.Ghassan S. Abu-Sittah|

* Save the consultation
* Navigate to patient dashboard
* Verify following details of "Final Validation" in Patient Dashboard 

     |FIELD                               |VALUE           |
     |------------------------------------|----------------|
     |Date of Presentation                |01 May 17       |
     |Outcome FV                          |Accepted        |
     |Comments on FV                      |FV comments     |
     |Does the Patient need Accommodation?|Yes             |
     |Type of Admission Recommended       |Normal admission|


Follow up Validation and Medical History Forms
----------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on registration app
* Search patient with name "Safa"
* Select the patient from the search results
* Start "Follow-Up Validation" visit and navigate to Programs page
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Follow-up Validation" from observation page and fill details 

     |FIELD                                           |VALUE                           |
     |------------------------------------------------|--------------------------------|
     |Qualitative outcome-Union                       |Non united                      |
     |Qualitative outcome - Infection                 |Pin tract infection             |
     |Qualitative outcome - SMFA                      |Done                            |
     |Date of presentation                            |07/05/2016                      |
     |Outcome for follow-up surgical validation       |Further stage admission         |
     |Reason for further stage admission              |Complementary surgery           |
     |Stage                                           |3                               |
     |Priority                                        |Moderate                        |
     |Name of Surgeon 1                               |Dr. Rasheed Al Samerai          |
     |Name of Surgeon 2                               |Dr. Ashraf Nabhan               |
     |Does the Patient need Surgical Final Validation?|Yes                             |
     |Comments about further stage admission          |further stage admission comments|

* Save the consultation
* Navigate to patient dashboard
* Verify following details of "Followup Validation" in Patient Dashboard 

     |FIELD                                           |VALUE                  |
     |------------------------------------------------|-----------------------|
     |Date of presentation                            |05 Jul 16            |
     |Outcome for follow-up surgical validation       |Further stage admission|
     |Reason for further stage admission              |Complementary surgery  |
     |Priority                                        |Moderate               |
     |Name of Surgeon 1                               |Dr. Rasheed Al Samerai |
     |Name of Surgeon 2                               |Dr. Ashraf Nabhan      |
     |Does the Patient need Surgical Final Validation?|Yes                    |

* Verify following details of "Medical History" in Patient Dashboard 

     |FIELD          |VALUE            |
     |---------------|-----------------|
     |Stage          |3                |
     |Name of MLO    |Dr. Wafa Al-Shawa|
     |Network Area   |Sana'a Network   |
     |Date of injury |05 Jul 16        |
     |Cause of injury|Burns            |
     |Specialty      |Orthopedic       |
