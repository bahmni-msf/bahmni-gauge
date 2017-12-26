package org.bahmni.gauge.amman.specs;

import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import org.bahmni.gauge.amman.AppointmentScheduling.*;
import org.bahmni.gauge.common.BahmniPage;
import org.bahmni.gauge.common.DriverFactory;
import org.bahmni.gauge.common.PageFactory;
import org.junit.Assert;
import org.openqa.selenium.WebElement;

import java.util.List;

import static junit.framework.TestCase.assertTrue;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;

/**
 * Created by jaseenam on 01/08/17.
 */
public class AppointmentSchedulingSpec {

    appointmentSchedulingAdminPage AppointmentSchedulingAdminPage;
    appointmentSchedulingHeader AppointmentSchedulingHeader;
    manageWeeklySummaryView ManageAppointmentsPage;
    servicePage ServicePage;
    manageAppointmentsHeaders ManageAppointmentsHeaders;
    manageAppointmentsListView ManageAppointmentsListView;
    manageAppointmentsCalendarView ManageAppointmentsCalendarView;


    public AppointmentSchedulingSpec() {
        AppointmentSchedulingAdminPage = PageFactory.get(appointmentSchedulingAdminPage.class);
        AppointmentSchedulingHeader = PageFactory.get(appointmentSchedulingHeader.class);
        ManageAppointmentsPage = PageFactory.get(manageWeeklySummaryView.class);
        ServicePage = PageFactory.get(servicePage.class);
        ManageAppointmentsHeaders = PageFactory.get(manageAppointmentsHeaders.class);
        ManageAppointmentsListView = PageFactory.get(manageAppointmentsListView.class);
        ManageAppointmentsCalendarView = PageFactory.get(manageAppointmentsCalendarView.class);
    }

    public void waitForAppReady() {
        BahmniPage.waitForSpinner(DriverFactory.getDriver());
    }

    @Step("Navigate to Admin Tab")
    public void gotoAdminTab() {
        waitForAppReady();
        AppointmentSchedulingHeader.gotoAdminPage();
    }

    @Step("Navigate to Manage Appointments Tab")
    public void gotoManageAppointmentsTab() {
        waitForAppReady();
        AppointmentSchedulingHeader.gotoManageAppointments();
        waitForAppReady();
    }


    @Step("Click on Appointments List link")
    public void gotoAppointmentsListTab() {
        AppointmentSchedulingHeader.gotoAppointmentsList();
        waitForAppReady();
    }

    @Step("Click on List view link")
    public void gotoListViewTab() {
        waitForAppReady();
        AppointmentSchedulingHeader.gotoListView();
    }

    @Step("Click on Add new appointment link")
    public void clickAddNewAppointment() {
        waitForAppReady();
        AppointmentSchedulingHeader.clickAddNewAppointment();
    }

    @Step("Create new service with below details <table>")
    public void createNewService(Table table) {
        List<String> columnNames = table.getColumnNames();
        ServicePage.addService(table, columnNames);
        waitForAppReady();
    }

    @Step("Verify user cannot create service with existing service name <Servicename> <table>")
    public void createNewServiceWithExistingServiceName(String servicename, Table table) {
        List<String> columnNames = table.getColumnNames();
        waitForAppReady();
        ServicePage.addService(table, columnNames);
        Assert.assertTrue(ServicePage.confirmSaveServiceError().contains("Please correct the values in the fields to proceed"));
        Assert.assertTrue(ServicePage.cautionServiceText().equalsIgnoreCase("Service name already exists"));
    }

    @Step("Cancel service creation")
    public void cancelServiceCreation() {
        ManageAppointmentsHeaders.gotoAdminPage();
        waitForAppReady();
        ServicePage.clickButton("Don't save");
    }

    @Step("Verify service details of <servicename> in Admin Service Page <table>")
    public void verifyServiceDetails(String servicename, Table table) {
        waitForAppReady();
        List<String> columnNames = table.getColumnNames();
        TableRow requiredRow = null;
        for (TableRow row : table.getTableRows()) {
            if (row.getCell("Service Name").contains(servicename)) {
                requiredRow = row;
                break;
            }
        }

        for (String coulmnName : columnNames) {
            String actualData = AppointmentSchedulingAdminPage.getColumnData(coulmnName, servicename);
            assertEquals(requiredRow.getCell(coulmnName), actualData);
        }
    }


    @Step("Edit service <Servicename> with following details <table>")
    public void editService(String serviceName, Table table) {
        waitForAppReady();
        AppointmentSchedulingAdminPage.clickEditService(serviceName);
        waitForAppReady();
        List<String> columnNames = table.getColumnNames();
        ServicePage.addService(table, columnNames);
        ServicePage.confirmEditService();
    }

    @Step("Delete service <Servicename> if it exists")
    public void deleteServiceForTeardown(String serviceName) {
        waitForAppReady();
        WebElement row = AppointmentSchedulingAdminPage.selectGivenServiceRow(serviceName);
        if (row != null){
            AppointmentSchedulingAdminPage.deleteService(serviceName);
        }
    }

    @Step("Delete service <Servicename>")
    public void deleteService(String serviceName) {
        waitForAppReady();
        AppointmentSchedulingAdminPage.deleteService(serviceName);
    }

    @Step("Add appointment with below details <table>")
    public void addNewAppointment(Table table) {
        List<String> columnNames = table.getColumnNames();
        waitForAppReady();
        ManageAppointmentsHeaders.addNewAppointment(table, columnNames);
        waitForAppReady();
    }

    @Step("Verify appointment with below details <table>")
    public void verifyAppointmentDetails(Table appointmentInfo) {
        waitForAppReady();
        assertTrue(ManageAppointmentsListView.hasAppointments());
        assertNotNull(ManageAppointmentsListView.isAppointmentMatched(appointmentInfo));
    }

    @Step("Mark cancel if appointment with below details exists <table>")
    public void cancelAppointmentDetails(Table appointmentInfo) {
        waitForAppReady();
        WebElement matchedAppointment = ManageAppointmentsListView.isAppointmentMatched(appointmentInfo);
        if (matchedAppointment != null) {
            ManageAppointmentsListView.cancelAppointment(matchedAppointment);
        }
    }

    @Step("Cancel appointment creation")
    public void cancelAppointmentCreation() {
        ManageAppointmentsCalendarView.click("Back to edit");
        waitForAppReady();
        ManageAppointmentsCalendarView.cancel();
        waitForAppReady();
        ManageAppointmentsCalendarView.click("Don't save");
        waitForAppReady();
    }

    @Step("Verify popup message as same as <message>")
    public void verifyPopupMessage(String message) {
        Assert.assertTrue(ManageAppointmentsCalendarView.conflictPopupMessage().contains(message));
    }

    @Step("Mark as missed appointment with below details <table>")
    public void markAsMissed(Table appointmentInfo) {
        waitForAppReady();
        WebElement matchedAppointment = ManageAppointmentsListView.isAppointmentMatched(appointmentInfo);
        if (matchedAppointment == null) {
            Assert.fail("There is no matching appointment to mark as missed");
            return;
        }
        ManageAppointmentsListView.missAppointment(matchedAppointment);
    }
}
