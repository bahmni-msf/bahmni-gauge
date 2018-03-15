Validation Committee Dashboard and Observation Forms
====================================================
Created by jaseena, swarup on 1/2/17

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

Verify the Validation Committee Dashboard display controls visibility
---------------------------------------------------------------------

tags: sanity, regression

* Create patient "MeeraOne" using API with "First Stage Validation" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_OPD_MO" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "MeeraOne" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Verify the dashboard name is "Validation Committee"
* Verify the following display controls are visible 

   |Display Control Title          |
   |-------------------------------|
   |Programs                       |
   |Edit forms                     |
   |Microbiology Results           |
   |Visits                         |
   |Patient Medical Documents (MLO)|

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

* Create patient "MeeraFirst" using API with "First Stage Validation" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_OPD_MO" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Search and select patient "MeeraFirst" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Patient History" from observation page and fill details 

   |FIELD                       |VALUE            |
   |----------------------------|-----------------|
   |Name of MLO                 |Dr. Wafa Al-Shawa|
   |Network Area                |Sana'a Network   |
   |Referred by                 |Local Doctor     |
   |Date of injury              |05/05/2016       |
   |Cause of injury             |Burns            |
   |Patient General Condition   |Walking Alone    |
   |If caretaker is needed, why?|Under 18 years   |

* Select template "First Stage Validation" from observation page and fill details 

   |FIELD                                                 |VALUE                              |
   |------------------------------------------------------|-----------------------------------|
   |Type of medical information received                  |New medical file                   |
   |Date Received                                         |07/07/2016                         |
   |Is the medical file complete?                         |Yes                                |
   |Document(s) needed to be complete                     |all complete                       |
   |Specialty                                             |Orthopedic                         |
   |Stage                                                 |2                                  |
   |Date of presentation                                  |10/10/2016                         |
   |Outcome for 1st stage surgical validation             |Valid                              |
   |Priority                                              |Low                                |
   |Name of Surgeon 1                                     |Dr. Rasheed Al Samerai             |
   |Name of Surgeon 2                                     |Dr. Hanna Janho                    |
   |Does the Patient need Surgical Final Validation?      |Yes                                |
   |Comments                                              |validation done                    |
   |Outcome for 1st stage Anaesthesia validation          |Need complementary investigation   |
   |Type of medical information needed for next submission|comments for Anaesthesia validation|

* Save the consultation
* Verify "First Stage Validation" is disabled to add
* Verify "Patient History" is disabled to add
* Navigate to patient dashboard
* Verify following details of "Medical History" in Patient Dashboard 

   |FIELD          |VALUE            |
   |---------------|-----------------|
   |Name of MLO    |Dr. Wafa Al-Shawa|
   |Network Area   |Sana'a Network   |
   |Date of injury |05 May 16        |
   |Cause of injury|Burns            |
   |Stage          |2                |
   |Specialty      |Orthopedic       |

* Verify following details of "First Stage Validation" in Patient Dashboard 

   |FIELD                                                 |VALUE                              |
   |------------------------------------------------------|-----------------------------------|
   |Type of medical information received                  |New medical file                   |
   |Date Received                                         |07 Jul 16                          |
   |Date of presentation                                  |10 Oct 16                          |
   |Outcome for 1st stage surgical validation             |Valid                              |
   |Priority                                              |Low                                |
   |Does the Patient need Surgical Final Validation?      |Yes                                |
   |Comments                                              |validation done                    |
   |Outcome for 1st stage Anaesthesia validation          |Need complementary investigation   |
   |Type of medical information needed for next submission|comments for Anaesthesia validation|

Final Validation form
---------------------
* Create patient "MeeraFinal" using API with "First Stage Validation" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_OPD_MO" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Search and select patient "MeeraFinal" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Final Validation" from observation page and fill details 

   |FIELD                               |VALUE                   |
   |------------------------------------|------------------------|
   |Date of Presentation                |05/05/2017              |
   |Outcome FV                          |Accepted                |
   |Comments on FV                      |FV comments             |
   |Does the Patient need Accommodation?|Yes                     |
   |Type of Admission Recommended       |Normal admission        |
   |Name of Surgeon 1                   |Dr. Ashraf Nabhan       |
   |Name of Surgeon 2                   |Dr.Ghassan S. Abu-Sittah|

* Save the consultation
* Verify "Final Validation" is disabled to add
* Navigate to patient dashboard
* Verify following details of "Final Validation" in Patient Dashboard 

   |FIELD                               |VALUE           |
   |------------------------------------|----------------|
   |Date of Presentation                |05 May 17       |
   |Outcome FV                          |Accepted        |
   |Comments on FV                      |FV comments     |
   |Does the Patient need Accommodation?|Yes             |
   |Type of Admission Recommended       |Normal admission|


Follow up Validation and Medical History Forms
----------------------------------------------

* Create patient "MeeraFollowup" using API with "First Stage Validation" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_OPD_MO" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Search and select patient "MeeraFollowup" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Patient History" from observation page and fill details 

   |FIELD                       |VALUE            |
   |----------------------------|-----------------|
   |Name of MLO                 |Dr. Wafa Al-Shawa|
   |Network Area                |Sana'a Network   |
   |Referred by                 |Local Doctor     |
   |Date of injury              |05/05/2016       |
   |Cause of injury             |Burns            |
   |Patient General Condition   |Walking Alone    |
   |If caretaker is needed, why?|Under 18 years   |

* Select template "First Stage Validation" from observation page and fill details 

   |FIELD    |VALUE  |
   |---------|-------|
   |Specialty|Plastic|

* Select template "Follow-up Validation" from observation page and fill details 

   |FIELD                                           |VALUE                           |
   |------------------------------------------------|--------------------------------|
   |Date of presentation                            |07/07/2016                      |
   |Qualitative outcome-Union                       |Non united                      |
   |Qualitative outcome - Infection                 |Pin tract infection             |
   |Qualitative outcome - SMFA                      |Done                            |
   |Outcome for follow-up surgical validation       |Further stage admission         |
   |Reason for further stage admission              |Complementary surgery           |
   |Stage                                           |3                               |
   |Priority                                        |Moderate                        |
   |Name of Surgeon 1                               |Dr. Rasheed Al Samerai          |
   |Name of Surgeon 2                               |Dr. Ashraf Nabhan               |
   |Does the Patient need Surgical Final Validation?|Yes                             |
   |Comments about further stage admission          |further stage admission comments|

* Save the consultation
* Verify "Patient History" is disabled to add
* Verify "First Stage Validation" is disabled to add
* Verify "Follow-up Validation" is disabled to add
* Navigate to patient dashboard
* Verify following details of "Followup Validation" in Patient Dashboard 

   |FIELD                                           |VALUE                  |
   |------------------------------------------------|-----------------------|
   |Date of presentation                            |07 Jul 16              |
   |Outcome for follow-up surgical validation       |Further stage admission|
   |Reason for further stage admission              |Complementary surgery  |
   |Priority                                        |Moderate               |
   |Name of Surgeon 1                               |Dr. Rasheed Al Samerai |
   |Name of Surgeon 2                               |Dr. Ashraf Nabhan      |
   |Does the Patient need Surgical Final Validation?|Yes                    |

* Verify following details of "Medical History" in Patient Dashboard 

   |FIELD          |VALUE            |
   |---------------|-----------------|
   |Name of MLO    |Dr. Wafa Al-Shawa|
   |Network Area   |Sana'a Network   |
   |Date of injury |05 May 16        |
   |Cause of injury|Burns            |
   |Stage          |3                |
   |Specialty      |Plastic          |
