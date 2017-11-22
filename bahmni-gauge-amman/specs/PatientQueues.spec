Patient Queues Scenarios
========================
Created by swarup, jaseena, kaustav on 10/24/16

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.


1. Create Patient and Verify Programs Queue. 2. Verify Patient In Awaiting 1st stage validation queue. 3. Patient In Postponed queue when FSTG Outcome is Postponed
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
// Create Patient and Verify Programs Queue.
* On the login page
* Login with user "weaam_a" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on registration app
* Click on create new patient link
* Enter Patient Details 

   |firstName|lastName|givenNameArabic|familyNameArabic|gender|age|governorate|country|phoneNumber1|spokenLanguages|nationality1|isCareTakerRequiredCheckBox|statusofOfficialIDdocuments|caretakerNameEnglish|caretakerGender|caretakerNationality|legalRepalsoCaretaker|
   |---------|--------|---------------|----------------|------|---|-----------|-------|------------|---------------|------------|---------------------------|---------------------------|--------------------|---------------|--------------------|---------------------|
   |Abdulla  |Yonus   |عبدالله        |حسن             |Male  |30 |Amman      |Jordan |+9898989898 |English        |Egyptian    |True                       |Waiting                    |Nadira              |Female         |Iraqi               |Yes                  |

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

// Patient In Awaiting 1st stage validation queue
* Search and select patient "Abdulla Yonus" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Patient History" from observation page and fill details 

   |FIELD                       |VALUE                |
   |----------------------------|---------------------|
   |Name of MLO                 |Dr. Feras Nasr       |
   |Network Area                |Sana'a Network       |
   |Referred by                 |Ameer                |
   |Date of injury              |08/08/2016           |
   |Cause of injury             |Burns                |
   |Patient General Condition   |Walking Alone        |
   |If caretaker is needed, why?|Functional disability|

* Select template "First Stage Validation" from observation page and fill details 

   |FIELD                               |VALUE           |
   |------------------------------------|----------------|
   |Type of medical information received|New medical file|
   |Date Received                       |10/10/2016      |
   |Is the medical file complete?       |Yes             |
   |Specialty                           |Orthopedic      |
   |Stage                               |2               |

* Save the consultation
* Navigate to queues
* Search patient "Abdulla Yonus" from "Awaiting Validation - 1st Stage " queue
* Verify patient details of "Abdulla Yonus" in queue 

   |Date Of File Received|Name         |Name Of MLO   |Nationality|Specialty |
   |---------------------|-------------|--------------|-----------|----------|
   |10/10/2016           |Abdulla Yonus|Dr. Feras Nasr|Egyptian   |Orthopedic|


// Patient In Postponed queue when FSTG Outcome is Postponed
* Search and select patient "Abdulla Yonus" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "First Stage Validation" from observation page and fill details 

   |FIELD                                    |VALUE                  |
   |-----------------------------------------|-----------------------|
   |Date of presentation                     |10/10/2016             |
   |Outcome for 1st stage surgical validation|Postponed              |
   |Postpone Reason                          |P2: Waiting for healing|
   |Comments about postpone reason           |postponed for a month  |
   |Medical file to be submitted again by    |01/01/2018             |

* Save the consultation
* Navigate to queues
* Search patient "Abdulla Yonus" from "Postponed" queue
* Verify patient details of "Abdulla Yonus" in queue 

   |Date Of Presentation|Name         |Nationality|Name Of MLO   |Specialty |Outcomes For 1st Stage Surgical Validation|Postpone Reason        |Comments About Postpone Reason|Medical File To Be Submitted Again By|
   |--------------------|-------------|-----------|--------------|----------|------------------------------------------|-----------------------|------------------------------|-------------------------------------|
   |10/10/2016          |Abdulla Yonus|Egyptian   |Dr. Feras Nasr|Orthopedic|Postponed                                 |P2: Waiting for healing|postponed for a month         |01/01/2018                           |

* Wait for the scheduler to run and close the visit
* Search and select patient "Abdulla Yonus" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Verify Consultation button is not present

