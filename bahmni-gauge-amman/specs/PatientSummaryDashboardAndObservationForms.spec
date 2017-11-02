Patient Summary Dashboard and Observation Forms
===============================================
Created by jaseena, swarup on 2/16/17

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

//Create Patient Via Api for Patient Summary Dashboard Display Verification
//-------------------------------------------------------------------------
//* Create patient "Sara" using API with "Hospital" visit
//* Enroll patient to reconstructive surgery program using API

Verify the Patient Summary Dashboard display controls visibility
----------------------------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Sara" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Click on "Patient Summary" dashboard
* Verify the following display controls are visible 

     |Display Control Title                       |
     |--------------------------------------------|
     |Patient Information                         |
     |Medication                                  |
     |Physical Examination                        |
     |Nursing Assessment                          |
     |Diagnoses                                   |
     |Surgical Ward Assessment                    |
     |Physician Progress Note-Ward                |
     |Post-Op Ward Monitoring                     |
     |Baseline Vital Signs                        |
     |Orders                                      |
     |MD Initial Assessment                       |
     |Surgeon Pre-Op Assessment and Treatment Plan|
     |OPD Nursing Note                            |
     |Ward Nursing Note                           |
     |Complications                               |
     |Surgical Appointments                       |
     |Surgeon Follow-up                           |
     |Operative Report                            |
     |OPD MD Follow-Up Note                       |

OPD Nurse - Baseline Vital Signs, OPD Nursing Initial Assessment forms
----------------------------------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_OPD_USER" and password "BAHMNI_GAUGE_OPD_PASSWORD" with location "BAHMNI_GAUGE_OPD_LOCATION"
* Click on programs app
* Search and select patient "Sara" from "Programs" queue
* Edit "Reconstructive Surgery" Program with following details 

     |programStatus|
     |-------------|
     |Pre-Operative|

* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Verify "Baseline Vital Signs" is added to the left pane
Verify "OPD Nursing Initial Assessment" is added to the left pane
* Select template "Baseline Vital Signs" from observation page and fill details 

     |FIELD                              |VALUE       |
     |-----------------------------------|------------|
     |Date recorded                      |01/01/2017  |
     |Weight (Kg)                        |80          |
     |Height (cm)                        |90          |
     |Respiratory rate (breaths/minute)  |2           |
     |Temperature (C)                    |36          |
     |Pulse (bpm)                        |8           |
     |Blood oxygen saturation (%)        |92          |
     |Comments about baseline vital signs|Low pressure|

* Select template "OPD Nursing Initial Assessment" from observation page and fill details 

     |FIELD               |VALUE     |
     |--------------------|----------|
     |Date of consultation|01/01/2017|
     |Pain severity       |2         |
     |Side of pain        |Right     |
     |Site of pain        |Arm       |
     |Number of wounds    |2         |
     |Site                |Ear;Nose  |
     |Description         |None      |
     |Nursing notes       |captured  |

* Save the consultation
* Navigate to patient dashboard
* Click on "Patient Summary" dashboard
* Verify following details of "Baseline Vital Signs" in Patient Dashboard 

     |FIELD                              |VALUE          |
     |-----------------------------------|---------------|
     |Date recorded                      |01 Jan 17      |
     |Weight                             |80Kg           |
     |Height                             |90cm           |
     |BMI                                |98.77Kg/m2     |
     |Respiratory rate                   |2breaths/minute|
     |Temperature                        |36C            |
     |Pulse                              |8bpm           |
     |Blood oxygen saturation            |92%            |
     |Comments about baseline vital signs|Low pressure   |

* Verify following details of "Nursing Assessment" in Patient Dashboard 

     |FIELD                 |VALUE    |
     |----------------------|---------|
     |Date of consultation  |01 Jan 17|
     |Pain severity (0 - 10)|2        |
     |Side of pain          |Right    |
     |Site of pain          |Arm      |
     |Number of wounds      |2        |
     |Site                  |Nose, Ear|
     |Description           |None     |
     |Nursing notes         |captured |

