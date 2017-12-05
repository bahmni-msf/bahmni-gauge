Other Observation Forms
=======================
Created by jaseenam on 5/29/17

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

Other Observation Forms
-----------------------
//* Create patient "Other Forms" using API with "Hospital" visit
//* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_OPD_USER" and password "BAHMNI_GAUGE_OPD_PASSWORD" with location "BAHMNI_GAUGE_OPD_LOCATION"
* Click on programs app
* Select patient "Other Forms" in tab "All"
* Edit "Reconstructive Surgery" Program with following details 

   |programStatus|
   |-------------|
   |Pre-Operative|

* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Select template "OPD Nursing Initial Assessment" from observation page and fill details

   |FIELD               |VALUE                 |
   |--------------------|----------------------|
   |Date of consultation|01/01/2017            |
   |Pain severity       |2                     |
   |Side of pain        |Right                 |
   |Site of pain        |Stump                 |
   |Number of wounds    |2                     |
   |Site                |Ear;Nose              |
   |Description         |new Description       |
   |Nursing notes       |captured Nursing notes|

* Select template "Vital Signs" from observation page and fill details

   |FIELD                              |VALUE       |
   |-----------------------------------|------------|
   |Date recorded                      |01/01/2017  |
   |Weight (Kg)                        |80          |
   |Height (cm)                        |170         |
   |Respiratory rate (breaths/minute)  |2           |
   |Temperature (C)                    |36          |
   |Pulse (bpm)                        |68          |
   |Blood oxygen saturation (%)        |92          |
   |Comments about baseline vital signs|Low pressure|

* Select template "Physician Progress Note-Ward" from observation page and fill details

   |FIELD                                 |VALUE                                                                    |
   |--------------------------------------|-------------------------------------------------------------------------|
   |Date recorded                         |04/04/2017                                                               |
   |Subjective (any new complaint)        |add new complaint                                                        |
   |Patient complaints                    |None;Pain;Nausea and vomiting;Diarrhea;Fever;Dyspnea;Abdominal Pain;Other|
   |Patient complaints, other             |Chilling                                                                 |
   |Assessment of vital signs             |Abnormal                                                                 |
   |Description of abnormal vital signs   |Abnormal Description                                                     |
   |Patient appetite                      |Poor                                                                     |
   |DVT prophylaxis                       |Yes                                                                      |
   |Duration                              |3 days                                                                   |
   |Dose                                  |4 per day                                                                |
   |Side of wound                         |Right                                                                    |
   |Wound status, 1                       |Closed                                                                   |
   |Wound status, 2                       |Discharge; Sinus                                                         |
   |Removal of clips                      |Yes                                                                      |
   |Wound assessment                      |Wound seen                                                               |
   |Description of wound                  |Other                                                                    |
   |Description of wound, other           |Other Description                                                        |
   |Drainage                              |Other                                                                    |
   |Drainage amount                       |5 ml                                                                     |
   |Drainage, other                       |other drainage comments                                                  |
   |Frequency of dressing                 |Other                                                                    |
   |Frequency of dressing, other          |Frequency of dressing, other comments                                    |
   |Abnormal lab values                   |High Temperature                                                         |
   |Active issues of patient              |IV antibiotics;Daily dressing;Isolation;Pain control;Other               |
   |Active issues of patient, other       |other issues                                                             |
   |Assessment of patient                 |Other                                                                    |
   |Assessment of patient, other          |other assessment                                                         |
   |Surgeon informed of patient assessment|Yes                                                                      |
   |Surgical ward patient care plan       |Removal of drain;Other                                                   |
   |Specify side of drain removal         |Right                                                                    |
   |Specify site of drain removal         |Site, Hand                                                               |
   |Surgical ward patient care plan, other|other care plan                                                          |
   |Summary of consultation               |Consultation comments                                                    |