Patient In More Information queue when FSTG Outcome is More Information
-----------------------------------------------------------------------
* On the login page
* Login with user "weaam_a" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on registration app
* Click on create new patient link
* Enter Patient Details 

   |firstName|lastName|givenNameArabic|familyNameArabic|gender|age|governorate|country|phoneNumber1|spokenLanguages|nationality1|isCareTakerRequiredCheckBox|statusofOfficialIDdocuments|caretakerNameEnglish|caretakerGender|caretakerNationality|legalRepalsoCaretaker|
   |---------|--------|---------------|----------------|------|---|-----------|-------|------------|---------------|------------|---------------------------|---------------------------|--------------------|---------------|--------------------|---------------------|
   |Ameer    |Yonus   |عبدالله        |حسن             |Male  |30 |Amman      |Jordan |+9898989898 |English        |Egyptian    |True                       |Waiting                    |Nadira              |Female         |Iraqi               |Yes                  |

* Start "First Stage Validation" visit and navigate to Programs page
* Enroll patient to the following program 

   |name                  |dateOfRegistration|programStatus |
   |----------------------|------------------|--------------|
   |Reconstructive Surgery|09/09/2016        |Identification|

* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Patient History" from observation page and fill details 

   |FIELD      |VALUE         |
   |-----------|--------------|
   |Name of MLO|Dr. Feras Nasr|

* Select template "First Stage Validation" from observation page and fill details 

   |FIELD                                                 |VALUE                           |
   |------------------------------------------------------|--------------------------------|
   |Specialty                                             |Plastic                         |
   |Date of presentation                                  |10/10/2016                      |
   |Outcome for 1st stage surgical validation             |More Information                |
   |Type of medical information needed for next submission|more medical info               |
   |Outcome for 1st stage Anaesthesia validation          |Need complementary investigation|

* Save the consultation
* Navigate to queues
* Search patient "Ameer Yonus" from "More Information" queue
* Verify patient details of "Ameer Yonus" in queue 

   |Date Of Presentation|Name       |Nationality|Name Of MLO   |Specialty|Outcomes For 1st Stage Surgical Validation|Outcomes For 1st Stage Anaesthesia Validation|Type Of Medical Information Needed For Next Submission|
   |--------------------|-----------|-----------|--------------|---------|------------------------------------------|---------------------------------------------|------------------------------------------------------|
   |10/10/2016          |Ameer Yonus|Egyptian   |Dr. Feras Nasr|Plastic  |More Information                          |Need complementary investigation             |more medical info                                     |

* Wait for the scheduler to run and close the visit
* Search and select patient "Ameer Yonus" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Verify Consultation button is not present

1. Verify Patient in Validated Patients queue - FSTG. 2. Patient In Expected arrival queue. 3. Patient In Hospital RSP queue.
-----------------------------------------------------------------------------------------------------------------------------
// Verify Patient in Validated Patients queue - FSTG
* On the login page
* Login with user "weaam_a" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on registration app
* Click on create new patient link
* Enter Patient Details 

   |firstName|lastName|givenNameArabic|familyNameArabic|gender|age|governorate|country|phoneNumber1|spokenLanguages|nationality1|isCareTakerRequiredCheckBox|statusofOfficialIDdocuments|caretakerNameEnglish|caretakerGender|caretakerNationality|legalRepalsoCaretaker|
   |---------|--------|---------------|----------------|------|---|-----------|-------|------------|---------------|------------|---------------------------|---------------------------|--------------------|---------------|--------------------|---------------------|
   |Kabir    |Yonus   |عبدالله        |حسن             |Male  |30 |Amman      |Jordan |+9898989898 |English        |Egyptian    |True                       |Waiting                    |Nadira              |Female         |Iraqi               |Yes                  |

* Start "First Stage Validation" visit and navigate to Programs page
* Enroll patient to the following program 

   |name                  |dateOfRegistration|programStatus |
   |----------------------|------------------|--------------|
   |Reconstructive Surgery|09/09/2016        |Identification|

