Operation Theatre Scheduling
============================
Created by jaseenam on 6/15/17

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

Prerequisite: Create Patient Via Api for OT Functionality Verification
----------------------------------------------------------------------
* Create patient "ot schedulea" using API with "Hospital" visit
* Enroll patient to reconstructive surgery program using API

* Create patient "ot cancela" using API with "Hospital" visit
* Enroll patient to reconstructive surgery program using API

* Create patient "ot postponea" using API with "Hospital" visit
* Enroll patient to reconstructive surgery program using API

* Create patient "ot completea" using API with "Hospital" visit
* Enroll patient to reconstructive surgery program using API

Prerequisite: Add forms and admit the patient
---------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "ot schedulea" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Disposition" tab
* Select "Admit to RC" disposition with notes "Admit this patient to RC"
* Go to "Observations" tab
* Select template "First Stage Validation" from observation page and fill details 

     |FIELD                               |VALUE               |
     |------------------------------------|--------------------|
     |Type of medical information received|Updated Medical file|
     |Date Received                       |04/04/2016          |
     |Is the medical file complete?       |Yes                 |
     |Document(s) needed to be complete   |all completed       |
     |Specialty                           |Orthopedic          |
     |Stage                               |2                   |

* Select template "Final Validation" from observation page and fill details 

     |FIELD               |VALUE         |
     |--------------------|--------------|
     |Date of Presentation|04/04/2016    |
     |Name of Surgeon 1   |Dr. Ali Al-Ani|

* Select template "Surgeon Pre-Op Assessment and Treatment Plan" from observation page and fill details 

     |FIELD                             |VALUE                  |
     |----------------------------------|-----------------------|
     |Date of consultation              |05/05/2017             |
     |Is patient for surgery            |Yes                    |
     |Has Patient Consent Been Obtained?|Yes                    |
     |Surgical summary                  |surgery summary comment|
     |Planned Procedure (surgical)      |Debridement of bone    |
     |Est Hours (Hrs)                   |1                      |
     |Est Minutes (Mins)                |20                     |

* Select template "Anesthesia Initial Assessment" from observation page and fill details 

     |FIELD                                                                         |VALUE            |
     |------------------------------------------------------------------------------|-----------------|
     |Date of consultation                                                          |05/05/2017       |
     |ASA score *                                                                   |ASA II           |
     |Outcome of anaesthesia initial assessment                                     |Ready for surgery|
     |I discussed the risks and benefits of anaesthesia and answered all questions *|Yes              |

* Save the consultation
* Navigate to queues
* Search and select patient "ot cancela" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Disposition" tab
* Select "Admit to RC" disposition with notes "Admit this patient to RC"
* Go to "Observations" tab
* Select template "First Stage Validation" from observation page and fill details 

     |FIELD                               |VALUE               |
     |------------------------------------|--------------------|
     |Type of medical information received|Updated Medical file|
     |Date Received                       |04/04/2016          |
     |Is the medical file complete?       |Yes                 |
     |Document(s) needed to be complete   |all completed       |
     |Specialty                           |Orthopedic          |
     |Stage                               |2                   |

* Select template "Final Validation" from observation page and fill details 

     |FIELD               |VALUE         |
     |--------------------|--------------|
     |Date of Presentation|04/04/2016    |
     |Name of Surgeon 1   |Dr. Ali Al-Ani|

* Select template "Surgeon Pre-Op Assessment and Treatment Plan" from observation page and fill details 

     |FIELD                             |VALUE                  |
     |----------------------------------|-----------------------|
     |Date of consultation              |05/05/2017             |
     |Is patient for surgery            |Yes                    |
     |Has Patient Consent Been Obtained?|Yes                    |
     |Surgical summary                  |surgery summary comment|
     |Planned Procedure (surgical)      |Debridement of bone    |
     |Est Hours (Hrs)                   |1                      |
     |Est Minutes (Mins)                |20                     |

* Select template "Anesthesia Initial Assessment" from observation page and fill details 

     |FIELD                                                                         |VALUE            |
     |------------------------------------------------------------------------------|-----------------|
     |Date of consultation                                                          |05/05/2017       |
     |ASA score *                                                                   |ASA II           |
     |Outcome of anaesthesia initial assessment                                     |Ready for surgery|
     |I discussed the risks and benefits of anaesthesia and answered all questions *|Yes              |

* Save the consultation
* Navigate to queues
* Search and select patient "ot postponea" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Disposition" tab
* Select "Admit to RC" disposition with notes "Admit this patient to RC"
* Go to "Observations" tab
* Select template "First Stage Validation" from observation page and fill details 

     |FIELD                               |VALUE               |
     |------------------------------------|--------------------|
     |Type of medical information received|Updated Medical file|
     |Date Received                       |04/04/2016          |
     |Is the medical file complete?       |Yes                 |
     |Document(s) needed to be complete   |all completed       |
     |Specialty                           |Orthopedic          |
     |Stage                               |2                   |

