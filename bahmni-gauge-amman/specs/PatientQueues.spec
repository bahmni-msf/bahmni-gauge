Patient Queues Scenarios
========================
Created by swarup, jaseena, kaustav on 10/24/16

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.


Create Patient and Verify Programs Queue
----------------------------------------
* On the login page
* Login with user "weaam_a" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on registration app
* Click on create new patient link
* Enter Patient Details 

     |firstName|lastName|givenNameArabic|familyNameArabic|gender|age|governorate|country|phoneNumber1|spokenLanguages|nationality1|isCareTakerRequiredCheckBox|statusofOfficialIDdocuments|caretakerNameEnglish|caretakerGender|caretakerNationality|legalRepalsoCaretaker|
     |---------|--------|---------------|----------------|------|---|-----------|-------|------------|---------------|------------|---------------------------|---------------------------|--------------------|---------------|--------------------|---------------------|
     |Abdulla  |Yonus   |عبدالله |حسن          |Male  |30 |Amman      |Jordan |+9898989898 |English        |Egyptian    |True                       |Waiting                    |Nadira              |Female         |Iraqi               |Yes                  |

* Start "First Stage Validation" visit and navigate to Programs page
* Enroll patient to the following program 

     |name                  |dateOfRegistration|programStatus |
     |----------------------|------------------|--------------|
     |Reconstructive Surgery|09/09/2016        |Identification|

* Navigate to queues
* Search patient "Abdulla Yonus" from "Programs" queue
* Verify patient details of "Abdulla Yonus" in queue 

     |Name         |
     |-------------|
     |Abdulla Yonus|

* Search patient "Abdulla Yonus" from "Awaiting Validation - 1st Stage" queue
* Verify patient details of "Abdulla Yonus" in queue 

     |Name         |Nationality|
     |-------------|-----------|
     |Abdulla Yonus|Egyptian   |

Patient In Medical File incomplete queue
----------------------------------------
* On the login page
* Login with user "ajeeb_am" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Abdulla Yonus" from "Awaiting Validation - 1st Stage" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Medical History" from observation page and fill details 

     |FIELD                       |VALUE                |
     |----------------------------|---------------------|
     |Name of MLO                 |Dr. Feras Nasr       |
     |Network Area                |Sana'a Network       |
     |Referred by                 |Ameer                |
     |Date of injury              |08/28/2016           |
     |Cause of injury             |Burns                |
     |Patient General Condition   |Walking Alone        |
     |If caretaker is needed, why?|Functional disability|

* Select template "First Stage Validation" from observation page and fill details 

     |FIELD                               |VALUE           |
     |------------------------------------|----------------|
     |Type of medical information received|New medical file|
     |Date Received                       |09/28/2016      |
     |Is the medical file complete?       |No              |
     |Document(s) needed to be complete   |Sample          |
     |Specialty                           |Orthopedic      |
     |Stage                               |2               |

* Save the consultation
* Navigate to queues
* Search patient "Abdulla Yonus" from "Incomplete Medical File" queue
* Verify patient details of "Abdulla Yonus" in queue 

     |Date Of File Received|Name         |Name Of MLO   |Documents Needed To Be Complete|
     |---------------------|-------------|--------------|-------------------------------|
     |28/09/2016           |Abdulla Yonus|Dr. Feras Nasr|Sample                         |


Patient In Awaiting 1st stage validation queue
----------------------------------------------
* On the login page
* Login with user "mahmoud_h" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Search and select patient "Abdulla Yonus" from "Incomplete Medical File" queue
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
* Search patient "Abdulla Yonus" from "Awaiting Validation - 1st Stage " queue
* Verify patient details of "Abdulla Yonus" in queue 

     |Date Of File Received|Name         |Name Of MLO   |Nationality|Specialty |
     |---------------------|-------------|--------------|-----------|----------|
     |10/10/2016           |Abdulla Yonus|Dr. Feras Nasr|Egyptian   |Orthopedic|


