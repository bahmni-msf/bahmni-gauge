Patient Summary Dashboard and Observation Forms
===============================================
Created by jaseena, swarup on 2/16/17

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

Enter data in observation forms and verify Patient Summary Dashboard
--------------------------------------------------------------------
Verify the Patient Summary Dashboard display controls

tags: sanity, regression

* Create patient "Patient Summary Dashboard" using API with "Hospital" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_OPD_USER" and password "BAHMNI_GAUGE_OPD_PASSWORD" with location "BAHMNI_GAUGE_OPD_LOCATION"
* Click on programs app
* Select patient "Patient Summary Dashboard" in tab "All"
* Edit "Reconstructive Surgery" Program with following details 

   |programStatus|
   |-------------|
   |Pre-Operative|

* Navigate to "Reconstructive Surgery" program dashboard
* Click on "Patient Summary" dashboard
* Verify the dashboard name is "Patient Summary"
* Verify the following display controls are visible 

   |Display Control Title                |
   |-------------------------------------|
   |Patient Information                  |
   |Medical History                      |
   |Past Medical History (Before Arrival)|
   |Social History                       |
   |Review of Systems                    |
   |Physical Examination                 |
   |Final Diagnoses                      |
   |Operative Course in Amman            |
   |Post Operative Anaesthesia Course    |
   |Pain Management                      |
   |Medications Administered in Amman RSP|
   |Medical Course                       |
   |Psycho Social Course                 |
   |Surgical Follow-up Plan              |
   |Physiotherapy Follow-up Plan         |
   |Medical Follow-up Plan               |
   |Appointments                         |
   |Microbiology Results                 |

* Navigate to consultation
* Select template "First Stage Validation" from observation page and fill details 

   |FIELD    |VALUE     |
   |---------|----------|
   |Specialty|Orthopedic|
   |Stage    |2         |

* Select template "Final Validation" from observation page and fill details 

   |FIELD            |VALUE                   |
   |-----------------|------------------------|
   |Name of Surgeon 1|Dr. Ashraf Nabhan       |
   |Name of Surgeon 2|Dr.Ghassan S. Abu-Sittah|

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

* Select template "Anesthesia Initial Assessment" from observation page and fill details 

   |FIELD                                                                         |VALUE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   |------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   |Date of consultation                                                          |05/05/2017                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   |Past medical history                                                          |None;Congenital lung disease;Cough or cold (present time);Sleep apnea;Asthma;Emphysema;Congenital heart disease;History of hypertension;History of Rheumatic fever;History of valve disease;History of MI;History of palpitations;History of heart problems (within last six months);Congenital renal disease;History of renal infection;History of renal stones;History of renal failure;Diabetes;Thyroid hormone diseases;History of corticosteroid drugs;Congenital disorders of the nervous system;Epilepsy or seizure;History of CVA - TIA;Spinal cord disease;History of upper GI bleeding;History of jaundice;History of cirrhosis;History of hepatitis;History of blood disorder;History of anemia;History of frequent bleeding;Abnormal blood clotting;History of cancer;Other|
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

* Select template "Health Education" from observation page and fill details 

   |FIELD                                          |VALUE              |
   |-----------------------------------------------|-------------------|
   |Date of consultation                           |01/01/2017         |
   |Marital status                                 |Single             |
   |Highest education level                        |No formal education|
   |Pregnancy status                               |No                 |
   |Current smoker                                 |Yes                |
   |Number of cigarettes per day                   |1                  |
   |Duration of smoking (in years)                 |2                  |
   |Drug and Alcohol use                           |Never              |
   |External devices, present                      |Big tube;Other     |
   |Other type of external device                  |Some device        |
   |Nutritional Assessment                         |Regular            |
   |Personal hygiene (presence of head lice / bugs)|No                 |
   |Education learning needs                       |Yes                |
   |Referral care plan                             |No care plan       |

* Select template "Physical Examination" from the Observation Page

* Select template "Surgical Diagnoses" from observation page and fill details 

   |FIELD             |VALUE            |
   |------------------|-----------------|
   |Surgical Diagnosis|Deformity of nose|
   |Side              |Right            |

* Select template "Medical Diagnoses" from observation page and fill details 

   |FIELD            |VALUE          |
   |-----------------|---------------|
   |Medical Diagnosis|Atherosclerosis|