MD - MD Initial Assessment, Physical Examination and Medical Diagnoses, Complications and Physician Progress Note-Ward forms
----------------------------------------------------------------------------------------------------------------------------
* On the login page
* Login with user "zaid_se" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Sara" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Verify "MD Initial Assessment" is added to the left pane
* Verify "Physical Examination" is added to the left pane
* Verify "Medical Diagnoses" is added to the left pane
* Select template "MD Initial Assessment" from observation page and fill details 

     |FIELD                                                       |VALUE                                                                                                         |
     |------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
     |Date of consultation                                        |01/01/2017                                                                                                    |
     |Reason for admission to program                             |swollen leg                                                                                                   |
     |History of present illness                                  |6 months                                                                                                      |
     |Medical History                                             |Hypertension;Tuberculosis                                                                                     |
     |Other medical problems                                      |HIV                                                                                                           |
     |History of Allergy                                          |Drugs;Food                                                                                                    |
     |Comments about allergy                                      |Nothing                                                                                                       |
     |Currently taking medication                                 |Yes                                                                                                           |
     |Type of medication                                          |Some drug                                                                                                     |
     |Dose and frequency                                          |daily                                                                                                         |
     |Date of last dose                                           |01/01/2017                                                                                                    |
     |Function of injured part                                    |Limitation of function                                                                                        |
     |Sensation of injured part                                   |Reduced (Regional)                                                                                            |
     |History of previous surgery                                 |Yes                                                                                                           |
     |Surgical procedures performed outside AMH                   |Debridement of bone                                                                                           |
     |Site of procedure                                           |Site, Leg                                                                                                     |
     |Side of procedure                                           |Right                                                                                                         |
     |Comment of procedure                                        |comments                                                                                                      |
     |Date of procedure                                           |01/01/2017                                                                                                    |
     |Type of previous fixation                                   |External;Internal;Other                                                                                       |
     |Type of internal fixation                                   |Intramedullary nails;Plate;Wires;Screws                                                                       |
     |Duration of External fixation                               |Less than 6 months                                                                                            |
     |Other type of fixation                                      |other comments                                                                                                |
     |History of infection                                        |Yes                                                                                                           |
     |Comments about previous infection                           |comments                                                                                                      |
     |Discharging sinus                                           |Yes                                                                                                           |
     |Duration of discharging sinus                               |Less than 6 months                                                                                            |
     |Bone Loss                                                   |Yes                                                                                                           |
     |Cm of bone loss                                             |4                                                                                                             |
     |United fracture                                             |Yes                                                                                                           |
     |Shortening                                                  |Yes                                                                                                           |
     |Cm of shortening                                            |4                                                                                                             |
     |Review of systems, general                                  |Fever;Pain;Night Sweats;Fatigue;Weight Loss;Other                                                             |
     |Description and duration of symptom (general)               |3 months                                                                                                      |
     |Other ROS general symptoms                                  |other                                                                                                         |
     |Review of systems, cardiopulmonary                          |Angina;Shortness Of Breath;Cough;Chest Pain;Edema;Other                                                       |
     |Description and duration of symptom (cardiopulmonary)       |2 months                                                                                                      |
     |Other ROS cardiopulmonary symptoms                          |other                                                                                                         |
     |Review of systems, gastrointestinal                         |Vomiting;Heartburn;Jaundice;Bloody Stool;Nausea;Diarrhea;Constipation;Pain after meals;Other;Black/Tarry Stool|
     |Description and duration of symptom (gastrointestinal)      |1 month                                                                                                       |
     |Other ROS gastrointestinal symptoms                         |other                                                                                                         |
     |Review of systems, genitourinary                            |Incontinence;Hesitancy;Abnormal menses;Kidney Stones;Hematuria;Dysuria;Other                                  |
     |Description and duration of symptom (genitourinary)         |5 months                                                                                                      |
     |Other ROS genitourinary symptoms                            |other                                                                                                         |
     |Review of systems, central nervous system                   |Other;Dizziness;Focal Weakness;Confusion;Paresthesia;Headache                                                 |
     |Description and duration of symptom (central nervous system)|4 months                                                                                                      |
     |Other ROS central nervous system symptoms                   |other                                                                                                         |
     |Review of systems, HEENT                                    |Epistaxis;Dysphagia;Dental Caries;Vision Difficulties;Decreased Hearing;Other;Difficulty Chewing;Gum Bleeding |
     |Description and duration of symptom (HEENT)                 |3 months                                                                                                      |
     |Other ROS HEENT symptoms                                    |other                                                                                                         |
     |Review of systems, musculoskeletal                          |Joint Pain;Other;Joint Swelling;Generalized Weakness;Joint Stiffness;Muscular Soreness                        |
     |Description and duration of symptom (musculoskeletal)       |2 months                                                                                                      |
     |Other ROS musculoskeletal symptoms                          |other                                                                                                         |

* Select template "Physical Examination" from the Observation Page
* Select template "Complications" from observation page and fill details 

     |FIELD                                      |VALUE                                                                                    |
     |-------------------------------------------|-----------------------------------------------------------------------------------------|
     |Patient complication                       |Anaesthetic complication in OT                                                           |
     |Start date of complication                 |12/12/2016                                                                               |
     |Anaesthetic complication in OT, description|Hypoxia;Severe nausea and vomiting;Hypotension;Spinal headache;Aspiration;Pneumonia;Other|
     |Outcome of complication                    |Resolved                                                                                 |
     |End date of complication                   |02/02/2017                                                                               |

