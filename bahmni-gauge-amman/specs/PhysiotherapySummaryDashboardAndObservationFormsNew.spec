Physiotherapy Summary Dashboard and Observation Forms
=====================================================
Created by jaseenam on 18/12/17

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

Enter data in observation forms and verify Physiotherapy Summary Dashboard
--------------------------------------------------------------------------
* Create patient "Physio Dashboard" using API with "Hospital" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_OPD_USER" and password "BAHMNI_GAUGE_OPD_PASSWORD" with location "BAHMNI_GAUGE_OPD_LOCATION"
* Click on "Programs" app
* Select patient "Physio Dashboard" in tab "All"
* Navigate to "Reconstructive Surgery" program dashboard
* Open "Physiotherapy Summary" tab on patient dashboard page
* Verify the dashboard name is "Physiotherapy Summary"
* Verify the following display controls are visible 

   |Display Control Title    |
   |-------------------------|
   |Patient Information      |
   |Operative Course in Amman|
   |Physiotherapy Assessments|
   |Appointments             |

* Navigate to consultation
* Select template "Lower Limb Physiotherapy Assessment" from observation page and fill details 

   |FIELD               |VALUE     |
   |--------------------|----------|
   |Date recorded       |01/12/2017|
   |Type of assessment *|Initial   |

