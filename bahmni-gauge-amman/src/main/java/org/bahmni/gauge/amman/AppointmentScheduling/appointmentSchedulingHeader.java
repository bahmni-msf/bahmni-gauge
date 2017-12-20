package org.bahmni.gauge.amman.AppointmentScheduling;

import org.bahmni.gauge.common.home.HomePage;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;

/**
 * Created by jaseenam on 01/08/17.
 */
public class appointmentSchedulingHeader extends HomePage {
    @FindBy(how = How.LINK_TEXT, using = "Manage Appointments")
    WebElement manageAppointments;

    @FindBy(how = How.LINK_TEXT, using = "Admin")
    WebElement adminTab;

    @FindBy(how = How.LINK_TEXT, using = "Appointments List")
    WebElement appointmentsListTab;

    @FindBy(how = How.LINK_TEXT, using = "Add new appointment")
    WebElement addNewAppointmentLink;

    @FindBy(how = How.LINK_TEXT, using = "List view")
    WebElement listViewLink;

    public void gotoManageAppointments() {
        waitForElementOnPage(manageAppointments);
        manageAppointments.click();
    }

    public void gotoAdminPage() {
        waitForElementOnPage(adminTab);
        adminTab.click();
    }

    public void gotoAppointmentsList() {
        waitForElementOnPage(appointmentsListTab);
        appointmentsListTab.click();
    }

    public void clickAddNewAppointment() {
        waitForElementOnPage(addNewAppointmentLink);
        addNewAppointmentLink.click();
    }

    public void gotoListView() {
        waitForElementOnPage(listViewLink);
        listViewLink.click();
    }
}
