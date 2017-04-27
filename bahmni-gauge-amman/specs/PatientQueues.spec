Patient Queues Scenarios
========================
Created by swarup, jaseena, kaustav on 10/24/16

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.


Create Patient and Verify Programs Queue
-----------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on registration app
* Click on create new patient link
* Enter Patient Details
| firstName | lastName | givenNameArabic | familyNameArabic | gender | age | governorate | country | phoneNumber1 | spokenLanguages | nationality1 | isCareTakerRequiredCheckBox | statusofOfficialIDdocuments|
| Abdulla   | Yonus    | عبدالله         | حسن              | Male   | 30  | Amman       | Jordan  | +9898989898  | English         | Egyptian     | True| Waiting|

* Start "First Stage Validation" visit and navigate to Programs page
* Enroll patient to the following program
| name                   | dateOfRegistration | programStatus  |
| Reconstructive Surgery | 09/09/2016         | Identification |

* Navigate to queues
* Search patient "Abdulla Yonus" from "Programs" queue
* Verify patient details of "Abdulla Yonus" in queue
| Name             |
| Abdulla Yonus    |

* Search patient "Abdulla Yonus" from "Awaiting Validation - 1st Stage " queue
* Verify patient details of "Abdulla Yonus" in queue
| Name             |
| Abdulla Yonus    |


Patient In Medical File incomplete queue
----------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Abdulla Yonus" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Medical History" from observation page and fill details
| FIELD                         | VALUE                 |
| Name of MLO                   | Dr. Feras Nasr        |
| Network Area                  | Sana'a Network        |
| Referred by                   | Ameer                 |
| Date of injury                | 08/28/2016            |
| Cause of injury               | Burns                 |
| Patient General Condition     | Walking Alone         |
| If caretaker is needed, why?  | Functional disability |

* Select template "First Stage Validation" from observation page and fill details
| FIELD                             | VALUE      |
| Date Received                     | 09/28/2016 |
| Is the medical file complete?     | No         |
| Document(s) needed to be complete | Sample     |
| Specialty                         | Orthopedic |
| Stage                             | 2          |

* Save the consultation
* Navigate to queues
* Search patient "Abdulla Yonus" from "Incomplete Medical File" queue
* Verify patient details of "Abdulla Yonus" in queue
| Date Of File Received | Name              | Name Of MLO    | Documents Needed To Be Complete |
| 28/09/2016            | Abdulla Yonus     | Dr. Feras Nasr | Sample                          |


Patient In Awaiting 1st stage validation queue
----------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Search and select patient "Abdulla Yonus" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "First Stage Validation" from observation page and fill details
| FIELD                         | VALUE      |
| Date Received                 | 10/10/2016 |
| Is the medical file complete? | Yes        |

* Save the consultation
* Navigate to queues
* Search patient "Abdulla Yonus" from "Awaiting Validation - 1st Stage " queue
* Verify patient details of "Abdulla Yonus" in queue
| Date Of File Received | Name             | Name Of MLO    | Nationality | Specialty  |
| 10/10/2016            | Abdulla Yonus    | Dr. Feras Nasr | Egyptian    | Orthopedic |


Patient In MoreInformation/ Postponed queue
----------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_VC_MEMBER_USER" and password "BAHMNI_GAUGE_VC_MEMBER_PASSWORD" with location "BAHMNI_GAUGE_VC_MEMBER_LOCATION"
* Click on programs app
* Search and select patient "Abdulla Yonus" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "First Stage Validation" from observation page and fill details
| FIELD                                     | VALUE                   |
| Date of presentation                      | 10/09/2016              |
| Outcome for 1st stage surgical validation | Postponed               |
| Postpone Reason                           | P2: Waiting for healing |

* Save the consultation
* Navigate to queues
* Search patient "Abdulla Yonus" from "More Information / Postponed " queue
* Verify patient details of "Abdulla Yonus" in queue
| Date Of Presentation | Name             | Outcomes For 1st Stage Surgical Validation | Postpone Reason         |
| 09/10/2016           | Abdulla Yonus    | Postponed                                  | P2: Waiting for healing |

Wait for the scheduler to run and close the visit
* Search and select patient "Abdulla Yonus" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Verify Consultation button is not present