* Select template "Final Validation" from observation page and fill details 

     |FIELD               |VALUE         |
     |--------------------|--------------|
     |Date of Presentation|04/04/2016    |
     |Name of Surgeon 1   |Dr. Ali Al-Ani|

* Select template "Surgeon Pre-Op Assessment and Treatment Plan" from observation page and fill details 

     |FIELD                             |VALUE                  |
     |----------------------------------|-----------------------|
     |Date of consultation              |05/05/2017             |
     |Is patient for surgery            |Yes                    |
     |Has Patient Consent Been Obtained?|Yes                    |
     |Surgical summary                  |surgery summary comment|
     |Planned Procedure (surgical)      |Debridement of bone    |
     |Est Hours (Hrs)                   |1                      |
     |Est Minutes (Mins)                |20                     |

* Select template "Anesthesia Initial Assessment" from observation page and fill details 

     |FIELD                                                                         |VALUE            |
     |------------------------------------------------------------------------------|-----------------|
     |Date of consultation                                                          |05/05/2017       |
     |ASA score *                                                                   |ASA II           |
     |Outcome of anaesthesia initial assessment                                     |Ready for surgery|
     |I discussed the risks and benefits of anaesthesia and answered all questions *|Yes              |

* Save the consultation
* Navigate to queues
* Search and select patient "ot completea" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Disposition" tab
* Select "Admit to RC" disposition with notes "Admit this patient to RC"
* Go to "Observations" tab
* Select template "First Stage Validation" from observation page and fill details 

     |FIELD                               |VALUE               |
     |------------------------------------|--------------------|
     |Type of medical information received|Updated Medical file|
     |Date Received                       |04/04/2016          |
     |Is the medical file complete?       |Yes                 |
     |Document(s) needed to be complete   |all completed       |
     |Specialty                           |Orthopedic          |
     |Stage                               |2                   |

* Select template "Final Validation" from observation page and fill details 

     |FIELD               |VALUE         |
     |--------------------|--------------|
     |Date of Presentation|04/04/2016    |
     |Name of Surgeon 1   |Dr. Ali Al-Ani|

* Select template "Surgeon Pre-Op Assessment and Treatment Plan" from observation page and fill details 

     |FIELD                             |VALUE                  |
     |----------------------------------|-----------------------|
     |Date of consultation              |05/05/2017             |
     |Is patient for surgery            |Yes                    |
     |Has Patient Consent Been Obtained?|Yes                    |
     |Surgical summary                  |surgery summary comment|
     |Planned Procedure (surgical)      |Debridement of bone    |
     |Est Hours (Hrs)                   |1                      |
     |Est Minutes (Mins)                |20                     |

* Select template "Anesthesia Initial Assessment" from observation page and fill details 

     |FIELD                                                                         |VALUE            |
     |------------------------------------------------------------------------------|-----------------|
     |Date of consultation                                                          |05/05/2017       |
     |ASA score *                                                                   |ASA II           |
     |Outcome of anaesthesia initial assessment                                     |Ready for surgery|
     |I discussed the risks and benefits of anaesthesia and answered all questions *|Yes              |

* Save the consultation

Admit Patient in RC
-------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "bed management" module
* Search patient "ot completea" from "Admit to RC" queue
* Click on "Admit To RC" link
* Click on "Rehabilitation Center" button
* Navigate to "Rehabilitation Center 4th floor"
* Assign an empty bed to the patient

* Navigate to patient ADT queues
* Search patient "ot postponea" from "Admit to RC" queue
* Click on "Admit To RC" link
* Click on "Rehabilitation Center" button
* Navigate to "Rehabilitation Center 4th floor"
* Assign an empty bed to the patient

* Navigate to patient ADT queues
* Search patient "ot cancel" from "Admit to RC" queue
* Click on "Admit To RC" link
* Click on "Rehabilitation Center" button
* Navigate to "Rehabilitation Center 4th floor"
* Assign an empty bed to the patient

* Navigate to patient ADT queues
* Search patient "ot schedulea" from "Admit to RC" queue
* Click on "Admit To RC" link
* Click on "Rehabilitation Center" button
* Navigate to "Rehabilitation Center 4th floor"
* Assign an empty bed to the patient

Verify the paients are in "To Be Scheduled" queue of Operation Theatre Scheduling Page
--------------------------------------------------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "operation theatre" module
* Search patient "ot schedulea" from "To Be Scheduled" queue
* Verify patient details of "ot schedule" in queue 

     |Name             |Planned Procedure  |Surgeon Name  |Speciality|Outcome Of Anaesthesia|
     |-----------------|-------------------|--------------|----------|----------------------|
     |ot schedulea Hasan|Debridement of bone|Dr. Ali Al-Ani|Orthopedic|Ready for surgery     |