* Select template "Psycho-Social Assessment" from observation page and fill details 

   |FIELD                                                             |VALUE                                                                                 |
   |------------------------------------------------------------------|--------------------------------------------------------------------------------------|
   |Date of consultation                                              |05/05/2017                                                                            |
   |Future expectations about care plan                               |Different from medical plan                                                           |
   |Comments about expectations                                       |care plan comments                                                                    |
   |Past history of psychological or counselling care for patient     |No                                                                                    |
   |Past history of psychological or counselling care of family member|Yes                                                                                   |
   |By who (NGO / private)                                            |NGO                                                                                   |
   |Past history of psychiatric care for patient                      |Unknown                                                                               |
   |Past history of psychiatric care of family member                 |No                                                                                    |
   |History of psychotropic drugs                                     |Yes                                                                                   |
   |Drug                                                              |drug details                                                                          |
   |SRQ20                                                             |20                                                                                    |
   |PTSD (score)                                                      |4                                                                                     |
   |PSYca 3-6 (child)                                                 |44                                                                                    |
   |SDQ P7-10                                                         |8                                                                                     |
   |SDQ S11-17                                                        |16                                                                                    |
   |Needed Mental Health Support                                      |Followed daily by counselor;Referred to clinical psychologist;Referred to psychiatrist|
   |Comments from counsellor                                          |counsellor comments                                                                   |

* Select template "Psycho-Social Assessment" from observation page and fill details in "Discharge Assessment" section 

   |FIELD                                    |VALUE                                                 |
   |-----------------------------------------|------------------------------------------------------|
   |SRQ20                                    |10                                                    |
   |PTSD (score)                             |3                                                     |
   |PSYca 3-6 (child)                        |30                                                    |
   |SDQ P7-10                                |22                                                    |
   |SDQ S11-17                               |13                                                    |
   |Psychosocial overview and comments       |Comments for Psychosocial overview and comments       |
   |Social needs or other referrals          |Comments for Social needs or other referrals          |
   |Specific comments regarding the caretaker|Comments for Specific comments regarding the caretaker|

* Select template "Complications" from observation page and fill details 

   |FIELD                                      |VALUE                                                                                    |
   |-------------------------------------------|-----------------------------------------------------------------------------------------|
   |Patient complication                       |Anaesthetic complication in OT                                                           |
   |Start date of complication                 |12/12/2016                                                                               |
   |Anaesthetic complication in OT, description|Hypoxia;Severe nausea and vomiting;Hypotension;Spinal headache;Aspiration;Pneumonia;Other|
   |Outcome of complication                    |Resolved                                                                                 |
   |End date of complication                   |02/02/2017                                                                               |

* Save the consultation
* Verify these forms are saved and disabled to add 

   |FORM                         |
   |-----------------------------|
   |Health Education             |
   |Patient History              |
   |First Stage Validation       |
   |Final Validation             |
   |Anesthesia Initial Assessment|
   |Psycho-Social Assessment     |
   |MD Initial Assessment        |
   |Physical Examination         |
   |Surgical Diagnoses           |
   |Medical Diagnoses            |

* Verify this form is Add More form "Complications"
* Navigate to patient dashboard
* Verify the dashboard name is "Patient Summary"
* Verify following details of "Patient Information" in Patient Dashboard 

   |FIELD            |VALUE            |
   |-----------------|-----------------|
   |Name of Surgeon 1|Dr. Ashraf Nabhan|
   |Stage            |2                |
   |Specialty        |Orthopedic       |

* Verify following details of "Medical History" in Patient Dashboard 

   |FIELD                                               |VALUE       |
   |----------------------------------------------------|------------|
   |Date of injury                                      |05 May 16   |
   |Cause of injury                                     |Burns       |
   |Reason for admission to program                     |swollen leg |
   |History of Allergy                                  |Food, Drugs |
   |Comments about allergy                              |Nothing     |
   |Is the patient allergic to any drugs / medications ?|Yes         |
   |Type of medication allergy                          |Dust allergy|
   |History of present illness                          |6 months    |

* Verify following details of "Past Medical History (Before Arrival)" in Patient Dashboard 

   |FIELD                                                  |VALUE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   |-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   |Past medical history                                   |History of valve disease, History of upper GI bleeding, History of hepatitis, Sleep apnea, History of cirrhosis, History of heart problems (within last six months), History of renal stones, None, Epilepsy  or seizure, Other, History of jaundice, Emphysema, Congenital lung disease, History of Rheumatic fever, History of renal infection, Abnormal blood clotting, History of CVA - TIA, History of cancer, History of frequent bleeding, Congenital disorders of the nervous system, Congenital heart disease, Diabetes, History of blood disorder, Cough or cold (present time), History of anemia, History of MI, History of corticosteroid drugs, Asthma, History of hypertension, History of renal failure, Spinal cord disease, Thyroid hormone diseases, Congenital renal disease, History of palpitations|
   |Past medical history, other                            |Other comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   |Adverse reaction to anaesthesia                        |None, Other, Delayed recovery, Admission to ICU, Suffocation or cyanosis, Difficult intubation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   |Comments about adverse reaction                        |comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   |Did an incident occur during previous blood transfusion|Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   |Describe                                               |comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   |Medical History                                        |Tuberculosis, Hypertension                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   |Other medical problems                                 |HIV                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   |Currently taking medication                            |Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   |Type of medication                                     |Some drug                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   |Dose and frequency                                     |daily                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   |Date of last dose                                      |01 Jan 17                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   |History of previous surgery                            |Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   |Surgical procedures performed outside AMH              |Debridement of bone                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   |Side of procedure                                      |Right                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   |Comment of procedure                                   |comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   |Date of procedure                                      |01 Jan 17                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   |Type of previous fixation                              |External, Internal, Other                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   |Type of internal fixation                              |Wires, Plate, Screws, Intramedullary nails                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   |Duration of External fixation                          |Less than 6 months                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   |Other type of fixation                                 |other comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   |History of infection                                   |Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   |Comments about previous infection                      |comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   |Discharging sinus                                      |Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   |Duration of discharging sinus                          |Less than 6 months                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   |Bone Loss                                              |Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   |Cm of bone loss (0 - 99)                               |4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   |United fracture                                        |Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   |Shortening                                             |Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   |Cm of shortening (0 - 99)                              |4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