* Select template "Surgeon Pre-Op Assessment and Treatment Plan" from observation page and fill details

   |FIELD                                   |VALUE                                                                                   |
   |----------------------------------------|----------------------------------------------------------------------------------------|
   |Date of consultation                    |05/05/2017                                                                              |
   |Site of injury                          |Site, Shoulder                                                                          |
   |Side of injury                          |Right                                                                                   |
   |Condition of soft tissue at presentation|Bad (need soft tissue coverage)                                                         |
   |Associated neural injury                |Yes                                                                                     |
   |Comments (neural injury)                |comments                                                                                |
   |Associated vascular injury              |Yes                                                                                     |
   |Is patient for surgery                  |Yes                                                                                     |
   |Has Patient Consent Been Obtained?      |Yes                                                                                     |
   |Planned Procedure (surgical)            |Debridement of bone                                                                     |
   |Side of surgical procedure              |Left                                                                                    |
   |Est Hours (Hrs)                         |1                                                                                       |
   |Est Minutes (Mins)                      |20                                                                                      |
   |Surgical summary                        |surgery summary comment                                                                 |
   |Initial general plan                    |Needs Physio / Other consultation                                                       |
   |Objectives of physiotherapy             |physio comments                                                                         |
   |Surgical objective                      |Repair anatomy;Prevent future problems;Uncertain;Replace loss;Manage long-term pathology|
   |Comments of uncertainty                 |uncertainty comments                                                                    |
   |Comments about surgical objectives      |comments                                                                                |
   |Frequency of Operations                 |Multiple Operations (+2)                                                                |
   |Estimated number of surgeries           |3                                                                                       |
   |Sites (donor areas excluded)            |Multi-site, different surgery                                                           |
   |Spacing between surgeries               |2                                                                                       |
   |Estimated length of stay                |30-60 days                                                                              |
   |Does the patient need further admissions|Yes                                                                                     |
   |Need consultations                      |Maxillo-facial;Orthopedic;Other;Plastic                                                 |
   |Reason for consultation                 |New Reason for consultation                                                             |
   |Other consultation needed               |other comments                                                                          |

* Select template "Ward Nursing Note" from observation page and fill details

   |FIELD                                   |VALUE      |
   |----------------------------------------|-----------|
   |Date recorded                           |05/05/2017 |
   |Pain Severity                           |1          |
   |Side of pain                            |Right      |
   |Site of pain                            |Hand       |
   |Type of pain                            |severe     |
   |When does the pain occur                |always     |
   |Does the patient have a dressing?       |Yes        |
   |Side of dressing                        |Right      |
   |Site of dressing                        |Site, Iliac|
   |Description of wound                    |Other      |
   |Description of wound, other             |wet wound  |
   |Dressing, comments                      |dressed    |
   |Does the patient have a peripheral line?|Yes        |
   |Site of peripheral line                 |Site, Wrist|
   |Date of insertion, peripheral line      |05/05/2017 |
   |Date of removal, peripheral line        |07/07/2017 |
   |Comments, peripheral line               |comments   |
   |Does the patient have a PICC line?      |Yes        |
   |Date of insertion, PICC line            |05/05/2017 |
   |Date of dressing                        |05/05/2017 |
   |Comments, dressing PICC line            |comments   |
   |Date of removal, PICC line              |08/08/2017 |
   |Does the patient have a Foley catheter? |No         |
   |Does the patient have a tissue expander?|Yes        |
   |Site of tissue expander                 |Site, Toe  |
   |Quantity injected (cc)                  |1          |
   |Quantity withdrawn (cc)                 |2          |
   |Total volume in tissue expander (cc)    |3          |
   |Condition of tissue expander            |no         |
   |Nursing consultation notes              |done       |
   |Blood sugar                             |Yes        |
   |RBS before meal                         |6          |
   |RBS after meal                          |7          |
   |FBS                                     |10         |
   |Insulin given                           |Yes        |
   |How much insulin given                  |15         |