* On the login page
* Login with user "hani_i" and password "BAHMNI_GAUGE_VC_MEMBER_PASSWORD" with location "BAHMNI_GAUGE_VC_MEMBER_LOCATION"
* Click on programs app
* Search and select patient "Kabir Yonus" from "Awaiting Validation - 1st Stage" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Patient History" from observation page and fill details 

   |FIELD                    |VALUE              |
   |-------------------------|-------------------|
   |Name of MLO              |Dr. Aziz Abu Azizeh|
   |Patient General Condition|Walking Alone      |

* Select template "First Stage Validation" from observation page and fill details 

   |FIELD                                           |VALUE                    |
   |------------------------------------------------|-------------------------|
   |Type of medical information received            |Updated Medical file     |
   |Date Received                                   |04/04/2016               |
   |Is the medical file complete?                   |Yes                      |
   |Document(s) needed to be complete               |all completed            |
   |Specialty                                       |Orthopedic               |
   |Stage                                           |2                        |
   |Date of presentation                            |10/10/2016               |
   |Outcome for 1st stage surgical validation       |Valid                    |
   |Priority                                        |Low                      |
   |Name of Surgeon 1                               |Dr. Rasheed Al Samerai   |
   |Name of Surgeon 2                               |Dr. Hanna Janho          |
   |Does the Patient need Surgical Final Validation?|Yes                      |
   |Comments                                        |validation done          |
   |Outcome for 1st stage Anaesthesia validation    |Fits anaesthesia criteria|
   |Name of Anaesthetist                            |Dr. Hadeel Al-Ani        |

* Select template "Final Validation" from observation page and fill details 

   |FIELD                               |VALUE               |
   |------------------------------------|--------------------|
   |Does the Patient need Accommodation?|Yes                 |
   |Type of Admission Recommended       |Normal admission    |
   |Name of Surgeon 1                   |Dr. Sofian Al-Qassab|

* Save the consultation
* Navigate to queues
* Search patient "Kabir Yonus" from "Validated Patients" queue
* Verify patient details of "Kabir Yonus" in queue 

   |Date Of Presentation|Name       |Age|Country|Name Of MLO        |Stage|Specialty |Name Of Surgeon     |Priority|Comments About Validation|Does The Patient Need Surgical Final Validation|Is Caretaker Required?|Status Of Official ID Documents|
   |--------------------|-----------|---|-------|-------------------|-----|----------|--------------------|--------|-------------------------|-----------------------------------------------|----------------------|-------------------------------|
   |10/10/2016          |Kabir Yonus|30 |Jordan |Dr. Aziz Abu Azizeh|2    |Orthopedic|Dr. Sofian Al-Qassab|Low     |validation done          |Yes                                            |Yes                   |Waiting                        |

// Patient In Expected arrival queue
* On the login page
* Login with user "weaam_a" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on registration app
* Search patient with name "Kabir Yonus"
* Select the patient from the search results
* Enter Patient Details 

   |expectedDateofArrival|
   |---------------------|
   |06/06/2017           |

* Save Patient
* Go to Home Page
* Click on programs app
* Search patient "Kabir Yonus" from "Expected Arrival" queue
* Verify patient details of "Kabir Yonus" in queue 

   |Name       |Age|Country|Specialty |Stage|Priority|Comments About Validation|Name Of Surgeon     |Expected Date Of Arrival|Patient General Condition|Does The Patient Need Accomodation|Type Of Admission Recommended|Is Caretaker Required?|Caretaker Gender|Caretaker Name|
   |-----------|---|-------|----------|-----|--------|-------------------------|--------------------|------------------------|-------------------------|----------------------------------|-----------------------------|----------------------|----------------|--------------|
   |Kabir Yonus|30 |Jordan |Orthopedic|2    |Low     |validation done          |Dr. Sofian Al-Qassab|06/06/2017              |Walking Alone            |Yes                               |Normal admission             |Yes                   |Female          |Nadira        |
* Wait for the scheduler to run and close the visit

// Patient In Hospital RSP queue
* On the login page
* Login with user "weaam_a" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on registration app
* Search patient with name "Kabir Yonus"
* Select the patient from the search results
* Enter Patient Details 

   |dateofArrival|
   |-------------|
   |05/05/2017   |