Patient in Validated Patients queue
-----------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on registration app
* Search patient with name "Abdulla Yonus"
* Select the patient from the search results
* Start "First Stage Validation" visit and navigate to Programs page
* On the login page
* Login with username "BAHMNI_GAUGE_VC_MEMBER_USER" and password "BAHMNI_GAUGE_VC_MEMBER_PASSWORD" with location "BAHMNI_GAUGE_VC_MEMBER_LOCATION"
* Click on programs app
* Search and select patient "Abdulla Yonus" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "First Stage Validation" from observation page and fill details
| FIELD                         | VALUE      |
|Type of medical information received|  Updated Medical file|
|Date Received|  04/01/2016|
|Is the medical file complete?|  Yes|
|Document(s) needed to be complete|  all completed|
|Specialty|  Orthopedic|
|Stage|  2|
|Date of presentation|  10/08/2016|
|Outcome for 1st stage surgical validation|  Valid|
|Priority|  Low|
|Name of Surgeon 1|  Dr. Rasheed Al Samerai|
|Name of Surgeon 2|  Dr. Sofian Al-Qassab|
|Does the Patient need Surgical Final Validation?|  Yes|
|Comments|  validation done|
|Outcome for 1st stage Anaesthesia validation|  Fits anaesthesia criteria|
|Name of Anaesthetist | Dr. Hadeel Al-Ani|
|Type of medical information needed for next submission|  up to date|

* Save the consultation
* Navigate to queues
* Search patient "Abdulla Yonus" from "Validated Patients" queue
* Verify patient details of "Abdulla Yonus" in queue
|Date Of Presentation|	Name|	Age|	Country|	Name Of MLO|	Stage|	Specialty|	Priority|	Comments About Validation|	Does The Patient Need Surgical Final Validation|    Is Caretaker Required?|	Status Of Official ID Documents|
|08/10/2016|	Abdulla Yonus|	30|	Jordan|	Dr. Feras Nasr|	2|	Orthopedic|	Low|	validation done|	Yes|	Yes|	Waiting|


Patient In Awaiting Follow up validation queue
----------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Abdulla Yonus" from "Programs" queue
* Edit "Reconstructive Surgery" Program with following details
| programStatus     |
| Network Follow-up |

* Navigate to queues
* Search patient "Abdulla Yonus" from "Awaiting Validation - Follow Up Stage " queue
* Verify patient details of "Abdulla Yonus" in queue
| Name          | Name Of MLO    | Nationality | Specialty  |
| Abdulla Yonus | Dr. Feras Nasr | Egyptian    | Orthopedic|



Patient In Continue Follow up validation queue
----------------------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on registration app
* Search patient with name "Abdulla Yonus"
* Select the patient from the search results
* Start "Follow-Up Validation" visit and navigate to Programs page
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Go to "Observations" tab
* Select template "Follow-up Validation" from observation page and fill details
| FIELD                                      | VALUE                    |
| Date of presentation                       | 10/10/2016               |
| Stage                                      | 2                        |
| Outcome for follow-up surgical validation  | Continue under follow-up |
| Time for next medical follow-up to be done | 1 month                  |
| Comments about next follow-up              | Followup After 1 month   |

* Save the consultation
* Navigate to queues
* Search patient "Abdulla Yonus" from "To Continue Under Follow-Up " queue
* Verify patient details of "Abdulla Yonus" in queue
| Date Of Presentation | Name          | Time For Next Medical Follow-up | Comments               |
| 10/10/2016           | Abdulla Yonus | 1 month                         | Followup After 1 month |


Patient In Expected arrival queue
---------------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on registration app
* Search patient with name "Abdulla Yonus"
* Select the patient from the search results
* Enter Patient Details
|expectedDateofArrival  |
|04/20/2017             |

* Save Patient
* Go to Home Page
* Click on programs app
* Search patient "Abdulla Yonus" from "Expected Arrival " queue
* Verify patient details of "Abdulla Yonus" in queue
| Name          | Age   | Country | Specialty  | Priority   | Expected Date Of Arrival |
| Abdulla Yonus | 30    | Jordan  | Orthopedic | Low        | 20/04/2017               |


Patient In Hospital RSP queue
-----------------------------
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on registration app
* Search patient with name "Abdulla Yonus"
* Select the patient from the search results
* Enter Patient Details
|dateofArrival|
|04/20/2017   |

* Start "First Stage Validation" visit and navigate to Programs page
* Edit "Reconstructive Surgery" Program with following details
| programStatus     |
| Surgical          |

* Navigate to queues
* Search patient "Abdulla Yonus" from "Hospital RSP" queue
* Verify patient details of "Abdulla Yonus" in queue
| Name          | Country | Age      | Specialty    |
| Abdulla Yonus | Jordan  | 30       | Orthopedic   |