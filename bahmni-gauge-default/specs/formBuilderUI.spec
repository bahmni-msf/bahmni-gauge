Form Builder UI related tests
=====================
Tags: FormBuilder


Created by bsantosh on 22/10/18

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
     
Create a form by dragging controls
----------------

* Login and create the "formBuilderUITest" form by form builder
* Drag a "label" control to form
* Change the "Label" label name to "Iron Man"
* Drag a "Section" control to form
* Change the "Section" label name to "Captain America"
* Drag a "Obs" control to form
* Associate "HI, Penicillin" concept to "obs"
* Drag a "ObsGroup" control to form
* Associate "History and Examination" concept to "obsGroup"
* Click on save
* Verify "Form Saved Successfully" showed up
* Navigate to form list
* Enter version "1" of "formBuilderUITest" form details
* Verify canvas has "Iron Man" label
* Verify canvas has "HI, Penicillin" label
* Verify canvas has "History and Examination" label
* Click on publish
* Navigate to form list
* Enter version "1" of "formBuilderUITest" form details
* Click on Edit
* Confirm edit
* Validate that control "HI, Penicillin" is not editable
* Select "AddMore" property for "Captain America"
* Drag a "Label" control to form
* Delete "Label" control from form
* Click on save
* Click on publish

Create Table with table control
------------------------
Tags: Intest


* Login and create the "formBuilderTableTest" form by form builder
* Drag a "Table" control to form
* Change the "Column1" label name to "left"
* Change the "Column2" label name to "right"
* Drag a obs control to "left" column of table
* Drag a obs control to "right" column of table
* Associate "HI, Penicillin" concept to "obs"
* Associate "FSTG, Date received" concept to "obs"


Validate Control Properties associated with different concept types
------------------------------------
* Navigate to form list
* Enter version "1" of "formBuilderUITest" form details
* Drag an "Obs" control to form
