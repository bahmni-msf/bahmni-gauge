Patient Summary Dashboard and Observation Forms
===============================================
Created by jaseena, swarup on 2/16/17

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

Create Patient Via Api for Patient Summary Dashboard Display Verification
-------------------------------------------------------------------------
* Create patient "Niya" using API with "Hospital" visit
* Enroll patient to reconstructive surgery program using API

OPD Nurse - Baseline Vital Signs, Social and Medical History forms
------------------------------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_OPD_USER" and password "BAHMNI_GAUGE_OPD_PASSWORD" with location "BAHMNI_GAUGE_OPD_LOCATION"
* Click on programs app
* Search and select patient "Niya" from "Programs" queue
* Edit "Reconstructive Surgery" Program with following details 

     |programStatus|
     |-------------|
     |Pre-Operative|

* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Verify "Baseline Vital Signs" is added to the left pane
* Verify "Social and Medical History" is added to the left pane
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

* Select template "Social and Medical History" from observation page and fill details 

     |FIELD                         |VALUE                    |
     |------------------------------|-------------------------|
     |Date of consultation          |01/01/2017               |
     |Marital status                |Single                   |
     |Highest education level       |No formal education      |
     |Pregnancy status              |No                       |
     |Current smoker                |Yes                      |
     |Number of cigarettes per day  |1                        |
     |Duration of smoking (in years)|2                        |
     |Drug and Alcohol use          |Never                    |
     |Medical History               |Hypertension;Tuberculosis|
     |Other medical problems        |HIV                      |
     |History of Allergy            |Drugs;Food               |
     |Comments about allergy        |Nothing                  |
     |Currently taking medication   |Yes                      |
     |Type of medication            |Some drug                |
     |Dose and freqency             |daily                    |
     |Date of last dose             |01/01/2017               |
     |Pain severity                 |2                        |
     |Side of pain                  |Right                    |
     |Site of pain                  |Arm                      |
     |Number of wounds              |2                        |
     |Site                          |Ear;Nose                 |
     |Description                   |None                     |
     |Nursing notes                 |captured                 |

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

     |FIELD                         |VALUE                     |
     |------------------------------|--------------------------|
     |Date of consultation          |01 Jan 17                 |
     |Marital status                |Single                    |
     |Highest education level       |No formal education       |
     |Pregnancy status              |No                        |
     |Current smoker                |Yes                       |
     |Number of cigarettes per day  |1                         |
     |Duration of smoking (in years)|2                         |
     |Drug and Alcohol use          |Never                     |
     |Medical History               |Tuberculosis, Hypertension|
     |Other medical problems        |HIV                       |
     |History of Allergy            |Food, Drugs               |
     |Comments about allergy        |Nothing                   |
     |Currently taking medication   |Yes                       |
     |Type of medication            |Some drug                 |
     |Dose and freqency             |daily                     |
     |Date of last dose             |01 Jan 17                 |
     |Pain severity (0 - 10)        |2                         |
     |Side of pain                  |Right                     |
     |Site of pain                  |Arm                       |
     |Number of wounds              |2                         |
     |Site                          |Nose, Ear                 |
     |Description                   |None                      |
     |Nursing notes                 |captured                  |

MD - MD Initial Assessment, Physical Examination and Medical Diagnoses forms
----------------------------------------------------------------------------
* On the login page
* Login with user "zaid_se" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Niya" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Verify "MD Initial Assessment" is added to the left pane
* Verify "Physical Examination" is added to the left pane
* Verify "Medical Diagnoses" is added to the left pane
* Select template "MD Initial Assessment" from observation page and fill details 

     |FIELD                                                       |VALUE                                                                                                         |
     |------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
     |Date of consultation                                        |05/16/2017                                                                                                    |
     |Chief complaint                                             |swollen leg                                                                                                   |
     |History of present illness                                  |6 months                                                                                                      |
     |Associated neural injury                                    |Yes                                                                                                           |
     |Comments (neural injury)                                    |comments                                                                                                      |
     |Associated vascular injury                                  |Yes                                                                                                           |
     |Comments (vascular injury)                                  |comments                                                                                                      |
     |Function of injured part                                    |Deformed, stiff                                                                                               |
     |Sensation of injured part                                   |Reduced (Regional)                                                                                            |
     |History of previous surgery                                 |Yes                                                                                                           |
     |Surgical procedures performed outside AMH                   |Debridement of bone                                                                                           |
     |Site of procedure                                           |Site, Leg                                                                                                     |
     |Side of procedure                                           |Right                                                                                                         |
     |Comment of procedure                                        |comments                                                                                                      |
     |Date of procedure                                           |05/01/2017                                                                                                    |
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
* Save the consultation
* Navigate to patient dashboard
* Click on "Patient Summary" dashboard
* Verify following details of "MD Initial Assessment" in Patient Dashboard 

     |FIELD                                                       |VALUE                                                                                                                  |
     |------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
     |Date of consultation                                        |16 May 17                                                                                                              |
     |Chief complaint                                             |swollen leg                                                                                                            |
     |History of present illness                                  |6 months                                                                                                               |
     |Associated neural injury                                    |Yes                                                                                                                    |
     |Comments (neural injury)                                    |comments                                                                                                               |
     |Associated vascular injury                                  |Yes                                                                                                                    |
     |Comments (vascular injury)                                  |comments                                                                                                               |
     |Function of injured part                                    |Deformed, stiff                                                                                                        |
     |Sensation of injured part                                   |Reduced (Regional)                                                                                                     |
     |History of previous surgery                                 |Yes                                                                                                                    |
     |Surgical procedures performed outside AMH                   |Debridement of bone                                                                                                    |
     |Site of procedure                                           |Leg                                                                                                                    |
     |Side of procedure                                           |Right                                                                                                                  |
     |Comment of procedure                                        |comments                                                                                                               |
     |Date of procedure                                           |01 May 17                                                                                                              |
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
     |Neurologic examination          |Cranial nerves intact, normal muscular deep tendon reflexes, normal strength, normal sensitivity                                                                                    |

