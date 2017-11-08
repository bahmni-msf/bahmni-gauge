package org.bahmni.gauge.amman.AppointmentScheduling;

import com.thoughtworks.gauge.Table;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;

import java.util.List;

/**
 * Created by jaseenam on 08/09/17.
 */

public class manageAppointmentsListView extends manageAppointmentsHeaders {

    @FindBy(how = How.CSS, using = ".app-list-view table tbody tr")
    public List<WebElement> allAppointmentDetails;

    @FindBy(how = How.CSS, using = ".app-list-view table thead tr th")
    public List<WebElement> appointmentHeaders;

    @FindBy(how = How.XPATH, using = "/html/body/div[2]/div[3]/div/div/section/div[2]/div/div[2]/div/fieldset/button[6]")
    public WebElement cancelStatus;

    @FindBy(how = How.XPATH, using = "/html/body/div[2]/div[3]/div/div/section/div[2]/div/div[2]/div/fieldset/button[5]")
    public WebElement missStatus;

    @FindBy(how = How.XPATH, using = "//*[@id=\"yes\"]")
    public WebElement yesPopup;

    public WebElement isAppointmentMatched(Table appointmentInfo) {
        if (!hasAppointments()) {
            return null;
        }
        for (WebElement appointment : allAppointmentDetails) {
            if (compareAppointments(appointmentInfo, appointment)) {
                return appointment;
            }
        }
        return null;
    }

    private boolean compareAppointments(Table appointmentInfo, WebElement appointment) {
        for (String columName : appointmentInfo.getColumnNames()) {
            int columnIndex = getColumnIndex(columName, appointmentHeaders);
            if (columnIndex < 0) {
                Assert.fail("Column names were not matching!");
                return false;
            }
            String columnValue = appointmentInfo.getTableRows().get(0).getCell(columName);
            if (!appointment.findElements(By.cssSelector("td")).get(columnIndex).getText().contains(columnValue)) {
                return false;
            }
        }
        return true;
    }

    private int getColumnIndex(String columName, List<WebElement> appointmentHeaders) {
        for (int index = 0; index < appointmentHeaders.size(); index++) {
            WebElement header = appointmentHeaders.get(index);
            if (header.getText().contains(columName)) {
                return index;
            }
        }
        return -1;
    }

    public void cancelAppointment(WebElement appointment) {
        appointment.click();
        cancelStatus.click();
        waitForSpinner(driver);
        yesPopup.click();
    }

    public boolean hasAppointments() {
        return !allAppointmentDetails.isEmpty();
    }

    public void missAppointment(WebElement appointment) {
        appointment.click();
        missStatus.click();
        waitForSpinner();
        yesPopup.click();
    }
}