* Search patient "ot cancela" from "To Be Scheduled" queue
* Verify patient details of "ot cancel" in queue 

     |Name           |Planned Procedure  |Surgeon Name  |Speciality|Outcome Of Anaesthesia|
     |---------------|-------------------|--------------|----------|----------------------|
     |ot cancela Hasan|Debridement of bone|Dr. Ali Al-Ani|Orthopedic|Ready for surgery     |

* Search patient "ot postponea" from "To Be Scheduled" queue
* Verify patient details of "ot postpone" in queue 

     |Name             |Planned Procedure  |Surgeon Name  |Speciality|Outcome Of Anaesthesia|
     |-----------------|-------------------|--------------|----------|----------------------|
     |ot postponea Hasan|Debridement of bone|Dr. Ali Al-Ani|Orthopedic|Ready for surgery     |

* Search patient "ot completea" from "To Be Scheduled" queue
* Verify patient details of "ot completea" in queue

     |Name             |Planned Procedure  |Surgeon Name  |Speciality|Outcome Of Anaesthesia|
     |-----------------|-------------------|--------------|----------|----------------------|
     |ot completea Hasan|Debridement of bone|Dr. Ali Al-Ani|Orthopedic|Ready for surgery     |

Create Surgical Block
---------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "operation theatre" module
* Navigate to OT Scheduling tab
* Create a new surgical block for "Hanna Janho" in "OT 1" from date "09/09/2017" time "09:00 AM" to date "09/09/2017" time "11:00 AM"

Edit Surgical Block
-------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "operation theatre" module
* Navigate to OT Scheduling tab
* Edit surgical block "Hanna Janho" in "OT 1" on "09 Sep 2017, Sat" with following details 

     |Surgeon         |Location|Start Date|Start Time|End Date  |End Time|
     |----------------|--------|----------|----------|----------|--------|
     |Muckhaled Naseef|OT 3    |10/10/2017|01:00 PM  |10/10/2017|05:00 PM|

Cancel Surgical Block from Surgical Block
-----------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "operation theatre" module
* Navigate to OT Scheduling tab
Create a new surgical block for "Hanna Janho" in "OT 1" from date "09/09/2017" time "09:00 AM" to date "09/09/2017" time "11:00 AM"
* Cancel surgical block from Surgical Block for "Hanna Janho" in "OT 1" on "09 Sep 2017, Sat" with reason "Cancel reason from Surgical Block"

Cancel Surgical Block from Calendar
-----------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "operation theatre" module
* Navigate to OT Scheduling tab
* Create a new surgical block for "Hanna Janho" in "OT 3" from date "09/09/2017" time "03:00 PM" to date "09/09/2017" time "06:00 PM"
* Cancel surgical block from Calendar for "Hanna Janho" in "OT 3" on "09 Sep 2017, Sat" with reason "Cancel reason from calendar"

Postpone Surgical Block from Surgical Block
-------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "operation theatre" module
* Navigate to OT Scheduling tab
* Create a new surgical block for "Ashraf Nabhan" in "OT 2" from date "09/09/2017" time "09:00 AM" to date "09/09/2017" time "11:00 AM"
* Postpone surgical block from Surgical Block for "Ashraf Nabhan" in "OT 2" on "09 Sep 2017, Sat" with reason "Postpone reason from Surgical Block"

Postpone Surgical Block from Calendar
-------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "operation theatre" module
* Navigate to OT Scheduling tab
* Create a new surgical block for "Ali Al Ani" in "OT 3" from date "09/09/2017" time "09:00 AM" to date "09/09/2017" time "11:00 AM"
* Postpone surgical block from Calendar for "Ali Al-Ani" in "OT 3" on "09 Sep 2017, Sat" with reason "Postpone reason from calendar"

Create Surgical Block and add surgery
-------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on "operation theatre" module
* Navigate to OT Scheduling tab
* Create a new surgical block for "Ashraf Bustanji" in "OT 2" from date "10/11/2017" time "08:00 AM" to date "10/11/2017" time "11:00 AM"
* Add surgery with below details 

     |Patient ID or Name|Other Surgeon|Surgical Assistant|Anaesthetist|Scrub Nurse|Circulating Nurse|Notes        |
     |------------------|-------------|------------------|------------|-----------|-----------------|-------------|
     |ot schedulea Hasan |Hanna Janho  |Dr. SA            |Dr. A       |S nurse    |C nurse          |surgery notes|

//     |ot complete Hasan |Rasheed Al Sammarraie|Dr. SA            |Dr. A       |S nurse    |C nurse          |surgery notes|




