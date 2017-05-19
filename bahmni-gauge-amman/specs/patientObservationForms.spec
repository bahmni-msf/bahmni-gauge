Patient Observation Forms
=========================
Created by jaseena, swarup on 2/16/17

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
     
Baseline Vital Signs
--------------------
* Create patient "Niya" using API with "Hospital" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Niya" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Baseline Vital Signs" from observation page and fill details
| FIELD                             | VALUE      |
| Date recorded                     | 01/01/2017 |
| Weight (Kg)                       | 80         |
| Height (cm)                       | 90         |
| Respiratory rate (breaths/minute) | 2          |
| Temperature (C)                   | 36         |
| Pulse (bpm)                       | 8          |
| Blood oxygen saturation (%)       | 92         |

* Verify "Baseline Vital Signs" is added to the left pane
* Save the consultation
* Verify "Baseline Vital Signs" is disabled to add
* Navigate to patient dashboard
* Click on "Patient Summary" dashboard
* Verify following details of "Baseline Vital Signs" in Patient Dashboard
| FIELD                   | VALUE           |
| Date recorded           | 01 Jan 17       |
| Weight                  | 80Kg            |
| Height                  | 90cm            |
| BMI                     | 98.77Kg/m2      |
| Respiratory rate        | 2breaths/minute |
| Temperature             | 36C             |
| Pulse                   | 8bpm            |
| Blood oxygen saturation | 92%             |

Nursing Assessment - Social and Medical History
-----------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Niya" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Social and Medical History" from observation page and fill details
| FIELD                          | VALUE                     |
| Date of consultation           | 01/01/2017                |
| Marital status                 | Single                    |
| Highest education level        | No formal education       |
| Pregnancy status               | No                        |
| Current smoker                 | Yes                       |
| Number of cigarettes per day   | 1                         |
| Duration of smoking (in years) | 2                         |
| Drug and Alcohol use           | Never                     |
| Medical History                | Hypertension;Tuberculosis |
| Other medical problems         | HIV                       |
| History of Allergy             | Drugs;Food                |
| Comments about allergy         | Nothing                   |
| Currently taking medication    | Yes                       |
| Type of medication             | Some drug                 |
| Dose and freqency              | daily                     |
| Date of last dose              | 01/01/2017                |
| Pain severity                  | 2                         |
| Side of pain                   | Right                     |
| Site of pain                   | Arm                       |
| Number of wounds               | 2                         |
| Site                           | Ear;Nose                  |
| Description                    | None                      |
| Nursing notes                  | captured                  |

* Verify "Social and Medical History" is added to the left pane
* Save the consultation
* Verify "Social and Medical History" is disabled to add
* Navigate to patient dashboard
* Click on "Patient Summary" dashboard
* Verify following details of "Nursing Assessment" in Patient Dashboard
| FIELD                          | VALUE                      |
| Date of consultation           | 01 Jan 17                  |
| Marital status                 | Single                     |
| Highest education level        | No formal education        |
| Pregnancy status               | No                         |
| Current smoker                 | Yes                        |
| Number of cigarettes per day   | 1                          |
| Duration of smoking (in years) | 2                          |
| Drug and Alcohol use           | Never                      |
| Medical History                | Tuberculosis, Hypertension |
| Other medical problems         | HIV                        |
| History of Allergy             | Food, Drugs                |
| Comments about allergy         | Nothing                    |
| Currently taking medication    | Yes                        |
| Type of medication             | Some drug                  |
| Dose and freqency              | daily                      |
| Date of last dose              | 01 Jan 17                  |
| Pain severity (0 - 10)         | 2                          |
| Side of pain                   | Right                      |
| Site of pain                   | Arm                        |
| Number of wounds               | 2                          |
| Site                           | Nose, Ear                  |
| Description                    | None                       |
| Nursing notes                  | captured                   |

Physical Examination
--------------------
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Niya" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select the template "Physical Examination" from on the observation page
* Verify "Physical Examination" is added to the left pane
* Save the consultation
* Verify "Physical Examination" is disabled to add
* Navigate to patient dashboard
* Click on "Patient Summary" dashboard
* Verify following details of "Physical Examination" in Patient Dashboard
| FIELD                             | VALUE                                                                                             |
| General examination               | Well developed female / male in no acute distress                                                 |
| HEENT examination                 | Pupils equal, regular, reactive to light and accomodation, normal extraocular muscles, normocephalic, normal dentition, clear throat, normal neck motion, no jugular vien distension  |
| Chest examination                 | Clear lung bilaterally to auscultation and percussion, normal chest wall motion                   |
| Heart examination                 | Normal S1 & S2, no murmurs, intact pulses                                                         |
| Abdomen examination               | Soft, no hepatosplenomegaly, no tenderness, no mass                                               |
| Rectal and genitalia examination  | Deferred                                                                                          |
| Extremities examination           | No clubbing, cyanosis or edema, normal joints with full range of motion                           |
| Neurologic examination            | Cranial nerves intact, normal muscular deep tendon reflexes, normal strength, normal sensitivity  |

Observation Forms
-----------------
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Niya" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Health Education" from observation page and fill details
| FIELD                                           | VALUE          |
| Date of consultation                            | 01/01/2017     |
| External devices, present                       | Big tube;Other |
| Other type of external device                   | Some device    |
| Nutritional Assessment                          | Regular        |
| Personal hygiene (presence of head lice / bugs) | No             |
| SMFA functional index                           | 1              |
| SMFA bothersome index                           | 2              |
| Education learning needs                        | Yes            |
| Referral care plan                              | No care plan   |
* Verify "Health Education" is added to the left pane

* Select template "OPD Nursing Note" from observation page and fill details
| FIELD                                     | VALUE         |
| Date recorded                             | 05/11/2017    |
| Temperature (C)                           | 32            |
| Pulse (bpm)                               | 77            |
| Respiratory rate (breaths/minute)         | 85            |
| Systolic blood pressure (mmHg)            | 120           |
| Diastolic blood pressure (mmHg)           | 80            |
| Pain Severity                             | 1             |
| Side of pain                              | Right         |
| Type of pain                              | severe        |
| When does the pain occur                  | always        |
| Does the patient have a dressing?         | Yes           |
| Side of dressing                          | Right         |
| Description of wound                      | Other         |
| Description of wound, other               | wet wound     |
| Dressing, comments                        | dressed       |
| Does the patient have a tissue expander?  | Yes           |
| Quantity injected                         | 1             |
| Quantity withdrawn                        | 2             |
| Total volume in tissue expander           | 3             |
| Condition of tissue expander              | normal        |
| Nursing consultation notes                | recorded      |
* Verify "OPD Nursing Note" is added to the left pane

* Save the consultation
* Verify these forms are saved and disabled to add
| FORM                              |
| Health Education                  |
| OPD Nursing Note                  |