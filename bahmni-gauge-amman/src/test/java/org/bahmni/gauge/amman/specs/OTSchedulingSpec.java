package org.bahmni.gauge.amman.specs;

import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.Table;
import org.bahmni.gauge.amman.OTScheduling.otHomePage;
import org.bahmni.gauge.amman.OTScheduling.otSchedulingPage;
import org.bahmni.gauge.amman.OTScheduling.otSurgicalBlockPage;
import org.bahmni.gauge.common.BahmniPage;
import org.bahmni.gauge.common.DriverFactory;
import org.bahmni.gauge.common.PageFactory;
import org.junit.Assert;

import java.util.List;

/**
 * Created by jaseenam on 20/07/17.
 */
public class OTSchedulingSpec {
    private otSchedulingPage OTSchedulingPage;
    private otHomePage OTHomePage;
    private otSurgicalBlockPage OTSurgicalBlockPage;

    public OTSchedulingSpec() {
        OTSchedulingPage = PageFactory.get(otSchedulingPage.class);
        OTHomePage = PageFactory.get(otHomePage.class);
        OTSurgicalBlockPage = PageFactory.get(otSurgicalBlockPage.class);
    }

    public void waitForAppReady() {

        BahmniPage.waitForSpinner(DriverFactory.getDriver());
    }

    @Step("Navigate to OT Scheduling tab")
    public void gotoOTScheduling() {
        waitForAppReady();
        OTHomePage.goToOTScheduling();
        waitForAppReady();
    }

    @Step("Navigate to Surgical Queues tab")
    public void goToSurgicalQueues() {
        OTHomePage.goToSurgicalQueues();
        waitForAppReady();
    }

    @Step("Create a new surgical block for <Surgeon> in <OT> from date <startDate> time <startTime> to date <endDate> time <endTime>")
    public void createNewSurgicalBlock(String surgeon, String OT, String startdate, String starttime, String enddate, String endtime) {
        waitForAppReady();
        OTSchedulingPage.gotoCreateSurgicalBlock();
        waitForAppReady();
        OTSurgicalBlockPage.selectSurgeon(surgeon);
        waitForAppReady();
        OTSurgicalBlockPage.selectLocation(OT);
        OTSurgicalBlockPage.selectDateTime(startdate, starttime, enddate, endtime);
        waitForAppReady();
        OTSurgicalBlockPage.clickSave();
    }

    @Step("Verify block is created for <Surgeon> in <OT> from date <startDate> time <startTime> to date <endDate> time <endTime>")
    public void verifySurgicalBlockIsCreated(String surgeon, String OT, String startdate, String starttime, String enddate, String endtime) {
        waitForAppReady();
        OTSchedulingPage.verifySurgicalBlockIsCreated(surgeon, OT, startdate, enddate);
        waitForAppReady();
        int check = OTSurgicalBlockPage.verifyBlockdata(surgeon, OT, startdate, starttime, enddate, endtime);
        if (check == 0) {
            Assert.fail("Block not found");
        }
    }

    @Step("Edit surgical block <surgicalBlock> in <OT> on <date> with following details <table>")
    public void editSurgicalBlock(String surgicalBlock, String OT, String date, Table table) {
        OTSchedulingPage.goToSurgeryBlockDate(date);
        OTSchedulingPage.clickEditService(surgicalBlock, OT);
        waitForAppReady();
        List<String> columnNames = table.getColumnNames();
        otSurgicalBlockPage.editSurgicalBlock(table, columnNames);
        OTSurgicalBlockPage.clickSave();
        waitForAppReady();
    }

    @Step("Add surgery with below details <table>")
    public void addSurgeriesInBlock(Table table) {
        waitForAppReady();
        OTSurgicalBlockPage.addSugery(table);
        waitForAppReady();
        OTSurgicalBlockPage.clickSave();
        waitForAppReady();
    }

    @Step(" Verify populated surgery details <table>")
    public void verifySurgeryDetails(Table table) {
        waitForAppReady();
        OTSurgicalBlockPage.editSurgery(table);
        waitForAppReady();
        OTSurgicalBlockPage.clickSave();
        waitForAppReady();
    }

    @Step("Cancel surgical block from Surgical Block for <Hanna Janho> in <OT 1> on <09 Sep 2017, Sat> with reason <Cancel reason from Surgical Block>")
    public void cancelSurgicalBlockFromSurgicalBlock(Object arg0, Object arg1, Object arg2, Object arg3) {

    }

    @Step("Cancel surgical block from Calendar for <Hanna Janho> in <OT 1> on <09 Sep 2017, Sat> with reason <Cancel reason from calendar>")
    public void cancelSurgicalBlockFromCalendar(Object arg0, Object arg1, Object arg2, Object arg3) {

    }

    @Step("Postpone surgical block from Surgical Block for <Hanna Janho> in <OT 1> on <09 Sep 2017, Sat> with reason <Postpone reason from Surgical Block>")
    public void postponeSurgicalBlockFromSurgicalBlock(Object arg0, Object arg1, Object arg2, Object arg3) {

    }

    @Step("Postpone surgical block from Calendar for <Hanna Janho> in <OT 1> on <09 Sep 2017, Sat> with reason <Postpone reason from calendar>")
    public void postponeSurgicalBlockFromCalendar(Object arg0, Object arg1, Object arg2, Object arg3) {

    }

    @Step("Verify block is created")
    public void implementation1() {

    }

}