* Verify "Complications" is added to the left pane
* Select template "Physician Progress Note-Ward" from observation page and fill details 

     |FIELD                                 |VALUE                                                                    |
     |--------------------------------------|-------------------------------------------------------------------------|
     |Date recorded                         |04/04/2017                                                               |
     |Patient complaints                    |None;Pain;Nausea and vomiting;Diarrhea;Fever;Dyspnea;Abdominal Pain;Other|
     |Patient complaints, other             |Chilling                                                                 |
     |Patient appetite                      |Poor                                                                     |
     |Side of wound                         |Right                                                                    |
     |Site of wound                         |Site, Ankle                                                              |
     |Wound assessment                      |Wound seen                                                               |
     |Description of wound                  |Healing                                                                  |
     |Drainage                              |Serous                                                                   |
     |Assessment of patient                 |Stable                                                                   |
     |Surgeon informed of patient assessment|Yes                                                                      |
     |Surgical ward patient care plan       |Removal of drain                                                         |
     |Specify side of drain removal         |Right                                                                    |

* Save the consultation
* Navigate to patient dashboard
* Click on "Patient Summary" dashboard
* Verify following details of "Complications" in Patient Dashboard 

     |FIELD                                      |VALUE                                                                                          |
     |-------------------------------------------|-----------------------------------------------------------------------------------------------|
     |Patient complication                       |Anaesthetic complication in OT                                                                 |
     |Start date of complication                 |12 Dec 16                                                                                      |
     |Anaesthetic complication in OT, description|Hypoxia, Hypotension, Pneumonia, Aspiration, Severe nausea and vomiting, Other, Spinal headache|
     |Outcome of complication                    |Resolved                                                                                       |
     |End date of complication                   |02 Feb 17                                                                                      |

* Verify following details of "Physician Progress Note-Ward" in Patient Dashboard 

     |FIELD                                 |VALUE                                                                           |
     |--------------------------------------|--------------------------------------------------------------------------------|
     |Date recorded                         |04 Apr 17                                                                       |
     |Patient complaints                    |Other, Diarrhea, Fever, None, Dyspnea, Pain, Abdominal Pain, Nausea and vomiting|
     |Patient complaints, other             |Chilling                                                                        |
     |Patient appetite                      |Poor                                                                            |
     |Side of wound                         |Right                                                                           |
     |Site of wound                         |Ankle                                                                           |
     |Wound assessment                      |Wound seen                                                                      |
     |Description of wound                  |Healing                                                                         |
     |Drainage                              |Serous                                                                          |
     |Assessment of patient                 |Stable                                                                          |
     |Surgeon informed of patient assessment|Yes                                                                             |
     |Surgical ward patient care plan       |Removal of drain                                                                |
     |Specify side of drain removal         |Right                                                                           |

