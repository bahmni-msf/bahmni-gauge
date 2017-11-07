package org.bahmni.gauge.amman.AppointmentScheduling;

import org.junit.Assert;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;

/**
 * Created by jaseenam on 08/09/17.
 */
public class manageAppointmentsCalendarView extends manageAppointmentsHeaders {

    @FindBy(how = How.XPATH, using = "//*[@id=\"modal-revise-button3\"]")
    public WebElement backToEditConflictPopup;

    @FindBy(how = How.CSS, using = "p.ng-binding")
    public WebElement conflictPopupMessage;

    public void click(String buttonName) {
        switch (buttonName) {
            case "Back to edit":
                backToEditConflictPopup.click();
                break;
            default:
                Assert.fail("There is no such " + buttonName + "button");
        }
    }

    public String conflictPopupMessage() {
        return conflictPopupMessage.getText();
    }
}
