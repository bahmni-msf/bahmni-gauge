package org.bahmni.gauge.endtb.specs;

import com.thoughtworks.gauge.Step;
import org.bahmni.gauge.common.PageFactory;
import org.bahmni.gauge.common.clinical.DashboardPage;
import org.bahmni.gauge.common.clinical.PatientListingPage;
import org.bahmni.gauge.endtb.program.EndTBProgramManagementPage;

import java.util.LinkedList;
import java.util.List;

public class testSpec {

    List<String> emptyDots= new LinkedList<>();



    @Step("Select patient using identifier in <regnum> and save obs for date <date>")
    public void fillBMI(String id, String date){
        PatientListingPage patientListingPage= PageFactory.get(PatientListingPage.class);
        EndTBProgramManagementPage endTBProgramManagementPage= PageFactory.get(EndTBProgramManagementPage.class);
        patientListingPage.enterPatientIDOrNameInAllPatients(id);
        endTBProgramManagementPage.clickTreatmentDashboard("Second-line TB treatment");
        DashboardPage dashboardPage= PageFactory.get(DashboardPage.class);
        dashboardPage.waitForSpinnerOnDisplayControl();
        dashboardPage.clickDisplayControlHeader("Follow-up");
        dashboardPage.saveObs(date);


    }

    @Step("Select patient using identifier in <regnum> and save obs for dates <date>")
    public void fillDot(String id, String date){



        PatientListingPage patientListingPage= PageFactory.get(PatientListingPage.class);
        EndTBProgramManagementPage endTBProgramManagementPage= PageFactory.get(EndTBProgramManagementPage.class);
        patientListingPage.enterPatientIDOrNameInAllPatients(id);
        endTBProgramManagementPage.clickTreatmentDashboard("Second-line TB treatment");
        DashboardPage dashboardPage= PageFactory.get(DashboardPage.class);

        String[] dates= date.split(";");
        for (String x: dates
             ) {
            dashboardPage.waitForSpinner();
            dashboardPage.waitForSpinnerOnDisplayControl();
            dashboardPage.clickDisplayControlHeader("Follow-up");
            dashboardPage.saveObs(x);


        }





    }
    @Step("Go back to Patient List")
    public void clickOnBackButton(){
        DashboardPage dashboardPage= PageFactory.get(DashboardPage.class);
        dashboardPage.goBackToPatientLists();
    }


//    @AfterSpec(tags="dot")
//    public void printEmptyDots(){
//
//        Gauge.writeMessage("Below are the patients with empty DOT section:");
//        for (String emptyReg: emptyDots
//        ) {
//
//            Gauge.writeMessage(emptyReg);
//
//        }
//    }

}