* Verify following details of "MD Initial Assessment" in Patient Dashboard 

     |FIELD                                                       |VALUE                                                                                                                  |
     |------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
     |Date of consultation                                        |01 Jan 17                                                                                                              |
     |Reason for admission to program                             |swollen leg                                                                                                            |
     |History of present illness                                  |6 months                                                                                                               |
     |Medical History                                             |Tuberculosis, Hypertension                                                                                             |
     |Other medical problems                                      |HIV                                                                                                                    |
     |History of Allergy                                          |Food, Drugs                                                                                                            |
     |Comments about allergy                                      |Nothing                                                                                                                |
     |Currently taking medication                                 |Yes                                                                                                                    |
     |Type of medication                                          |Some drug                                                                                                              |
     |Dose and frequency                                          |daily                                                                                                                  |
     |Date of last dose                                           |01 Jan 17                                                                                                              |
     |Function of injured part                                    |Limitation of function                                                                                                 |
     |Sensation of injured part                                   |Reduced (Regional)                                                                                                     |
     |History of previous surgery                                 |Yes                                                                                                                    |
     |Surgical procedures performed outside AMH                   |Debridement of bone                                                                                                    |
     |Site of procedure                                           |Leg                                                                                                                    |
     |Side of procedure                                           |Right                                                                                                                  |
     |Comment of procedure                                        |comments                                                                                                               |
     |Date of procedure                                           |01 Jan 17                                                                                                              |
     |Type of previous fixation                                   |Internal, Other, External                                                                                              |
     |Type of internal fixation                                   |Plate, Screws, Intramedullary nails, Wires                                                                             |
     |Duration of External fixation                               |Less than 6 months                                                                                                     |
     |Other type of fixation                                      |other comments                                                                                                         |
     |History of infection                                        |Yes                                                                                                                    |
     |Comments about previous infection                           |comments                                                                                                               |
     |Discharging sinus                                           |Yes                                                                                                                    |
     |Duration of discharging sinus                               |Less than 6 months                                                                                                     |
     |Bone Loss                                                   |Yes                                                                                                                    |
     |Cm of bone loss (0 - 99)                                    |4                                                                                                                      |
     |United fracture                                             |Yes                                                                                                                    |
     |Shortening                                                  |Yes                                                                                                                    |
     |Cm of shortening (0 - 99)                                   |4                                                                                                                      |
     |Review of systems, general                                  |Pain, Fever, Fatigue, Other, Weight Loss, Night Sweats                                                                 |
     |Description and duration of symptom (general)               |3 months                                                                                                               |
     |Other ROS general symptoms                                  |other                                                                                                                  |
     |Review of systems, cardiopulmonary                          |Chest Pain, Edema, Cough, Angina, Shortness Of Breath, Other                                                           |
     |Description and duration of symptom (cardiopulmonary)       |2 months                                                                                                               |
     |Other ROS cardiopulmonary symptoms                          |other                                                                                                                  |
     |Review of systems, gastrointestinal                         |Pain after meals, Black/Tarry Stool, Bloody Stool, Constipation, Other, Diarrhea, Vomiting, Nausea, Jaundice, Heartburn|
     |Description and duration of symptom (gastrointestinal)      |1 month                                                                                                                |
     |Other ROS gastrointestinal symptoms                         |other                                                                                                                  |
     |Review of systems, genitourinary                            |Hematuria, Hesitancy, Kidney Stones, Dysuria, Abnormal menses, Other, Incontinence                                     |
     |Description and duration of symptom (genitourinary)         |5 months                                                                                                               |
     |Other ROS genitourinary symptoms                            |other                                                                                                                  |
     |Review of systems, central nervous system                   |Paresthesia, Dizziness, Confusion, Headache, Focal Weakness, Other                                                     |
     |Description and duration of symptom (central nervous system)|4 months                                                                                                               |
     |Other ROS central nervous system symptoms                   |other                                                                                                                  |
     |Review of systems, HEENT                                    |Dysphagia, Dental Caries, Vision Difficulties, Difficulty Chewing, Other, Epistaxis, Decreased Hearing, Gum Bleeding   |
     |Description and duration of symptom (HEENT)                 |3 months                                                                                                               |
     |Other ROS HEENT symptoms                                    |other                                                                                                                  |
     |Review of systems, musculoskeletal                          |Other, Joint Swelling, Joint Pain, Generalized Weakness, Muscular Soreness, Joint Stiffness                            |
     |Description and duration of symptom (musculoskeletal)       |2 months                                                                                                               |
     |Other ROS musculoskeletal symptoms                          |other                                                                                                                  |

* Verify following details of "Physical Examination" in Patient Dashboard 

     |FIELD                           |VALUE                                                                                                                                                                               |
     |--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
     |General examination             |Well developed female / male in no acute distress                                                                                                                                   |
     |HEENT examination               |Pupils equal, regular, reactive to light and accomodation, normal extraocular muscles, normocephalic, normal dentition, clear throat, normal neck motion, no jugular vien distension|
     |Chest examination               |Clear lung bilaterally to auscultation and percussion, normal chest wall motion                                                                                                     |
     |Heart examination               |Normal S1 & S2, no murmurs, intact pulses                                                                                                                                           |
     |Abdomen examination             |Soft, no hepatosplenomegaly, no tenderness, no mass                                                                                                                                 |
     |Rectal and genitalia examination|Deferred                                                                                                                                                                            |
     |Extremities examination         |No clubbing, cyanosis or edema, normal joints with full range of motion                                                                                                             |
     |Neurologic examination          |Cranial nerves intact, normal muscular deep tendon reflexes, sensation intact throughout, muscle power intact, gait intact, mental status intact                                    |

Surgeon and Anaesthetist - Surgical Diagnoses and Surgeon Pre-Op Assessment and Treatment plan and Anesthesia Initial Assessment form
-------------------------------------------------------------------------------------------------------------------------------------

