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

    public boolean isAppointmentMatched(Table appointmentInfo) {
        System.out.println(allAppointmentDetails.size());
        if (allAppointmentDetails.isEmpty()) {
            Assert.fail("No appointments found");
            return false;
        }
        for (WebElement appointment: allAppointmentDetails){
            if (compareAppointments(appointmentInfo, appointment)){
                return true;
            }
        }
        return false;
    }

    private boolean compareAppointments(Table appointmentInfo, WebElement appointment) {
        for (String columName: appointmentInfo.getColumnNames()) {
            int columnIndex = getColumnIndex(columName, appointmentHeaders);
            if (columnIndex < 0){
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

}