Patient In MoreInformation/ Postponed queue when FSTG Outcome is Postponed
--------------------------------------------------------------------------
* On the login page
* Login with user "nabil_j" and password "BAHMNI_GAUGE_VC_MEMBER_PASSWORD" with location "BAHMNI_GAUGE_VC_MEMBER_LOCATION"
* Click on programs app
* Search and select patient "Abdulla Yonus" from "Awaiting Validation - 1st Stage" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "First Stage Validation" from observation page and fill details 

     |FIELD                                    |VALUE                  |
     |-----------------------------------------|-----------------------|
     |Date of presentation                     |10/09/2016             |
     |Outcome for 1st stage surgical validation|Postponed              |
     |Postpone Reason                          |P2: Waiting for healing|
     |Comments about postpone reason           |postponed for a month  |

* Save the consultation
* Navigate to queues
* Search patient "Abdulla Yonus" from "More Information / Postponed" queue
* Verify patient details of "Abdulla Yonus" in queue 

     |Date Of Presentation|Name         |Nationality|Name Of MLO   |Specialty |Outcomes For 1st Stage Surgical Validation|Postpone Reason        |Comments About Postpone Reason|
     |--------------------|-------------|-----------|--------------|----------|------------------------------------------|-----------------------|------------------------------|
     |09/10/2016          |Abdulla Yonus|Egyptian   |Dr. Feras Nasr|Orthopedic|Postponed                                 |P2: Waiting for healing|postponed for a month         |

Wait for the scheduler to run and close the visit
* Search and select patient "Abdulla Yonus" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Verify Consultation button is not present

Patient In MoreInformation/ Postponed queue when FSTG Outcome is More Information
---------------------------------------------------------------------------------
* On the login page
* Login with user "weaam_a" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on registration app
* Search patient with name "Abdulla Yonus"
* Select the patient from the search results
* Start "First Stage Validation" visit and navigate to Programs page
* On the login page
* Login with user "nabil_j" and password "BAHMNI_GAUGE_VC_MEMBER_PASSWORD" with location "BAHMNI_GAUGE_VC_MEMBER_LOCATION"
* Click on programs app
* Search and select patient "Abdulla Yonus" from "Awaiting Validation - 1st Stage" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "First Stage Validation" from observation page and fill details 

     |FIELD                                                 |VALUE            |
     |------------------------------------------------------|-----------------|
     |Date of presentation                                  |10/09/2016       |
     |Outcome for 1st stage surgical validation             |More Information |
     |Type of medical information needed for next submission|more medical info|

* Save the consultation
* Navigate to queues
* Search patient "Abdulla Yonus" from "More Information / Postponed " queue
* Verify patient details of "Abdulla Yonus" in queue 

     |Date Of Presentation|Name         |Nationality|Name Of MLO   |Specialty |Outcomes For 1st Stage Surgical Validation|Type Of Medical Information Needed For Next Submission|
     |--------------------|-------------|-----------|--------------|----------|------------------------------------------|------------------------------------------------------|
     |09/10/2016          |Abdulla Yonus|Egyptian   |Dr. Feras Nasr|Orthopedic|More Information                          |more medical info                                     |

Wait for the scheduler to run and close the visit
* Search and select patient "Abdulla Yonus" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Verify Consultation button is not present

