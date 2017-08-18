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

    public void gotoManageAppointments() {
        manageAppointments.click();
    }

    public void gotoAdminPage() {
        adminTab.click();
    }

}