* Verify "Ward Nursing Note" is added to the left pane
* Select template "Surgical Ward Admission Nursing Assessment" from observation page and fill details

   |FIELD                                                 |VALUE                                                                                                                      |
   |------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
   |Date recorded                                         |05/05/2017                                                                                                                 |
   |Reason for admission                                  |Other                                                                                                                      |
   |Reason for admission, other                           |Physio                                                                                                                     |
   |Pain Severity                                         |1                                                                                                                          |
   |Side of pain                                          |Right                                                                                                                      |
   |Site of pain                                          |Leg                                                                                                                        |
   |Type of pain                                          |severe                                                                                                                     |
   |When does the pain occur                              |always                                                                                                                     |
   |Patient mood                                          |Other                                                                                                                      |
   |Patient mood, other                                   |Excited                                                                                                                    |
   |Does the patient have suicidal or depressive thoughts?|No                                                                                                                         |
   |Number of wounds                                      |4                                                                                                                          |
   |Site of wound                                         |Site, Scalp                                                                                                                |
   |Description                                           |Wound needs dressing                                                                                                       |
   |Nutritional Assessment                                |Regular;Low salt;High protein;Diabetic diet;Other                                                                          |
   |Nutritional Assessment, other                         |Bitter                                                                                                                     |
   |Admission Nursing Notes                               |Admit by tomorrow morning                                                                                                  |
   |Orientation of the patient                            |Environment;General Hygiene;Medication;Visiting hours;Isolation instructions;Sleeping time;Meal time;Smoking;Discharge plan|

* Verify "Surgical Ward Admission Nursing Assessment" is added to the left pane
* Select template "Post-Op Ward Monitoring" from observation page and fill details

   |FIELD                            |VALUE                |
   |---------------------------------|---------------------|
   |Date recorded                    |05/05/2017           |
   |Consciousness                    |Awake                |
   |Oxygen (L/min)                   |80                   |
   |Blood oxygen saturation (%)      |56                   |
   |Respiration rate (breaths/minute)|85                   |
   |Pulse (bpm)                      |77                   |
   |Systolic blood pressure (mmHg)   |120                  |
   |Diastolic blood pressure (mmHg)  |80                   |
   |Temperature (C)                  |32                   |
   |Pain Severity                    |1                    |
   |Side of pain                     |Right                |
   |Site of pain                     |Leg                  |
   |Type of pain                     |severe               |
   |When does the pain occur         |always               |
   |Nausea                           |Yes                  |
   |Vomiting                         |No                   |
   |Side of dressing                 |Right                |
   |Site of dressing                 |Site, Iliac          |
   |Description of wound             |Other                |
   |Description of wound, other      |fresh since one month|
   |Urine                            |Yes                  |
   |Does the patient have a drain?   |Yes                  |
   |Side of drain                    |Left                 |
   |Site of drain                    |Site, Toe            |
   |Drainage                         |2000                 |
   |Patient Position                 |sitting              |

* Verify "Post-Op Ward Monitoring" is added to the left pane
* Select template "Surgeon Follow-up" from observation page and fill details

   |FIELD                             |VALUE                                        |
   |----------------------------------|---------------------------------------------|
   |Date recorded                     |05/05/2017                                   |
   |Early Follow-up                   |Complications developed                      |
   |Impact of complication            |Did not effect the results of flow           |
   |Patient requires amputation       |Yes                                          |
   |Is patient for surgery            |Yes                                          |
   |Has patient consent been obtained?|Yes                                          |
   |Planned Procedure (surgical)      |Dental extraction                            |
   |Side of surgical procedure        |Left                                         |
   |Est Hours (Hrs)                   |1                                            |
   |Est Minutes (Mins)                |30                                           |
   |Surgical summary                  |need periodic monitoring of patient condition|