* On the login page
* Login with user "ashraf_n" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Sara" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Verify "Surgeon Pre-Op Assessment and Treatment Plan" is added to the left pane
* Verify "Surgical Diagnoses" is added to the left pane
* Select template "Surgeon Pre-Op Assessment and Treatment Plan" from observation page and fill details 

     |FIELD                                   |VALUE                                                                                          |
     |----------------------------------------|-----------------------------------------------------------------------------------------------|
     |Date of consultation                    |05/05/2017                                                                                     |
     |Site of injury                          |Site, Shoulder                                                                                 |
     |Side of injury                          |Right                                                                                          |
     |Condition of soft tissue at presentation|Bad (need soft tissue coverage)                                                                |
     |Associated neural injury                |Yes                                                                                            |
     |Comments (neural injury)                |comments                                                                                       |
     |Associated vascular injury              |Yes                                                                                            |
     |Is patient for surgery                  |Yes                                                                                            |
     |Has Patient Consent Been Obtained?      |Yes                                                                                            |
     |Surgical summary                        |surgery summary comment                                                                        |
     |Planned Procedure (surgical)            |Debridement of bone                                                                            |
     |Est Hours (Hrs)                         |1                                                                                              |
     |Est Minutes (Mins)                      |20                                                                                             |
     |Initial general plan                    |Needs Physio / Other consultation                                                              |
     |Objectives of physiotherapy             |physio comments                                                                                |
     |Surgical objective                      |Repair anatomy;Prevent future problems;Uncertain;Replace the loss of;Manage long-term pathology|
     |Side of surgical objective              |Left;Right                                                                                     |
     |Site of surgical objective              |Site, Nose                                                                                     |
     |Comments of uncertainty                 |uncertainty comments                                                                           |
     |Comments about surgical objectives      |comments                                                                                       |
     |Frequency of Operations                 |Multiple Operations (+2)                                                                       |
     |Estimated number of surgeries           |3                                                                                              |
     |Sites (donor areas excluded)            |Multi-site, different surgery                                                                  |
     |Spacing between surgeries               |2                                                                                              |
     |Estimated length of stay                |30-60 days                                                                                     |
     |Does the patient need further admissions|Yes                                                                                            |
     |Investigations needed                   |MRI;CBC;EMG & NCS;CRP;X-ray;CT scan;Swab for c/s                                               |
     |Need consultations                      |Maxillo-facial;Orthopedic;Other;Plastic                                                        |
     |Other consultation needed               |other comments                                                                                 |

* Select template "Surgical Diagnoses" from observation page and fill details 

     |FIELD             |VALUE            |
     |------------------|-----------------|
     |Surgical Diagnosis|Deformity of nose|
     |Site              |Site, Nose       |
     |Side              |Right            |

* Select template "Medical Diagnoses" from observation page and fill details 

     |FIELD            |VALUE          |
     |-----------------|---------------|
     |Medical Diagnosis|Atherosclerosis|

* Select template "Anesthesia Initial Assessment" from observation page and fill details 

     |FIELD                                                                         |VALUE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
     |------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
     |Date of consultation                                                          |05/05/2017                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
     |Past medical history                                                          |None;Congenital lung disease;Cough or cold (present time);Sleep apnea;Asthma;Emphysema;Congential heart disease;History of hypertension;History of Rheumatic fever;History of valve disease;History of MI;History of palpitations;History of heart problems (within last six months);Congenital renal disease;History of renal infection;History of renal stones;History of renal failure;Diabetes;Thyroid hormone diseases;History of corticosteroid drugs;Congenital disorders of the nervous system;Epilepsy or seizure;History of CVA - TIA;Spinal cord disease;History of upper GI bleeding;History of jaundice;History of cirrhosis;History of hepatitis;History of blood disorder;History of anemia;History of frequent bleeding;Abnormal blood clotting;History of cancer;Other|
     |Past medical history, other                                                   |Other comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
     |Is the patient allergic to any drugs / medications ?                          |Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
     |Type of medication allergy                                                    |Dust allergy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
     |Previous Anaesthesia history                                                  |None;Local;General;Regional                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
     |Specify number of times receiving anaesthesia                                 |3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
     |Adverse reaction to anaesthesia                                               |None;Delayed recovery;Admission to ICU;Suffocation or cyanosis;Difficult intubation;Other                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
     |Comments about adverse reaction                                               |comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
     |Personal history of blood transfusion                                         |Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
     |Did an incident occur during previous blood transfusion                       |Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
     |Describe                                                                      |comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
     |Mallampati class                                                              |Class IV                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
     |Mouth opening                                                                 |5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
     |ASA score *                                                                   |ASA II                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
     |Planned anaesthesia technique                                                 |RSA;GAI;GAO                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
     |Does the patient need fiberoptic ?                                            |No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
     |Remarks-anaesthetist                                                          |remarks                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
     |Outcome of anaesthesia initial assessment                                     |Ready for surgery                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
     |Outcome of anaesthesia initial assessment, comments                           |anaes. comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
     |I discussed the risks and benefits of anaesthesia and answered all questions *|Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

* Save the consultation
* Navigate to patient dashboard
* Click on "Patient Summary" dashboard
* Verify following details of "Surgeon Pre-Op Assessment and Treatment Plan" in Patient Dashboard 

     |FIELD                                   |VALUE              |
     |----------------------------------------|-------------------|
     |Planned Procedure (surgical)            |Debridement of bone|
     |Estimated length of stay                |30-60 days         |
     |Does the patient need further admissions|Yes                |