* Start "Hospital" visit and navigate to Programs page
* Edit "Reconstructive Surgery" Program with following details 

   |programStatus|
   |-------------|
   |Pre-Operative|

* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Surgeon Pre-Op Assessment and Treatment Plan" from observation page and fill details 

   |FIELD               |VALUE     |
   |--------------------|----------|
   |Date of consultation|05/05/2017|

* Select template "Anesthesia Initial Assessment" from observation page and fill details 

   |FIELD                                                                         |VALUE     |
   |------------------------------------------------------------------------------|----------|
   |Date of consultation                                                          |05/05/2017|
   |ASA score *                                                                   |ASA II    |
   |I discussed the risks and benefits of anaesthesia and answered all questions *|Yes       |

* Save the consultation
* Navigate to queues
* Search patient "Kabir Yonus" from "Hospital RSP" queue
* Verify patient details of "Kabir Yonus" in queue 

   |Date Of Arrival|Name       |Age|Country|Is Caretaker Required?|Specialty |Stage|Name Of Surgeon     |Date Of Consultation (Anaesth.)|Date Of Consultation (Surgeon)|Phase Of Treatment|
   |---------------|-----------|---|-------|----------------------|----------|-----|--------------------|-------------------------------|------------------------------|------------------|
   |05/05/2017     |Kabir Yonus|30 |Jordan |Yes                   |Orthopedic|2    |Dr. Sofian Al-Qassab|05/05/2017                     |05/05/2017                    |Pre-Operative     |

* Search and select patient "Kabir Yonus" from "Programs" queue
* Edit "Reconstructive Surgery" Program with following details 

   |programStatus    |
   |-----------------|
   |Network Follow-up|

* Wait for the scheduler to run and close the visit
* Navigate to queues
* Search patient "Kabir Yonus" from "To Continue Under Follow-Up" queue
* Verify patient details of "Kabir Yonus" in queue

   |Name       |Specialty |Name Of MLO        |
   |-----------|----------|-------------------|
   |Kabir Yonus|Orthopedic|Dr. Aziz Abu Azizeh|

1. Patient In Awaiting Follow up validation queue. 2. Patient In Continue Follow up validation queue
----------------------------------------------------------------------------------------------------
 Create Patient and Verify Programs Queue.
* On the login page
* Login with user "weaam_a" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on registration app
* Click on create new patient link
* Enter Patient Details

   |firstName|lastName|givenNameArabic|familyNameArabic|gender|age|governorate|country|phoneNumber1|spokenLanguages|nationality1|isCareTakerRequiredCheckBox|statusofOfficialIDdocuments|caretakerNameEnglish|caretakerGender|caretakerNationality|legalRepalsoCaretaker|
   |---------|--------|---------------|----------------|------|---|-----------|-------|------------|---------------|------------|---------------------------|---------------------------|--------------------|---------------|--------------------|---------------------|
   |Shazia   |Yonus   |عبدالله        |حسن             |Female|30 |Amman      |Jordan |+9898989898 |English        |Egyptian    |True                       |Waiting                    |Nadira              |Female         |Iraqi               |Yes                  |

* Start "Follow-Up Validation" visit and navigate to Programs page
* Enroll patient to the following program

   |name                  |dateOfRegistration|programStatus    |
   |----------------------|------------------|-----------------|
   |Reconstructive Surgery|09/09/2016        |Network Follow-up|

* Navigate to queues
* Search patient "Shazia Yonus" from "Programs" queue
* Verify patient details of "Shazia Yonus" in queue

   |Name        |
   |------------|
   |Shazia Yonus|

* Search patient "Shazia Yonus" from "Awaiting Validation - Follow Up Stage" queue
* Verify patient details of "Shazia Yonus" in queue

   |Name        |Nationality|
   |------------|-----------|
   |Shazia Yonus|Egyptian   |

   // Patient In Awaiting Follow up validation queue
* Search and select patient "Shazia Yonus" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Patient History" from observation page and fill details

   |FIELD      |VALUE              |
   |-----------|-------------------|
   |Name of MLO|Dr. Aziz Abu Azizeh|