* Verify following details of "Social History" in Patient Dashboard 

   |FIELD                         |VALUE              |
   |------------------------------|-------------------|
   |Highest education level       |No formal education|
   |Current smoker                |Yes                |
   |Number of cigarettes per day  |1                  |
   |Duration of smoking (in years)|2                  |
   |Drug and Alcohol use          |Never              |

* Verify following details of "Review of Systems" in Patient Dashboard 

   |FIELD                                                       |VALUE                                                                                                                  |
   |------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
   |Review of systems, general                                  |Weight Loss, Night Sweats, Other, Fever, Pain, Fatigue                                                                 |
   |Description and duration of symptom (general)               |3 months                                                                                                               |
   |Other ROS general symptoms                                  |other                                                                                                                  |
   |Review of systems, cardiopulmonary                          |Edema, Angina, Other, Cough, Chest Pain, Shortness Of Breath                                                           |
   |Description and duration of symptom (cardiopulmonary)       |2 months                                                                                                               |
   |Other ROS cardiopulmonary symptoms                          |other                                                                                                                  |
   |Review of systems, gastrointestinal                         |Vomiting, Jaundice, Bloody Stool, Other, Heartburn, Constipation, Black/Tarry Stool, Diarrhea, Pain after meals, Nausea|
   |Description and duration of symptom (gastrointestinal)      |1 month                                                                                                                |
   |Other ROS gastrointestinal symptoms                         |other                                                                                                                  |
   |Review of systems, genitourinary                            |Kidney Stones, Hematuria, Hesitancy, Dysuria, Abnormal menses, Other, Incontinence                                     |
   |Description and duration of symptom (genitourinary)         |5 months                                                                                                               |
   |Other ROS genitourinary symptoms                            |other                                                                                                                  |
   |Review of systems, central nervous system                   |Paresthesia, Headache, Other, Dizziness, Focal Weakness, Confusion                                                     |
   |Description and duration of symptom (central nervous system)|4 months                                                                                                               |
   |Other ROS central nervous system symptoms                   |other                                                                                                                  |
   |Review of systems, HEENT                                    |Decreased Hearing, Dental Caries, Gum Bleeding, Other, Difficulty Chewing, Epistaxis, Vision Difficulties, Dysphagia   |
   |Description and duration of symptom (HEENT)                 |3 months                                                                                                               |
   |Other ROS HEENT symptoms                                    |other                                                                                                                  |
   |Review of systems, musculoskeletal                          |Other, Joint Stiffness, Generalized Weakness, Muscular Soreness, Joint Swelling, Joint Pain                            |
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

* Verify following details of "Final Diagnoses" in Patient Dashboard 

   |FIELD             |VALUE            |
   |------------------|-----------------|
   |Surgical Diagnosis|Deformity of nose|
   |Side              |Right            |
   |Medical Diagnosis |Atherosclerosis  |

* Verify following details of "Post Operative Anaesthesia Course" in Patient Dashboard 

   |FIELD                     |VALUE                         |
   |--------------------------|------------------------------|
   |Patient complication      |Anaesthetic complication in OT|
   |Start date of complication|12 Dec 16                     |
   |Outcome of complication   |Resolved                      |
   |End date of complication  |02 Feb 17                     |


* Verify following details of "Psycho-Social Course" in Patient Dashboard 

   |FIELD                   |VALUE              |
   |------------------------|-------------------|
   |SRQ20 (< 20)            |20                 |
   |SRQ20 (< 20)            |10                 |
   |PTSD (score) (< 4)      |4                  |
   |PTSD (score) (< 4)      |3                  |
   |PSYca 3-6 (child) (< 44)|44                 |
   |PSYca 3-6 (child) (< 44)|30                 |
   |Comments from counsellor|counsellor comments|