* Verify following details of "Diagnoses" in Patient Dashboard 

     |FIELD             |VALUE            |
     |------------------|-----------------|
     |Surgical Diagnosis|Deformity of nose|
     |Site              |Nose             |
     |Side              |Right            |
     |Medical Diagnosis |Atherosclerosis  |

* Verify following details of "Orders" in Patient Dashboard 

     |FIELD                |VALUE                                                 |
     |---------------------|------------------------------------------------------|
     |Investigations needed|Swab for c/s, CT scan, X-ray, CRP, EMG & NCS, CBC, MRI|

R 3.1 forms - OPD Nursing Note, Nursing Needs - Ward, Ward Nursing Note, Surgical Ward Admission Nursing Assessment, Post-Op Ward Monitoring
--------------------------------------------------------------------------------------------------------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Sara" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
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
     |Site of pain                            |Site, Face |
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
* Select template "Nursing Needs - Ward" from observation page and fill details 

     |FIELD                    |VALUE                                                   |
     |-------------------------|--------------------------------------------------------|
     |Date recorded            |06/06/2016                                              |
     |Draining wound(s)?       |Yes                                                     |
     |IV/IM needed?            |IV Antibiotics;PICC line;IM Narcotics;IV Narcotics;Other|
     |Twice daily Physiotherapy|No                                                      |
     |Non-ambulatory?          |Yes                                                     |
     |Special needs?           |Yes                                                     |
     |Injection (subcutaneous)?|Insulin;DVT Prophylaxis;Other                           |

* Verify "Nursing Needs - Ward" is added to the left pane
* Select template "Ward Nursing Note" from observation page and fill details 

     |FIELD                                   |VALUE      |
     |----------------------------------------|-----------|
     |Date recorded                           |05/05/2017 |
     |Pain Severity                           |1          |
     |Side of pain                            |Right      |
     |Site of pain                            |Site, Hand |
     |Type of pain                            |severe     |
     |When does the pain occur                |always     |
     |Does the patient have a drain?          |Yes        |
     |Side of drain                           |Left       |
     |Site of drain                           |Site, Arm  |
     |Drainage                                |1000       |
     |Total quantity evacuated from the drain |10         |
     |Change Position                         |Done       |
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
     |Site of pain                                          |Site, Leg                                                                                                                  |
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
     |Site of pain                     |Site, Leg            |
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
* Save the consultation
* Verify these forms are saved and disabled to add 

     |FORM                                      |
     |------------------------------------------|
     |OPD Nursing Note                          |
     |Ward Nursing Note                         |
     |Surgical Ward Admission Nursing Assessment|
     |Nursing Needs - Ward                      |

* Navigate to patient dashboard
* Click on "Patient Summary" dashboard
* Verify following details of "OPD Nursing Note" in Patient Dashboard 

     |FIELD                                   |VALUE           |
     |----------------------------------------|----------------|
     |Date recorded                           |05 May 17       |
     |Temperature                             |32C             |
     |Pulse                                   |77bpm           |
     |Respiratory rate                        |85breaths/minute|
     |Systolic blood pressure                 |120mmHg         |
     |Diastolic blood pressure                |80mmHg          |
     |Pain Severity                           |1               |
     |Side of pain                            |Right           |
     |Site of pain                            |Face            |
     |Type of pain                            |severe          |
     |When does the pain occur                |always          |
     |Does the patient have a dressing?       |Yes             |
     |Side of dressing                        |Right           |
     |Site of dressing                        |Femur           |
     |Description of wound                    |Other           |
     |Description of wound, other             |wet wound       |
     |Dressing, comments                      |dressed         |
     |Does the patient have a tissue expander?|Yes             |
     |Site of tissue expander                 |Leg             |
     |Quantity injected                       |1cc             |
     |Quantity withdrawn                      |2cc             |
     |Total volume in tissue expander         |3cc             |
     |Condition of tissue expander            |normal          |
     |Nursing consultation notes              |recorded        |