Patient in Validated Patients queue - FSTG
------------------------------------------
* On the login page
* Login with user "weaam_a" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on registration app
* Search patient with name "Abdulla Yonus"
* Select the patient from the search results
* Start "First Stage Validation" visit and navigate to Programs page
* On the login page
* Login with user "hani_i" and password "BAHMNI_GAUGE_VC_MEMBER_PASSWORD" with location "BAHMNI_GAUGE_VC_MEMBER_LOCATION"
* Click on programs app
* Search and select patient "Abdulla Yonus" from "Awaiting Validation - 1st Stage" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "First Stage Validation" from observation page and fill details 

     |FIELD                                                 |VALUE                    |
     |------------------------------------------------------|-------------------------|
     |Type of medical information received                  |Updated Medical file     |
     |Date Received                                         |04/01/2016               |
     |Is the medical file complete?                         |Yes                      |
     |Document(s) needed to be complete                     |all completed            |
     |Specialty                                             |Orthopedic               |
     |Stage                                                 |2                        |
     |Date of presentation                                  |10/08/2016               |
     |Outcome for 1st stage surgical validation             |Valid                    |
     |Priority                                              |Low                      |
     |Name of Surgeon 1                                     |Dr. Rasheed Al Samerai   |
     |Name of Surgeon 2                                     |Dr. Sofian Al-Qassab     |
     |Does the Patient need Surgical Final Validation?      |Yes                      |
     |Comments                                              |validation done          |
     |Outcome for 1st stage Anaesthesia validation          |Fits anaesthesia criteria|
     |Name of Anaesthetist                                  |Dr. Hadeel Al-Ani        |
     |Type of medical information needed for next submission|up to date               |

* Save the consultation
* Navigate to queues
* Search patient "Abdulla Yonus" from "Validated Patients" queue
* Verify patient details of "Abdulla Yonus" in queue 

     |Date Of Presentation|Name         |Age|Country|Name Of MLO   |Stage|Specialty |Priority|Comments About Validation|Does The Patient Need Surgical Final Validation|Is Caretaker Required?|Status Of Official ID Documents|
     |--------------------|-------------|---|-------|--------------|-----|----------|--------|-------------------------|-----------------------------------------------|----------------------|-------------------------------|
     |08/10/2016          |Abdulla Yonus|30 |Jordan |Dr. Feras Nasr|2    |Orthopedic|Low     |validation done          |Yes                                            |Yes                   |Waiting                        |

Patient In Expected arrival queue
---------------------------------
* On the login page
* Login with user "mahmoud_h" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on registration app
* Search patient with name "Abdulla Yonus"
* Select the patient from the search results
* Enter Patient Details 

     |expectedDateofArrival|
     |---------------------|
     |06/01/2017           |

* Save Patient
* Go to Home Page
* Click on programs app
* Search patient "Abdulla Yonus" from "Expected Arrival" queue
* Verify patient details of "Abdulla Yonus" in queue 

     |Name         |Age|Country|Specialty |Stage|Priority|Comments About Validation|Expected Date Of Arrival|Patient General Condition|Is Caretaker Required?|Caretaker Gender|Caretaker Name|
     |-------------|---|-------|----------|-----|--------|-------------------------|------------------------|-------------------------|----------------------|----------------|--------------|
     |Abdulla Yonus|30 |Jordan |Orthopedic|2    |Low     |validation done          |01/06/2017              |Walking Alone            |Yes                   |Female          |Nadira        |


Patient In Hospital RSP queue
-----------------------------
* On the login page
* Login with user "mahmoud_h" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on registration app
* Search patient with name "Abdulla Yonus"
* Select the patient from the search results
* Enter Patient Details 

     |dateofArrival|
     |-------------|
     |05/23/2017   |
* Start "Hospital" visit and navigate to Programs page
* Edit "Reconstructive Surgery" Program with following details 

     |programStatus|
     |-------------|
     |Pre-Operative|

* Navigate to queues
* Search patient "Abdulla Yonus" from "Hospital RSP" queue
* Verify patient details of "Abdulla Yonus" in queue 

     |Date Of Arrival|Name         |Age|Country|Is Caretaker Required?|Specialty |Stage|Phase Of Treatment|
     |---------------|-------------|---|-------|----------------------|----------|-----|------------------|
     |23/05/2017     |Abdulla Yonus|30 |Jordan |Yes                   |Orthopedic|2    |Pre-Operative     |

* Search and select patient "Abdulla Yonus" from "Programs" queue
* Edit "Reconstructive Surgery" Program with following details 

     |programStatus    |
     |-----------------|
     |Network Follow-up|