* Select template "First Stage Validation" from observation page and fill details

   |FIELD    |VALUE     |
   |---------|----------|
   |Specialty|Orthopedic|

* Select template "Final Validation" from observation page and fill details

   |FIELD            |VALUE               |
   |-----------------|--------------------|
   |Name of Surgeon 1|Dr. Ashraf Bustangi |
   |Name of Surgeon 2|Dr. Muckhaled Naseef|

* Save the consultation
* Navigate to queues
* Search patient "Shazia Yonus" from "Awaiting Validation - Follow Up Stage" queue
* Verify patient details of "Shazia Yonus" in queue

   |Name        |Name Of MLO        |Nationality|Specialty |Name Of Surgeon 1  |Name Of Surgeon 2   |
   |------------|-------------------|-----------|----------|-------------------|--------------------|
   |Shazia Yonus|Dr. Aziz Abu Azizeh|Egyptian   |Orthopedic|Dr. Ashraf Bustangi|Dr. Muckhaled Naseef|


// Patient In Continue Follow up validation queue
* On the login page
* Login with user "mahmoud_h" and password "BAHMNI_GAUGE_VC_MEMBER_PASSWORD" with location "BAHMNI_GAUGE_VC_MEMBER_LOCATION"
* Click on programs app
* Search and select patient "Shazia Yonus" from "Awaiting Validation - Follow Up Stage" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Follow-up Validation" from observation page and fill details

   |FIELD                                    |VALUE                   |
   |-----------------------------------------|------------------------|
   |Date of presentation                     |10/10/2016              |
   |Outcome for follow-up surgical validation|Continue under follow-up|
   |Time for next medical follow-up          |1 month                 |
   |Date of next medical follow-up           |12/12/2017              |
   |Type of medical investigations requested |X-ray                   |
   |Comments about next follow-up            |Followup After 1 month  |

* Save the consultation
* Navigate to queues
* Search patient "Shazia Yonus" from "To Continue Under Follow-Up " queue
* Verify patient details of "Shazia Yonus" in queue

   |Date Of Presentation|Name        |Specialty |Name Of MLO        |Time For Next Medical Follow-up|Date Of Next Medical Follow-up|Type Of Medical Investigations Requested|Comments              |
   |--------------------|------------|----------|-------------------|-------------------------------|------------------------------|----------------------------------------|----------------------|
   |10/10/2016          |Shazia Yonus|Orthopedic|Dr. Aziz Abu Azizeh|1 month                        |12/12/2017                    |X-ray                                   |Followup After 1 month|

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
* Select template "Patient History" from observation page and fill details 

   |FIELD      |VALUE              |
   |-----------|-------------------|
   |Name of MLO|Dr. Aziz Abu Azizeh|

* Select template "First Stage Validation" from observation page and fill details 

   |FIELD    |VALUE     |
   |---------|----------|
   |Specialty|Orthopedic|

* Select template "Follow-up Validation" from observation page and fill details 

   |FIELD                                           |VALUE                           |
   |------------------------------------------------|--------------------------------|
   |Qualitative outcome-Union                       |Non united                      |
   |Qualitative outcome - Infection                 |Pin tract infection             |
   |Qualitative outcome - SMFA                      |Done                            |
   |Date of presentation                            |07/07/2016                      |
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

   |Date Of Presentation|Name      |Age|Country|Name Of MLO        |Stage|Specialty |Name Of Surgeon       |Priority|Comments About Validation       |Does The Patient Need Surgical Final Validation|Is Caretaker Required?|Status Of Official ID Documents|
   |--------------------|----------|---|-------|-------------------|-----|----------|----------------------|--------|--------------------------------|-----------------------------------------------|----------------------|-------------------------------|
   |07/07/2016          |Abdul Bari|30 |Jordan |Dr. Aziz Abu Azizeh|3    |Orthopedic|Dr. Rasheed Al Samerai|Moderate|further stage admission comments|Yes                                            |Yes                   |Waiting                        |