* Verify following details of "Ward Nursing Note" in Patient Dashboard 

     |FIELD                                   |VALUE    |
     |----------------------------------------|---------|
     |Date recorded                           |05 May 17|
     |Pain Severity                           |1        |
     |Side of pain                            |Right    |
     |Site of pain                            |Hand     |
     |Type of pain                            |severe   |
     |When does the pain occur                |always   |
     |Does the patient have a drain?          |Yes      |
     |Side of drain                           |Left     |
     |Site of drain                           |Arm      |
     |Drainage                                |1000     |
     |Total quantity evacuated from the drain |10       |
     |Change Position                         |Done     |
     |Does the patient have a dressing?       |Yes      |
     |Side of dressing                        |Right    |
     |Site of dressing                        |Iliac    |
     |Description of wound                    |Other    |
     |Description of wound, other             |wet wound|
     |Dressing, comments                      |dressed  |
     |Does the patient have a peripheral line?|Yes      |
     |Site of peripheral line                 |Wrist    |
     |Date of insertion, peripheral line      |05 May 17|
     |Date of removal, peripheral line        |07 Jul 17|
     |Comments, peripheral line               |comments |
     |Does the patient have a PICC line?      |Yes      |
     |Date of insertion, PICC line            |05 May 17|
     |Date of dressing                        |05 May 17|
     |Comments, dressing PICC line            |comments |
     |Date of removal, PICC line              |08 Aug 17|
     |Does the patient have a Foley catheter? |No       |
     |Does the patient have a tissue expander?|Yes      |
     |Site of tissue expander                 |Toe      |
     |Quantity injected                       |1cc      |
     |Quantity withdrawn                      |2cc      |
     |Total volume in tissue expander         |3cc      |
     |Condition of tissue expander            |no       |
     |Nursing consultation notes              |done     |
     |Blood sugar                             |Yes      |
     |RBS before meal                         |6        |
     |RBS after meal                          |7        |
     |FBS                                     |10       |
     |Insulin given                           |Yes      |
     |How much insulin given                  |15       |

* Verify following details of "Surgical Ward Assessment" in Patient Dashboard 

     |FIELD                                                 |VALUE                                                                                                                              |
     |------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
     |Date recorded                                         |05 May 17                                                                                                                          |
     |Reason for admission                                  |Other                                                                                                                              |
     |Reason for admission, other                           |Physio                                                                                                                             |
     |Pain Severity                                         |1                                                                                                                                  |
     |Side of pain                                          |Right                                                                                                                              |
     |Site of pain                                          |Leg                                                                                                                                |
     |Type of pain                                          |severe                                                                                                                             |
     |When does the pain occur                              |always                                                                                                                             |
     |Patient mood                                          |Other                                                                                                                              |
     |Patient mood, other                                   |Excited                                                                                                                            |
     |Does the patient have suicidal or depressive thoughts?|No                                                                                                                                 |
     |Number of wounds                                      |4                                                                                                                                  |
     |Description                                           |Wound needs dressing                                                                                                               |
     |Nutritional Assessment                                |High protein, Diabetic diet, Regular, Low salt, Other                                                                              |
     |Nutritional Assessment, other                         |Bitter                                                                                                                             |
     |Admission Nursing Notes                               |Admit by tomorrow morning                                                                                                          |
     |Orientation of the patient                            |Meal time, Sleeping time, Smoking, Environment, Isolation instructions, General Hygiene, Medication, Discharge plan, Visiting hours|

* Verify following details of "Post-Op Ward Monitoring" in Patient Dashboard 

     |FIELD                         |VALUE                |
     |------------------------------|---------------------|
     |Date recorded                 |05 May 17            |
     |Consciousness                 |Awake                |
     |Oxygen                        |80L/min              |
     |Blood oxygen saturation       |56%                  |
     |Respiration rate              |85breaths/minute     |
     |Pulse                         |77bpm                |
     |Systolic blood pressure       |120mmHg              |
     |Diastolic blood pressure      |80mmHg               |
     |Temperature                   |32C                  |
     |Pain Severity                 |1                    |
     |Side of pain                  |Right                |
     |Site of pain                  |Leg                  |
     |Type of pain                  |severe               |
     |When does the pain occur      |always               |
     |Nausea                        |Yes                  |
     |Vomiting                      |No                   |
     |Side of dressing              |Right                |
     |Site of dressing              |Iliac                |
     |Description of wound          |Other                |
     |Description of wound, other   |fresh since one month|
     |Urine                         |Yes                  |
     |Does the patient have a drain?|Yes                  |
     |Side of drain                 |Left                 |
     |Site of drain                 |Toe                  |
     |Drainage                      |2000                 |
     |Patient Position              |sitting              |

R 3.2 forms - Surgeon Follow-up, Operative Report, OPD MD Follow-Up Note
------------------------------------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Sara" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Surgeon Follow-up" from observation page and fill details 

     |FIELD                             |VALUE                                        |
     |----------------------------------|---------------------------------------------|
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
* Select template "OPD MD Follow-Up Note" from observation page and fill details 

     |FIELD                     |VALUE                                                                                         |
     |--------------------------|----------------------------------------------------------------------------------------------|
     |Chief complaint           |Pain;Diabetes;Hypertension;URI symptoms;Heartburn;N/V, Diarrhea;Rash;Cough;Poor appetite;Other|
     |Other chief complaint     |New other complaint                                                                           |
     |History of present illness|No improvement                                                                                |
     |Allergies                 |New allergies                                                                                 |
     |Current plan              |Physio bone lengthening;Physio Other;Antibiotics;Dressings;Neuropathic pain clinic;None       |
     |Impression                |New impression                                                                                |
     |Plan                      |New plan                                                                                      |

