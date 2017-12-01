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

    @FindBy(how = How.CSS, using = ".ngdialog-content")
    public WebElement conflictPopupMessage;

    @FindBy(how = How.ID, using = "modal-revise-button2")
    public WebElement dontSavePopup;

    public void click(String buttonName) {
        waitForSpinner();
        switch (buttonName) {
            case "Back to edit":
                backToEditConflictPopup.click();
                break;
            case "Don't save":
                dontSavePopup.click();
                break;
            default:
                Assert.fail("There is no such " + buttonName + "button");
        }
        waitForSpinner();
    }

    public String conflictPopupMessage() {
        return conflictPopupMessage.getText();
    }
}