* Select template "Lower Limb Physiotherapy Assessment" from observation page and fill details 

   |FIELD                                                                                 |VALUE                                                                                                  |
   |--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
   |Previous history of physiotherapy                                                     |Yes                                                                                                    |
   |Details of previous physiotherapy                                                     |test Details of previous physiotherapy                                                                 |
   |Chief complaint of patient                                                            |test Chief complaint of patient                                                                        |
   |Problem List                                                                          |new Problem List                                                                                       |
   |Affected side                                                                         |Right                                                                                                  |
   |Grooming                                                                              |Independent                                                                                            |
   |Feeding                                                                               |With Assistance                                                                                        |
   |Dressing                                                                              |Dependent                                                                                              |
   |Toilet use                                                                            |With Assistance                                                                                        |
   |Transfers                                                                             |Independent                                                                                            |
   |Stairs                                                                                |With Assistance                                                                                        |
   |Mobility                                                                              |Wheelchair                                                                                             |
   |Does the patient use an assistive device or orthosis?                                 |Yes                                                                                                    |
   |Type of assistive device or orthosis                                                  |Other;One axillary crutch;One elbow crutch;Cane;Two elbow crutches;Orthosis;Two axillary crutches|
   |Other type of assistive device                                                        |Other assistive device                                                                                 |
   |Comments about assistive device or orthosis                                           |new comments                                                                                           |
   |Amputee patient?                                                                      |Yes                                                                                                    |
   |Type of amputation                                                                    |Other                                                                                                  |
   |Other type of amputation                                                              |rtet                                                                                                   |
   |Side of amputation                                                                    |Right                                                                                                  |
   |From                                                                                  |right leg                                                                                              |
   |cm                                                                                    |3                                                                                                      |
   |Comments about stump                                                                  |stump comments                                                                                         |
   |Is the patient using a prostheses?                                                    |Yes                                                                                                    |
   |Comments about prostheses usage                                                       |prostheses comments                                                                                    |
   |True (reference point)                                                                |5cm                                                                                                    |
   |Functional                                                                            |5cm                                                                                                    |
   |Pain Severity                                                                         |1                                                                                                      |
   |Side of pain                                                                          |Right                                                                                                  |
   |Site of pain                                                                          |Other, Toe, Scalp                                                                                      |
   |Site of pain, other                                                                   |other parts                                                                                            |
   |Type of pain                                                                          |severe                                                                                                 |
   |When does the pain occur                                                              |always                                                                                                 |
   |Left : Hip flex.                                                                      |x unit                                                                                                 |
   |Left : Hip ext.                                                                       |y unit                                                                                                 |
   |Left : Int. Rotation                                                                  |z unit                                                                                                 |
   |Left : Ext. Rotation                                                                  |x unit                                                                                                 |
   |Left : Abduction                                                                      |x unit                                                                                                 |
   |Left : Adduction                                                                      |k unit                                                                                                 |
   |Left : Knee flex.                                                                     |x unit                                                                                                 |
   |Left : Knee ext.                                                                      |x unit                                                                                                 |
   |Left : Ankle dorsiflex.                                                               |x unit                                                                                                 |
   |Left : Ankle planterflex                                                              |k unit                                                                                                 |
   |Left : Ankle inversion                                                                |x unit                                                                                                 |
   |Left : Ankle eversion                                                                 |x unit                                                                                                 |
   |Right : Hip flex.                                                                     |x unit                                                                                                 |
   |Right : Hip ext.                                                                      |x unit                                                                                                 |
   |Right : Int. Rotation                                                                 |x unit                                                                                                 |
   |Right : Ext. Rotation                                                                 |x unit                                                                                                 |
   |Right : Abduction                                                                     |x unit                                                                                                 |
   |Right : Adduction                                                                     |x unit                                                                                                 |
   |Right : Knee flex.                                                                    |x unit                                                                                                 |
   |Right : Knee ext.                                                                     |x unit                                                                                                 |
   |Right : Ankle dorsiflex.                                                              |x unit                                                                                                 |
   |Right : Ankle planterflex                                                             |x unit                                                                                                 |
   |Right : Ankle inversion                                                               |x unit                                                                                                 |
   |Right : Ankle eversion                                                                |x unit                                                                                                 |
   |Left : Hip flex.                                                                      |x unit                                                                                                 |
   |Left : Hip ext.                                                                       |x unit                                                                                                 |
   |Left : Int. Rotation                                                                  |x unit                                                                                                 |
   |Left : Ext. Rotation                                                                  |x unit                                                                                                 |
   |Left : Abduction                                                                      |x unit                                                                                                 |
   |Left : Adduction                                                                      |x unit                                                                                                 |
   |Left : Knee flex.                                                                     |x unit                                                                                                 |
   |Left : Knee ext.                                                                      |x unit                                                                                                 |
   |Left : Ankle dorsiflex.                                                               |x unit                                                                                                 |
   |Left : Ankle planterflex                                                              |x unit                                                                                                 |
   |Left : Ankle inversion                                                                |x unit                                                                                                 |
   |Left : Ankle eversion                                                                 |x unit                                                                                                 |
   |Right : Hip flex.                                                                     |x unit                                                                                                 |
   |Right : Hip ext.                                                                      |x unit                                                                                                 |
   |Right : Int. Rotation                                                                 |x unit                                                                                                 |
   |Right : Ext. Rotation                                                                 |x unit                                                                                                 |
   |Right : Abduction                                                                     |x unit                                                                                                 |
   |Right : Adduction                                                                     |x unit                                                                                                 |
   |Right : Knee flex.                                                                    |x unit                                                                                                 |
   |Right : Knee ext.                                                                     |x unit                                                                                                 |
   |Right : Ankle dorsiflex.                                                              |x unit                                                                                                 |
   |Right : Ankle planterflex                                                             |x unit                                                                                                 |
   |Right : Ankle inversion                                                               |x unit                                                                                                 |
   |Right : Ankle eversion                                                                |x unit                                                                                                 |
   |Summary neurological examination (sensation)                                          |Hypo-sensation;Hyper-sensation;Normal                                                                |
   |Summary neurological examination (sensation), comments                                |dsfdsf                                                                                                 |
   |Does the patient have a nerve injury?                                                 |Yes                                                                                                    |
   |Left : Gluteus medius                                                                 |w unit                                                                                                 |
   |Right : Gluteus medius                                                                |b unit                                                                                                 |
   |Left : Gluteus maxi.                                                                  |b unit                                                                                                 |
   |Right : Gluteus maxi.                                                                 |b unit                                                                                                 |
   |Left : Quadriceps                                                                     |b unit                                                                                                 |
   |Left : Illiopsoas                                                                     |b unit                                                                                                 |
   |Right : Quadriceps                                                                    |b unit                                                                                                 |
   |Right : Illiopsoas                                                                    |b unit                                                                                                 |
   |Left : Adductors                                                                      |b unit                                                                                                 |
   |Right : Adductors                                                                     |c unit                                                                                                 |
   |Left : Tibialis anterior                                                              |c unit                                                                                                 |
   |Left : Peron. long. brev                                                              |c unit                                                                                                 |
   |Left : Ext. digitorum                                                                 |c unit                                                                                                 |
   |Left : Ext. hallucis                                                                  |c unit                                                                                                 |
   |Right : Tibialis anterior                                                             |c unit                                                                                                 |
   |Right : Peron. long. Brev                                                             |c unit                                                                                                 |
   |Right : Ext. digitorum                                                                |c unit                                                                                                 |
   |Right : Ext. hallucis                                                                 |c unit                                                                                                 |
   |Left : Gastrocnemius                                                                  |c unit                                                                                                 |
   |Left : Tibialis post.                                                                 |c unit                                                                                                 |
   |Left : Flex. digi. long                                                               |c unit                                                                                                 |
   |Left : Flex. hall. long                                                               |c unit                                                                                                 |
   |Right : Gastrocnemius                                                                 |c unit                                                                                                 |
   |Right : Tibialis post.                                                                |c unit                                                                                                 |
   |Right : Flex. digi. long                                                              |c unit                                                                                                 |
   |Right : Flex. hall. long                                                              |c unit                                                                                                 |
   |Sitting Balance                                                                       |1 = Steady, safe                                                                                       |
   |Rises from chair                                                                      |0 = Unable to without help                                                                             |
   |Attempts to rise                                                                      |1 = Able, requires >1 attempt                                                                          |
   |Immediate standing, balance (first 5 seconds)                                         |2 = Steady without walker or other support                                                             |
   |Standing balance                                                                      |2 = Narrow stance without support                                                                      |
   |Nudged                                                                                |1 = Staggers, grabs, catches self                                                                      |
   |Eyes closed                                                                           |1 = Steady                                                                                             |
   |Turning 360 degrees_1                                                                 |0 = Discontinuous steps                                                                                |
   |Turning 360 degrees_2                                                                 |1 = Steady                                                                                             |
   |Sitting down                                                                          |1 = Uses arms or not a smooth motion                                                                   |
   |Indication of gait                                                                    |1 = No hesitancy                                                                                       |
   |Step length and height                                                                |1 = Steps through L;1 = Steps through R;0 = Steps to                                                 |
   |Foot clearance                                                                        |0 = Foot drop;1 = L foot clears floor;1 = R foot clears floor                                        |
   |Step symmetry                                                                         |1 = Right and left step length appear equal                                                            |
   |Step continuity                                                                       |1 = Steps appear Continuous                                                                            |
   |Path                                                                                  |1 = Mild/moderate deviation or uses w. Aid                                                             |
   |Trunk                                                                                 |2 = No sway, flex., use of arms or w. Aid                                                              |
   |Walking time                                                                          |0 = Heels apart                                                                                        |
   |How old is the patient                                                                |\< 18 years                                                                                             |
   |I could get down on my knees without holding on to something                          |4 = With no trouble                                                                                    |
   |I could keep up when I played with other kids                                         |3 = With a little trouble                                                                              |
   |I could walk for 15 minutes                                                           |3 = With a little trouble                                                                              |
   |I could walk between rooms                                                            |3 = With a little trouble                                                                              |
   |I could get on and off the toilet without using my arms                               |4 = With no trouble                                                                                    |
   |I could get on and off a low chair                                                    |4 = With no trouble                                                                                    |
   |I could get up from the floor by myself                                               |4 = With no trouble                                                                                    |
   |I could sit on a bench without support for 15 minutes?                                |4 = With no trouble                                                                                    |
   |I could stand on my tiptoes to reach for something                                    |4 = With no trouble                                                                                    |
   |I could stand on my tiptoes to put something (e.g. a pack of sugar) on a shelf        |3 = With a little trouble                                                                              |
   |I could walk on slightly uneven surfaces (such as cracked pavement)4 = With no trouble|                                                                                                       |
   |I could walk on rough, uneven surfaces (such as lawns/ fields)                        |3 = With a little trouble                                                                              |
   |I could walk up and down ramps and hills                                              |4 = With no trouble                                                                                    |
   |I could walk up and down curbs (steps)                                                |3 = With a little trouble                                                                              |
   |I could get in and out of a bus                                                       |3 = With a little trouble                                                                              |
   |I could get in and out of a car                                                       |4 = With no trouble                                                                                    |
   |I could walk across the room                                                          |3 = With a little trouble                                                                              |
   |I could walk while wearing a backpack full of books                                   |4 = With no trouble                                                                                    |
   |I could bend over to pick something up                                                |3 = With a little trouble                                                                              |
   |I could exercise that others my age can do                                            |3 = With a little trouble                                                                              |
   |Additional comments                                                                   |test                                                                                                   |