* Verify "Surgeon Follow-up" is added to the left pane
* Select template "Operative Report" from observation page and fill details

   |FIELD                         |VALUE                                                                                                                                                               |
   |------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   |Surgeon                       |Dr. Ali Al-Ani;Dr. Sofian Al-Qassab;Dr. Hanna Janho;Dr. Ashraf Nabhan;Dr. Rasheed Al Samerai;Dr. Muckhaled Naseef;Dr. Ashraf Bustangi;Dr.Ghassan S. Abu-Sittah;Other|
   |Surgeon assistant             |Dr. Azeez                                                                                                                                                           |
   |Anaesthetist                  |Dr. Hadeel Al-Ani;Dr. Abdelraouf Alhamad;Dr. Ammar Subhi;Other                                                                                                      |
   |Anaesthesia technician        |Dr. Hani                                                                                                                                                            |
   |Type of anaesthesia           |None;GAI;GAO;GAL;RSA;RPX;RTA;RAO;LOA;SED;INF                                                                                                                        |
   |Scrub nurse                   |Nurse Hanna                                                                                                                                                         |
   |Operation performed           |Quadricepsplasty                                                                                                                                                    |
   |Size of tissue expander       |2                                                                                                                                                                   |
   |Side of operation             |Right                                                                                                                                                               |
   |Findings                      |New findings                                                                                                                                                        |
   |Operation details             |operation successful                                                                                                                                                |
   |Does the patient have a drain?|Yes                                                                                                                                                                 |
   |Side of drain                 |Left                                                                                                                                                                |
   |Site of drain                 |Site, Leg                                                                                                                                                           |
   |Type of drain inserted        |Vacuum drain                                                                                                                                                        |
   |Specimen sent to lab          |Yes                                                                                                                                                                 |
   |Estimated blood loss          |6                                                                                                                                                                   |
   |Blood transfusion             |Yes                                                                                                                                                                 |
   |Number of units               |7                                                                                                                                                                   |

* Verify "Operative Report" is added to the left pane
* Select template "Observation Sheet" from observation page and fill details

   |FIELD                                  |VALUE                    |
   |---------------------------------------|-------------------------|
   |Temperature (C)                        |32                       |
   |Pulse (bpm)                            |77                       |
   |Respiratory rate (breaths/minute)      |85                       |
   |Systolic blood pressure (mmHg)         |120                      |
   |Diastolic blood pressure (mmHg)        |80                       |
   |Pain Severity                          |1                        |
   |Side of pain                           |Right                    |
   |Site of pain                           |Face                     |
   |Type of pain                           |severe                   |
   |When does the pain occur               |always                   |
   |Does the patient have a drain?         |Yes                      |
   |Side of drain                          |Left                     |
   |Site of drain                          |Site, Leg                |
   |Drainage                               |-30                      |
   |Total quantity evacuated from the drain|300                      |
   |Change Position                        |Change Position comments |
   |Additional Notes                       |Additional Notes comments|

* Select template "OPD Nursing Note" from observation page and fill details

   |FIELD                                   |VALUE      |
   |----------------------------------------|-----------|
   |Date recorded                           |05/05/2017 |
   |Temperature (C)                         |32         |
   |Pulse (bpm)                             |77         |
   |Respiratory rate (breaths/minute)       |85         |
   |Systolic blood pressure (mmHg)          |120        |
   |Diastolic blood pressure (mmHg)         |80         |
   |Pain Severity                           |1          |
   |Side of pain                            |Right      |
   |Site of pain                            |Ear        |
   |Type of pain                            |severe     |
   |When does the pain occur                |always     |
   |Does the patient have a dressing?       |Yes        |
   |Side of dressing                        |Right      |
   |Site of dressing                        |Site, Femur|
   |Description of wound                    |Other      |
   |Description of wound, other             |wet wound  |
   |Dressing, comments                      |dressed    |
   |Does the patient have a tissue expander?|Yes        |
   |Site of tissue expander                 |Site, Leg  |
   |Quantity injected (cc)                  |1          |
   |Quantity withdrawn (cc)                 |2          |
   |Total volume in tissue expander (cc)    |3          |
   |Condition of tissue expander            |normal     |
   |Nursing consultation notes              |recorded   |

* Verify "OPD Nursing Note" is added to the left pane
* Save the consultation
* Verify these forms are saved and disabled to add

   |FORM                                        |
   |--------------------------------------------|
   |Surgeon Follow-up                           |
   |Operative Report                            |
   |OPD Nursing Note                            |
   |Ward Nursing Note                           |
   |Surgical Ward Admission Nursing Assessment  |
   |OPD Nursing Initial Assessment              |
   |Surgeon Pre-Op Assessment and Treatment Plan|
   |Vital Signs                                 |

* Verify this form is Add More form "Post-Op Ward Monitoring"
* Verify this form is Add More form "Physician Progress Note-Ward"
* Verify this form is Add More form "Observation Sheet"

