package org.bahmni.gauge.amman.specs;

import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import org.bahmni.gauge.amman.AppointmentScheduling.*;
import org.bahmni.gauge.amman.home.HomePage;
import org.bahmni.gauge.common.BahmniPage;
import org.bahmni.gauge.common.DriverFactory;
import org.bahmni.gauge.common.PageFactory;
import org.junit.Assert;

import java.util.List;

/**
 * Created by jaseenam on 01/08/17.
 */
public class AppointmentSchedulingSpec {

    appointmentSchedulingAdminPage AppointmentSchedulingAdminPage;
    appointmentSchedulingHeader AppointmentSchedulingHeader;
    manageWeeklySummaryView ManageAppointmentsPage;
    servicePage ServicePage;
    manageAppointmentsHeaders ManageAppointmentsHeaders;


    public AppointmentSchedulingSpec() {
        AppointmentSchedulingAdminPage = PageFactory.get(appointmentSchedulingAdminPage.class);
        AppointmentSchedulingHeader = PageFactory.get(appointmentSchedulingHeader.class);
        ManageAppointmentsPage = PageFactory.get(manageWeeklySummaryView.class);
        ServicePage = PageFactory.get(servicePage.class);
    }

    public void waitForAppReady() {
        BahmniPage.waitForSpinner(DriverFactory.getDriver());
    }

    @Step("Navigate to Admin Tab")
    public void gotoAdminTab() {
        waitForAppReady();
        AppointmentSchedulingHeader.gotoAdminPage();
        waitForAppReady();

    }

    @Step("Navigate to Manage Appointments Tab")
    public void gotoManageAppointmentsTab() {
        waitForAppReady();
        AppointmentSchedulingHeader.gotoManageAppointments();
    }

    @Step("Create new service with below details <table>")
    public void createNewService(Table table) {
        List<String> columnNames = table.getColumnNames();
        ServicePage.addService(table, columnNames);
        waitForAppReady();
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
            //System.out.println(requiredRow.getCell(coulmnName));
            String actualData = AppointmentSchedulingAdminPage.getColumnData(coulmnName, servicename);
            //System.out.println(actualData);
            Assert.assertEquals(requiredRow.getCell(coulmnName), actualData);
        }
    }


    @Step("Edit service <Servicename> with following details <table>")
    public void editService(String serviceName, Table table) {
        AppointmentSchedulingAdminPage.clickEditService(serviceName);
        waitForAppReady();
        List<String> columnNames = table.getColumnNames();
        ServicePage.addService(table, columnNames);
        ServicePage.confirmEditService();
    }

    @Step("Delete service <Servicename>")
    public void deleteService(String serviceName) {
        AppointmentSchedulingAdminPage.deleteService(serviceName);
    }


    @Step("Add appointment with below details <table>")
    public void implementation1(Table table) {
        List<String> columnNames = table.getColumnNames();
        ManageAppointmentsHeaders.addNewAppointment(table, columnNames);
        waitForAppReady();
    }

    @Step("Click on link <button>")
    public void clickButton(String button) {
        waitForAppReady();
        switch (button) {
            case "Appointments List":
                ManageAppointmentsHeaders.clickAppointmentsList();
                break;
            case "Add new appointment":
                ManageAppointmentsHeaders.clickAddNewAppointment();
                break;

            case "Today":
                ManageAppointmentsHeaders.clickToday();
                break;

            case "List view":
                ManageAppointmentsHeaders.clickListView();
                break;

            case "Calendar":
                ManageAppointmentsHeaders.clickCalendarView();
                break;
        }
        waitForAppReady();
    }
}