* Save the consultation
* Verify these forms are saved and disabled to add 

   |FORM                               |
   |-----------------------------------|
   |Lower Limb Physiotherapy Assessment|

* Navigate to patient dashboard
* Verify the dashboard name is "Physiotherapy Summary"
* Verify following details of "Physiotherapy Assessments" in Patient Dashboard 

   |FIELD                                                                                 |VALUE                                                                                                  |
   |--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
   |Date recorded                                                                         |01 Dec 17                                                                                              |
   |Type of assessment                                                                    |Initial                                                                                                |
   |Previous history of physiotherapy                                                     |Yes                                                                                                    |
   |Details of previous physiotherapy                                                     |test Details of previous physiotherapy                                                                 |
   |Chief complaint of patient                                                            |test Chief complaint of patient                                                                        |
   |Problem List                                                                          |new Problem List                                                                                       |
   |Affected side                                                                         |Right                                                                                                  |
   |Grooming                                                                              |Independent                                                                                            |
   |Feeding                                                                               |With Assistance                                                                                        |
   |Dressing                                                                              |Dependent                                                                                              |
   |Toilet use                                                                            |With Assistance                                                                                        |
   |Transfers                                                                             |Independent                                                                                            |
   |Stairs                                                                                |With Assistance                                                                                        |
   |Mobility                                                                              |Wheelchair                                                                                             |
   |Does the patient use an assistive device or orthosis?                                 |Yes                                                                                                    |
   |Type of assistive device or orthosis                                                  |Other, One axillary crutch, One elbow crutch, Cane, Two elbow crutches, Orthosis, Two axillary crutches|
   |Other type of assistive device                                                        |Other assistive device                                                                                 |
   |Comments about assistive device or orthosis                                           |new comments                                                                                           |
   |Amputee patient?                                                                      |Yes                                                                                                    |
   |Type of amputation                                                                    |Other                                                                                                  |
   |Other type of amputation                                                              |rtet                                                                                                   |
   |Side of amputation                                                                    |Right                                                                                                  |
   |From                                                                                  |right leg                                                                                              |
   |cm                                                                                    |3                                                                                                      |
   |Comments about stump                                                                  |stump comments                                                                                         |
   |Is the patient using a prostheses?                                                    |Yes                                                                                                    |
   |Comments about prostheses usage                                                       |prostheses comments                                                                                    |
   |True (reference point)                                                                |5cm                                                                                                    |
   |Functional                                                                            |5cm                                                                                                    |
   |Pain Severity                                                                         |1                                                                                                      |
   |Side of pain                                                                          |Right                                                                                                  |
   |Site of pain                                                                          |Other, Toe, Scalp                                                                                      |
   |Site of pain, other                                                                   |other parts                                                                                            |
   |Type of pain                                                                          |severe                                                                                                 |
   |When does the pain occur                                                              |always                                                                                                 |
   |Left : Hip flex.                                                                      |x unit                                                                                                 |
   |Left : Hip ext.                                                                       |y unit                                                                                                 |
   |Left : Int. Rotation                                                                  |z unit                                                                                                 |
   |Left : Ext. Rotation                                                                  |x unit                                                                                                 |
   |Left : Abduction                                                                      |x unit                                                                                                 |
   |Left : Adduction                                                                      |k unit                                                                                                 |
   |Left : Knee flex.                                                                     |x unit                                                                                                 |
   |Left : Knee ext.                                                                      |x unit                                                                                                 |
   |Left : Ankle dorsiflex.                                                               |x unit                                                                                                 |
   |Left : Ankle planterflex                                                              |k unit                                                                                                 |
   |Left : Ankle inversion                                                                |x unit                                                                                                 |
   |Left : Ankle eversion                                                                 |x unit                                                                                                 |
   |Right : Hip flex.                                                                     |x unit                                                                                                 |
   |Right : Hip ext.                                                                      |x unit                                                                                                 |
   |Right : Int. Rotation                                                                 |x unit                                                                                                 |
   |Right : Ext. Rotation                                                                 |x unit                                                                                                 |
   |Right : Abduction                                                                     |x unit                                                                                                 |
   |Right : Adduction                                                                     |x unit                                                                                                 |
   |Right : Knee flex.                                                                    |x unit                                                                                                 |
   |Right : Knee ext.                                                                     |x unit                                                                                                 |
   |Right : Ankle dorsiflex.                                                              |x unit                                                                                                 |
   |Right : Ankle planterflex                                                             |x unit                                                                                                 |
   |Right : Ankle inversion                                                               |x unit                                                                                                 |
   |Right : Ankle eversion                                                                |x unit                                                                                                 |
   |Left : Hip flex.                                                                      |x unit                                                                                                 |
   |Left : Hip ext.                                                                       |x unit                                                                                                 |
   |Left : Int. Rotation                                                                  |x unit                                                                                                 |
   |Left : Ext. Rotation                                                                  |x unit                                                                                                 |
   |Left : Abduction                                                                      |x unit                                                                                                 |
   |Left : Adduction                                                                      |x unit                                                                                                 |
   |Left : Knee flex.                                                                     |x unit                                                                                                 |
   |Left : Knee ext.                                                                      |x unit                                                                                                 |
   |Left : Ankle dorsiflex.                                                               |x unit                                                                                                 |
   |Left : Ankle planterflex                                                              |x unit                                                                                                 |
   |Left : Ankle inversion                                                                |x unit                                                                                                 |
   |Left : Ankle eversion                                                                 |x unit                                                                                                 |
   |Right : Hip flex.                                                                     |x unit                                                                                                 |
   |Right : Hip ext.                                                                      |x unit                                                                                                 |
   |Right : Int. Rotation                                                                 |x unit                                                                                                 |
   |Right : Ext. Rotation                                                                 |x unit                                                                                                 |
   |Right : Abduction                                                                     |x unit                                                                                                 |
   |Right : Adduction                                                                     |x unit                                                                                                 |
   |Right : Knee flex.                                                                    |x unit                                                                                                 |
   |Right : Knee ext.                                                                     |x unit                                                                                                 |
   |Right : Ankle dorsiflex.                                                              |x unit                                                                                                 |
   |Right : Ankle planterflex                                                             |x unit                                                                                                 |
   |Right : Ankle inversion                                                               |x unit                                                                                                 |
   |Right : Ankle eversion                                                                |x unit                                                                                                 |
   |Summary neurological examination (sensation)                                          |Hypo-sensation, Hyper-sensation, Normal                                                                |
   |Summary neurological examination (sensation), comments                                |dsfdsf                                                                                                 |
   |Does the patient have a nerve injury?                                                 |Yes                                                                                                    |
   |Left : Gluteus medius                                                                 |w unit                                                                                                 |
   |Right : Gluteus medius                                                                |b unit                                                                                                 |
   |Left : Gluteus maxi.                                                                  |b unit                                                                                                 |
   |Right : Gluteus maxi.                                                                 |b unit                                                                                                 |
   |Left : Quadriceps                                                                     |b unit                                                                                                 |
   |Left : Illiopsoas                                                                     |b unit                                                                                                 |
   |Right : Quadriceps                                                                    |b unit                                                                                                 |
   |Right : Illiopsoas                                                                    |b unit                                                                                                 |
   |Left : Adductors                                                                      |b unit                                                                                                 |
   |Right : Adductors                                                                     |c unit                                                                                                 |
   |Left : Tibialis anterior                                                              |c unit                                                                                                 |
   |Left : Peron. long. brev                                                              |c unit                                                                                                 |
   |Left : Ext. digitorum                                                                 |c unit                                                                                                 |
   |Left : Ext. hallucis                                                                  |c unit                                                                                                 |
   |Right : Tibialis anterior                                                             |c unit                                                                                                 |
   |Right : Peron. long. Brev                                                             |c unit                                                                                                 |
   |Right : Ext. digitorum                                                                |c unit                                                                                                 |
   |Right : Ext. hallucis                                                                 |c unit                                                                                                 |
   |Left : Gastrocnemius                                                                  |c unit                                                                                                 |
   |Left : Tibialis post.                                                                 |c unit                                                                                                 |
   |Left : Flex. digi. long                                                               |c unit                                                                                                 |
   |Left : Flex. hall. long                                                               |c unit                                                                                                 |
   |Right : Gastrocnemius                                                                 |c unit                                                                                                 |
   |Right : Tibialis post.                                                                |c unit                                                                                                 |
   |Right : Flex. digi. long                                                              |c unit                                                                                                 |
   |Right : Flex. hall. long                                                              |c unit                                                                                                 |
   |Sitting Balance                                                                       |1 = Steady, safe                                                                                       |
   |Rises from chair                                                                      |0 = Unable to without help                                                                             |
   |Attempts to rise                                                                      |1 = Able, requires >1 attempt                                                                          |
   |Immediate standing, balance (first 5 seconds)                                         |2 = Steady without walker or other support                                                             |
   |Standing balance                                                                      |2 = Narrow stance without support                                                                      |
   |Nudged                                                                                |1 = Staggers, grabs, catches self                                                                      |
   |Eyes closed                                                                           |1 = Steady                                                                                             |
   |Turning 360 degrees_1                                                                 |0 = Discontinuous steps                                                                                |
   |Turning 360 degrees_2                                                                 |1 = Steady                                                                                             |
   |Sitting down                                                                          |1 = Uses arms or not a smooth motion                                                                   |
   |Balance Score                                                                         |10                                                                                                     |
   |Indication of gait                                                                    |1 = No hesitancy                                                                                       |
   |Step length and height                                                                |1 = Steps through L, 1 = Steps through R, 0 = Steps to                                                 |
   |Foot clearance                                                                        |0 = Foot drop, 1 = L foot clears floor, 1 = R foot clears floor                                        |
   |Step symmetry                                                                         |1 = Right and left step length appear equal                                                            |
   |Step continuity                                                                       |1 = Steps appear Continuous                                                                            |
   |Path                                                                                  |1 = Mild/moderate deviation or uses w. Aid                                                             |
   |Trunk                                                                                 |2 = No sway, flex., use of arms or w. Aid                                                              |
   |Walking time                                                                          |0 = Heels apart                                                                                        |
   |Gait Score                                                                            |10                                                                                                     |
   |Total Score                                                                           |20                                                                                                     |
   |Risk of Falls                                                                         |Moderate                                                                                               |
   |How old is the patient                                                                |\< 18 years                                                                                             |
   |I could get down on my knees without holding on to something                          |4 = With no trouble                                                                                    |
   |I could keep up when I played with other kids                                         |3 = With a little trouble                                                                              |
   |I could walk for 15 minutes                                                           |3 = With a little trouble                                                                              |
   |I could walk between rooms                                                            |3 = With a little trouble                                                                              |
   |I could get on and off the toilet without using my arms                               |4 = With no trouble                                                                                    |
   |I could get on and off a low chair                                                    |4 = With no trouble                                                                                    |
   |I could get up from the floor by myself                                               |4 = With no trouble                                                                                    |
   |I could sit on a bench without support for 15 minutes?                                |4 = With no trouble                                                                                    |
   |I could stand on my tiptoes to reach for something                                    |4 = With no trouble                                                                                    |
   |I could stand on my tiptoes to put something (e.g. a pack of sugar) on a shelf        |3 = With a little trouble                                                                              |
   |I could walk on slightly uneven surfaces (such as cracked pavement)4 = With no trouble|                                                                                                       |
   |I could walk on rough, uneven surfaces (such as lawns/ fields)                        |3 = With a little trouble                                                                              |
   |I could walk up and down ramps and hills                                              |4 = With no trouble                                                                                    |
   |I could walk up and down curbs (steps)                                                |3 = With a little trouble                                                                              |
   |I could get in and out of a bus                                                       |3 = With a little trouble                                                                              |
   |I could get in and out of a car                                                       |4 = With no trouble                                                                                    |
   |I could walk across the room                                                          |3 = With a little trouble                                                                              |
   |I could walk while wearing a backpack full of books                                   |4 = With no trouble                                                                                    |
   |I could bend over to pick something up                                                |3 = With a little trouble                                                                              |
   |I could exercise that others my age can do                                            |3 = With a little trouble                                                                              |
   |Total Score                                                                           |87.5                                                                                                   |
   |Additional comments                                                                   |test                                                                                                   |