Surgeon and Anaesthetist - Surgical Diagnoses and Surgeon Pre-Op Assessment & Tx plan and Anesthesia Initial Assessment form
----------------------------------------------------------------------------------------------------------------------------

* On the login page
* Login with user "ashraf_n" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Niya" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Verify "Surgeon Pre-Op Assessment & Tx Plan" is added to the left pane
* Verify "Surgical Diagnoses" is added to the left pane
* Select template "Surgeon Pre-Op Assessment & Tx Plan" from observation page and fill details 

     |FIELD                                   |VALUE                                                                                          |
     |----------------------------------------|-----------------------------------------------------------------------------------------------|
     |Date of consultation                    |05/17/2017                                                                                     |
     |Site of injury                          |Site, Shoulder                                                                                 |
     |Side of injury                          |Right                                                                                          |
     |Condition of soft tissue at presentation|Bad (need soft tissue coverage)                                                                |
     |Planned procedure                       |Debridement of bone                                                                            |
     |Side of surgical procedure              |Right                                                                                          |
     |Surgical summary                        |surgery comment                                                                                |
     |Initial general plan                    |Needs Physio / Other consultation                                                              |
     |Objectives of physiotherapy             |physio comments                                                                                |
     |Surgical objective                      |Repair anatomy;Prevent future problems;Uncertain;Replace the loss of;Manage long-term pathology|
     |Side of surgical objective              |Left;Right                                                                                     |
     |Site of surgical objective              |Site, Nose                                                                                     |
     |Comments of uncertainty                 |uncertainty comments                                                                           |
     |Comments about sugical objectives       |comments                                                                                       |
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

     |FIELD                                                                         |VALUE                       |
     |------------------------------------------------------------------------------|----------------------------|
     |Date of consultation                                                          |05/04/2017                  |
     |Previous Anaesthesia history                                                  |GAI;GAO                     |
     |Adverse reaction to anaesthesia                                               |Yes                         |
     |Comments about adverse reaction                                               |comments                    |
     |Personal history of blood transfusion                                         |Yes                         |
     |Did an incident occur during previous blood transfusion                       |Yes                         |
     |Describe                                                                      |comments                    |
     |Mallampati class                                                              |Class IV                    |
     |ASA score *                                                                   |ASA II                      |
     |Planned anaesthesia technique                                                 |RSA;GAI;GAO                 |
     |Remarks-anaesthetist                                                          |remarks                     |
     |Pre-anaesthesia orders                                                        |CRP;Electrolytes;KFT;CBC;LFT|
     |Outcome of anaesthesia initial assessment                                     |Ready for surgery           |
     |I discussed the risks and benefits of anaesthesia and answered all questions *|Yes                         |

* Save the consultation
* Navigate to patient dashboard
* Click on "Patient Summary" dashboard
* Verify following details of "Surgeon Pre-Op Assessment and Treatment Plan" in Patient Dashboard 

     |FIELD                                   |VALUE              |
     |----------------------------------------|-------------------|
     |Planned procedure                       |Debridement of bone|
     |Side of surgical procedure              |Right              |
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

     |FIELD                 |VALUE                                                 |
     |----------------------|------------------------------------------------------|
     |Pre-anaesthesia orders|LFT, CBC, KFT, Electrolytes, CRP                      |
     |Investigations needed |Swab for c/s, CT scan, X-ray, CRP, EMG & NCS, CBC, MRI|