* Navigate to queues
* Verify patient "Abdulla Yonus" is not present in any queue except Programs and All queues

Patient In Awaiting Follow up validation queue
----------------------------------------------
* On the login page
* Login with user "mahmoud_h" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on registration app
* Search patient with name "Abdulla Yonus"
* Select the patient from the search results
* Start "Follow-Up Validation" visit and navigate to Programs page
* On the login page
* Login with user "hani_i" and password "BAHMNI_GAUGE_VC_MEMBER_PASSWORD" with location "BAHMNI_GAUGE_VC_MEMBER_LOCATION"
* Click on programs app
* Search patient "Abdulla Yonus" from "Awaiting Validation - Follow Up Stage" queue
* Verify patient details of "Abdulla Yonus" in queue 

     |Name         |Name Of MLO   |Nationality|Specialty |
     |-------------|--------------|-----------|----------|
     |Abdulla Yonus|Dr. Feras Nasr|Egyptian   |Orthopedic|



Patient In Continue Follow up validation queue
----------------------------------------------
* On the login page
* Login with user "mahmoud_h" and password "BAHMNI_GAUGE_VC_MEMBER_PASSWORD" with location "BAHMNI_GAUGE_VC_MEMBER_LOCATION"
* Click on programs app
* Search and select patient "Abdulla Yonus" from "Awaiting Validation - Follow Up Stage" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Follow-up Validation" from observation page and fill details 

     |FIELD                                     |VALUE                   |
     |------------------------------------------|------------------------|
     |Date of presentation                      |10/10/2016              |
     |Outcome for follow-up surgical validation |Continue under follow-up|
     |Time for next medical follow-up to be done|1 month                 |
     |Comments about next follow-up             |Followup After 1 month  |

* Save the consultation
* Navigate to queues
* Search patient "Abdulla Yonus" from "To Continue Under Follow-Up " queue
* Verify patient details of "Abdulla Yonus" in queue 

     |Date Of Presentation|Name         |Time For Next Medical Follow-up|Comments              |
     |--------------------|-------------|-------------------------------|----------------------|
     |10/10/2016          |Abdulla Yonus|1 month                        |Followup After 1 month|

Patient in Validated Patients queue - FUP
-----------------------------------------
* On the login page
* Login with user "weaam_a" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on registration app
* Click on create new patient link
* Enter Patient Details 

     |firstName|lastName|givenNameArabic|familyNameArabic|gender|age|governorate|country|phoneNumber1|spokenLanguages|nationality1|isCareTakerRequiredCheckBox|statusofOfficialIDdocuments|caretakerNameEnglish|caretakerGender|caretakerNationality|legalRepalsoCaretaker|
     |---------|--------|---------------|----------------|------|---|-----------|-------|------------|---------------|------------|---------------------------|---------------------------|--------------------|---------------|--------------------|---------------------|
     |Abdul    |Bari    |عبدالله        |حسن             |Male  |30 |Amman      |Jordan |+9898989898 |English        |Egyptian    |True                       |Waiting                    |Nadira              |Female         |Iraqi               |Yes                  |

* Start "Follow-Up Validation" visit and navigate to Programs page
* Enroll patient to the following program 

     |name                  |dateOfRegistration|programStatus    |
     |----------------------|------------------|-----------------|
     |Reconstructive Surgery|09/09/2016        |Network Follow-up|

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
* Navigate to queues
* Search patient "Abdul Bari" from "Validated Patients" queue
* Verify patient details of "Abdul Bari" in queue 

     |Date Of Presentation|Name      |Age|Country|Stage|Priority|Comments About Validation       |Does The Patient Need Surgical Final Validation|Is Caretaker Required?|Status Of Official ID Documents|
     |--------------------|----------|---|-------|-----|--------|--------------------------------|-----------------------------------------------|----------------------|-------------------------------|
     |05/07/2016          |Abdul Bari|30 |Jordan |3    |Moderate|further stage admission comments|Yes                                            |Yes                   |Waiting                        |
