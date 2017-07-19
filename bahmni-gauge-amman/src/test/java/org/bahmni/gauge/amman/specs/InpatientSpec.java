package org.bahmni.gauge.amman.specs;

import com.thoughtworks.gauge.Step;
import org.bahmni.gauge.amman.inpatient.AdmitPage;
import org.bahmni.gauge.amman.inpatient.IpdHeader;
import org.bahmni.gauge.common.BahmniPage;
import org.bahmni.gauge.common.DriverFactory;
import org.bahmni.gauge.common.PageFactory;
import org.bahmni.gauge.common.inpatient.BedAssignmentPage;
import org.bahmni.gauge.common.inpatient.InpatientHeader;
import org.bahmni.gauge.data.StoreHelper;
import org.junit.Assert;

/**
 * Created by jaseena on 4/28/17.
 */
public class InpatientSpec {

    public void waitForAppReady() {

        BahmniPage.waitForSpinner(DriverFactory.getDriver());
    }

    @Step("Navigate to Inpatient Dashboard")
    public void gotoInpatientDashboard() {
        InpatientHeader inpatientHeader = PageFactory.get(InpatientHeader.class);
        inpatientHeader.gotoIpdDashboard();
        waitForAppReady();
    }


    @Step("Assign an empty bed to the patient")
    public void assignBed() {
        AdmitPage admitPage = PageFactory.get(AdmitPage.class);
        admitPage.assignAnEmptyBed();
    }


    @Step("Navigate to patient ADT queues")
    public void goToPatientAdtQueues() {
        waitForAppReady();
        IpdHeader ipdHeader = PageFactory.get(IpdHeader.class);
        ipdHeader.goToAdmitTab();
    }

    @Step("Navigate to bed management tab")
    public void goToBedManagement() {
        waitForAppReady();
        IpdHeader ipdHeader = PageFactory.get(IpdHeader.class);
        ipdHeader.goToBedManagementTab();
    }

    @Step("Navigate to <ward>")
    public void implementation1(String ward) {
        AdmitPage admitPage = PageFactory.get(AdmitPage.class);
        switch (ward) {

            case "Ward 2nd floor":
                admitPage.goToWard2ndFloor();
                break;

            case "Ward 3rd floor":
                admitPage.goToWard3rdFloor();
                break;

            case "Rehabilitation Center 4th floor":
                admitPage.goToRC4thFloor();
                break;

            case "Rehabilitation Center 5th floor":
                admitPage.goToRC5thFloor();
                break;

            case "Kahramana 1st floor":
                admitPage.goToKahramana1stFloor();
                break;

            case "Kahramana 2nd floor":
                admitPage.goToKahramana2ndFloor();
                break;

            case "Buffer Beds":
                admitPage.goToKahramanaBufferBeds();
                break;
        }
    }

    @Step("Discharge the patient")
    public void transferHome() {
        AdmitPage admitPage = PageFactory.get(AdmitPage.class);
        admitPage.dischargePatient();
    }

}