* Verify "OPD MD Follow-Up Note" is added to the left pane
* Save the consultation
* Verify these forms are saved and disabled to add 

     |FORM                 |
     |---------------------|
     |Surgeon Follow-up    |
     |Operative Report     |
     |OPD MD Follow-Up Note|

* Navigate to patient dashboard
* Click on "Patient Summary" dashboard
* Verify following details of "Surgeon Follow-up" in Patient Dashboard 

     |FIELD                             |VALUE                                        |
     |----------------------------------|---------------------------------------------|
     |Early Follow-up                   |Complications developed                      |
     |Impact of complication            |Did not effect the results of flow           |
     |Patient requires amputation       |Yes                                          |
     |Is patient for surgery            |Yes                                          |
     |Has patient consent been obtained?|Yes                                          |
     |Planned Procedure (surgical)      |Dental extraction                            |
     |Side of surgical procedure        |Left                                         |
     |Est Hours (0 - 23)                |1Hrs                                         |
     |Est Minutes (0 - 59)              |30Mins                                       |
     |Surgical summary                  |need periodic monitoring of patient condition|

* Verify following details of "Operative Report" in Patient Dashboard 

     |FIELD                         |VALUE                                                                                                                                                                       |
     |------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
     |Surgeon                       |Dr. Rasheed Al Samerai, Dr. Hanna Janho, Dr. Sofian Al-Qassab, Dr. Ashraf Bustangi, Other, Dr. Ashraf Nabhan, Dr.Ghassan S. Abu-Sittah, Dr. Ali Al-Ani, Dr. Muckhaled Naseef|
     |Surgeon assistant             |Dr. Azeez                                                                                                                                                                   |
     |Anaesthetist                  |Dr. Ammar Subhi, Dr. Abdelraouf Alhamad, Dr. Hadeel Al-Ani, Other                                                                                                           |
     |Anaesthesia technician        |Dr. Hani                                                                                                                                                                    |
     |Type of anaesthesia           |RTA, RPX, INF, RAO, GAL, LOA, GAI, GAO, None, SED, RSA                                                                                                                      |
     |Scrub nurse                   |Nurse Hanna                                                                                                                                                                 |
     |Operation performed           |Quadricepsplasty                                                                                                                                                            |
     |Size of tissue expander       |2                                                                                                                                                                           |
     |Side of operation             |Right                                                                                                                                                                       |
     |Findings                      |New findings                                                                                                                                                                |
     |Operation details             |operation successful                                                                                                                                                        |
     |Does the patient have a drain?|Yes                                                                                                                                                                         |
     |Side of drain                 |Left                                                                                                                                                                        |
     |Site of drain                 |Leg                                                                                                                                                                         |
     |Type of drain inserted        |Vacuum drain                                                                                                                                                                |
     |Specimen sent to lab          |Yes                                                                                                                                                                         |
     |Estimated blood loss          |6                                                                                                                                                                           |
     |Blood transfusion             |Yes                                                                                                                                                                         |
     |Number of units               |7                                                                                                                                                                           |

* Verify following details of "OPD MD Follow-Up Note" in Patient Dashboard 

     |FIELD                     |VALUE                                                                                                  |
     |--------------------------|-------------------------------------------------------------------------------------------------------|
     |Chief complaint           |URI symptoms, Cough, Heartburn, Pain, Other, Poor appetite, Rash, N/V, Diarrhea, Hypertension, Diabetes|
     |Other chief complaint     |New other complaint                                                                                    |
     |History of present illness|No improvement                                                                                         |
     |Allergies                 |New allergies                                                                                          |
     |Current plan              |Neuropathic pain clinic, Physio bone lengthening, Physio Other, Dressings, None, Antibiotics           |
     |Impression                |New impression                                                                                         |
     |Plan                      |New plan                                                                                               |


R 3.3 form - Vital Signs
------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Search and select patient "Sara" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Vital Signs" from observation page and fill details 

     |FIELD                            |VALUE|
     |---------------------------------|-----|
     |Temperature (C)                  |32   |
     |Pulse (bpm)                      |77   |
     |Respiratory rate (breaths/minute)|85   |
     |Systolic blood pressure (mmHg)   |120  |
     |Diastolic blood pressure (mmHg)  |80   |
     |Blood oxygen saturation (%)      |56   |
     |Blood glucose (mg/dl)            |59   |

* Save the consultation