Other Observation Forms - OPD Nursing Note, Ward Nursing Note, Surgical Ward Admission Nursing Assessment
---------------------------------------------------------------------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Niya" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "OPD Nursing Note" from observation page and fill details 

     |FIELD                                   |VALUE     |
     |----------------------------------------|----------|
     |Date recorded                           |05/11/2017|
     |Temperature (C)                         |32        |
     |Pulse (bpm)                             |77        |
     |Respiratory rate (breaths/minute)       |85        |
     |Systolic blood pressure (mmHg)          |120       |
     |Diastolic blood pressure (mmHg)         |80        |
     |Pain Severity                           |1         |
     |Side of pain                            |Right     |
     |Site of pain                            |Site, Face|
     |Type of pain                            |severe    |
     |When does the pain occur                |always    |
     |Does the patient have a dressing?       |Yes       |
     |Side of dressing                        |Right     |
     |Site of dressing                        |Site, Ear |
     |Description of wound                    |Other     |
     |Description of wound, other             |wet wound |
     |Dressing, comments                      |dressed   |
     |Does the patient have a tissue expander?|Yes       |
     |Site of tissue expander                 |Site, Leg |
     |Quantity injected                       |1         |
     |Quantity withdrawn                      |2         |
     |Total volume in tissue expander         |3         |
     |Condition of tissue expander            |normal    |
     |Nursing consultation notes              |recorded  |

* Verify "OPD Nursing Note" is added to the left pane
* Select template "Ward Nursing Note" from observation page and fill details 

     |FIELD                                   |VALUE       |
     |----------------------------------------|------------|
     |Date recorded                           |05/10/2017  |
     |Temperature (C)                         |32          |
     |Pulse (bpm)                             |77          |
     |Respiratory rate (breaths/minute)       |85          |
     |Systolic blood pressure (mmHg)          |120         |
     |Diastolic blood pressure (mmHg)         |80          |
     |Pain Severity                           |1           |
     |Side of pain                            |Right       |
     |Site of pain                            |Site, Hand  |
     |Type of pain                            |severe      |
     |When does the pain occur                |always      |
     |Does the patient have a drain?          |Yes         |
     |Side of drain                           |Left        |
     |Site of drain                           |Site, Arm   |
     |Drainage                                |1000        |
     |Change Position                         |Done        |
     |Does the patient have a dressing?       |Yes         |
     |Side of dressing                        |Right       |
     |Site of dressing                        |Site, Finger|
     |Description of wound                    |Other       |
     |Description of wound, other             |wet wound   |
     |Dressing, comments                      |dressed     |
     |Does the patient have a peripheral line?|Yes         |
     |Site of peripheral line                 |Site, Wrist |
     |Date of insertion, peripheral line      |05/10/2017  |
     |Date of removal, peripheral line        |07/10/2017  |
     |Comments, peripheral line               |comments    |
     |Does the patient have a PICC line?      |Yes         |
     |Date of insertion, PICC line            |05/10/2017  |
     |Date of dressing                        |05/10/2017  |
     |Comments, dressing PICC line            |comments    |
     |Date of removal, PICC line              |08/10/2017  |
     |Does the patient have a tissue expander?|Yes         |
     |Site of tissue expander                 |Site, Toe   |
     |Quanity injected                        |1           |
     |Quantity withdrawn                      |2           |
     |Total volume in tissue expander         |3           |
     |Condition of tissue expander            |no          |
     |Nursing consultation notes              |done        |

* Verify "Ward Nursing Note" is added to the left pane
* Select template "Surgical Ward Admission Nursing Assessment" from observation page and fill details 

     |FIELD                                                 |VALUE                                                                                                                      |
     |------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
     |Date recorded                                         |05/11/2017                                                                                                                 |
     |Reason for admission                                  |Other                                                                                                                      |
     |Reason for admission, other                           |Physio                                                                                                                     |
     |Temperature (C)                                       |32                                                                                                                         |
     |Pulse (bpm)                                           |77                                                                                                                         |
     |Respiratory rate (breaths/minute)                     |85                                                                                                                         |
     |Systolic blood pressure (mmHg)                        |120                                                                                                                        |
     |Diastolic blood pressure (mmHg)                       |80                                                                                                                         |
     |Blood oxygen saturation (%)                           |56                                                                                                                         |
     |Blood glucose (mg/dl)                                 |59                                                                                                                         |
     |Pain Severity                                         |1                                                                                                                          |
     |Side of pain                                          |Right                                                                                                                      |
     |Site of pain                                          |Site, Leg                                                                                                                  |
     |Type of pain                                          |severe                                                                                                                     |
     |When does the pain occur                              |always                                                                                                                     |
     |Patient mood                                          |Other                                                                                                                      |
     |Patient mood, other                                   |Excited                                                                                                                    |
     |Does the patient have suicidal or depressive thoughts?|No                                                                                                                         |
     |Number of wounds                                      |4                                                                                                                          |
     |Description                                           |Wound needs dressing                                                                                                       |
     |Nutritional Assessment                                |Regular;Low salt;High protein;Diabetic diet;Other                                                                          |
     |Nutritional Assessment, other                         |Bitter                                                                                                                     |
     |Admission Nursing Notes                               |Admit by tomorrow morning                                                                                                  |
     |Orientation of the patient                            |Environment;General Hygiene;Medication;Visiting hours;Isolation instructions;Sleeping time;Meal time;Smoking;Discharge plan|

* Verify "Surgical Ward Admission Nursing Assessment" is added to the left pane
* Save the consultation
* Verify these forms are saved and disabled to add 

     |FORM                                      |
     |------------------------------------------|
     |OPD Nursing Note                          |
     |Ward Nursing Note                         |
     |Surgical Ward Admission Nursing Assessment|
