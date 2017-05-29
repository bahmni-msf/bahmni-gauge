Other Observation Forms
=======================
Created by jaseenam on 5/29/17

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

OPD Nurse and HE - Health Education form
----------------------------------------
* Create patient "Sara" using API with "Hospital" visit
* Enroll patient to reconstructive surgery program using API
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
* Verify "Health Education" is added to the left pane
* Select template "Health Education" from observation page and fill details 

     |FIELD                                          |VALUE         |
     |-----------------------------------------------|--------------|
     |Date of consultation                           |01/01/2017    |
     |External devices, present                      |Big tube;Other|
     |Other type of external device                  |Some device   |
     |Nutritional Assessment                         |Regular       |
     |Personal hygiene (presence of head lice / bugs)|No            |
     |SMFA functional index                          |1             |
     |SMFA bothersome index                          |2             |
     |Education learning needs                       |Yes           |
     |Referral care plan                             |No care plan  |

* Save the consultation

Physio - Physiotherapy Initial Assessment form
----------------------------------------------
* On the login page
* Login with user "hussein_am" and password "BAHMNI_GAUGE_OPD_PASSWORD" with location "BAHMNI_GAUGE_OPD_LOCATION"
* Click on programs app
* Search and select patient "Sara" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Verify "Physiotherapy Initial Assessment" is added to the left pane
* Select template "Physiotherapy Initial Assessment" from observation page and fill details 

     |FIELD                                                |VALUE                                                                                            |
     |-----------------------------------------------------|-------------------------------------------------------------------------------------------------|
     |Date of consultation                                 |05/23/2017                                                                                       |
     |Grooming                                             |Independent                                                                                      |
     |Feeding                                              |With Assistance                                                                                  |
     |Dressing                                             |Dependent                                                                                        |
     |Toilet use                                           |With Assistance                                                                                  |
     |Transfers                                            |Independent                                                                                      |
     |Stairs                                               |With Assistance                                                                                  |
     |Mobility                                             |Wheelchair                                                                                       |
     |Does the patient use an assistive device or orthosis?|Yes                                                                                              |
     |Type of assistive device or orthosis                 |Two axillary crutches;One elbow crutch;One axillary crutch;Two elbow crutches;cane;Orthosis;Other|
     |Other type of assistive device                       |device comments                                                                                  |
     |Comments about assistive device or orthosis          |assistive device comments                                                                        |
     |Amputee patient?                                     |Yes                                                                                              |
     |Type of amputation                                   |Above Elbow                                                                                      |
     |Side of amputation                                   |Right                                                                                            |
     |Comments about amputation                            |comments                                                                                         |
     |Is the patient coming with a prostheses?             |Yes                                                                                              |
     |Comment about prostheses usage                       |comments                                                                                         |
     |Is there a need of new prosthesis or modification    |Yes                                                                                              |
     |Comment about new prosthesis or modification         |comments                                                                                         |
     |Location of assessment                               |Maxillo-facial                                                                                   |
     |Physical Functional Score (FDI) (%)                  |25.3                                                                                             |
     |Social / Well-being Score (FDI) (%)                  |34.7                                                                                             |
     |Mouth opening test (cm)                              |101                                                                                              |
     |Physiotherapy remarks initial assessment             |comments                                                                                         |

* Save the consultation
