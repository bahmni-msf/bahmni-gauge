Patient Nursing Assessment
=====================
Created by swarup on 2/16/17

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
     
Nursing Assessment Baseline Vital Signs
---------------------------------------
* Create patient "Yahya" using API with "First Stage Validation" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Yahya" from "Programs" queue
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

* Save the consultation
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

Nursing Assessment Social and Medical History
---------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Yahya" from "Programs" queue
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

* Save the consultation
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

//Nursing Assessment Health Education
//-----------------------------------
//* On the login page
//* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
//* Click on programs app
//* Search and select patient "Yahya" from "Programs" queue
//* Navigate to "Reconstructive Surgery" program dashboard
//* Navigate to consultation
//* Go to "Observations" tab
//* Select template "Health Education" from observation page and fill details
//| FIELD                                           | VALUE          |
//| Date of consultation                            | 01/01/2017     |
//| External devices, present                       | Big tube;Other |
//| Other type of external device                   | Some device    |
//| Nutritional Assessment                          | Regular        |
//| Personal hygiene (presence of head lice / bugs) | No             |
//| SMFA functional index                           | 1              |
//| SMFA bothersome index                           | 2              |
//| Education learning needs                        | Yes            |
//| Referral care plan                              | No care plan   |
//* Save the consultation
//* Navigate to patient dashboard
//* Click on "Patient Summary" dashboard
//* Verify following details of "Health Education" in Patient Dashboard
//| FIELD                                           | VALUE           |
//| Date of consultation                            | 01 Jan 17       |
//| External devices, present                       | Big tube, Other |
//| Other type of external device                   | Some device     |
//| Nutritional Assessment                          | Regular         |
//| Personal hygiene (presence of head lice / bugs) | No              |
//| SMFA functional index                           | 1               |
//| SMFA bothersome index                           | 2               |
//| Education learning needs                        | Yes             |
//| Referral care plan                              | No care plan    |
