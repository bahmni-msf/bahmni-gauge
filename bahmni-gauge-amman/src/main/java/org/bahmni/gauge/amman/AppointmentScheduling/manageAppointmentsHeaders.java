package org.bahmni.gauge.amman.AppointmentScheduling;

import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;
import org.openqa.selenium.support.ui.Select;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;

/**
 * Created by jaseenam on 08/09/17.
 */
public class manageAppointmentsHeaders extends appointmentSchedulingHeader {
    @FindBy(how = How.CSS, using = "#patientID")
    WebElement patientIDorName;

    @FindBy(how = How.CSS, using = "#service")
    WebElement serviceName;

    @FindBy(how = How.CSS, using = "#serviceType")
    WebElement serviceType;

    @FindBy(how = How.CSS, using = "#location")
    WebElement location;

    @FindBy(how = How.CSS, using = "#provider")
    WebElement provider;

    @FindBy(how = How.CSS, using = "#date")
    WebElement appointmentDate;

    @FindBy(how = How.CSS, using = "#startTimeID")
    WebElement startTime;

    @FindBy(how = How.CSS, using = "#endTimeID")
    WebElement endTime;

    @FindBy(how = How.CSS, using = "input[type='checkbox']")
    WebElement walkInAppCheckbox;

    @FindBy(how = How.CSS, using = "#notes")
    WebElement notes;

    @FindBy(how = How.CSS, using = ".create-new-app-container")
    WebElement addAppointmentSlider;

    @FindBy(how = How.CSS, using = ".service-save-btn.create-appointment-action-btn")
    WebElement saveAppointmentBtn;

    @FindBy(how = How.LINK_TEXT, using = "Cancel")
    WebElement cancelAppointmentBtn;

    public void addNewAppointment(Table table, List<String> colNames) {
        waitForVisibilityOfElementOnPage(addAppointmentSlider);
        List<TableRow> services = table.getTableRows();
        TableRow service = services.get(0);
        for (String cellname : colNames) {
            String cellVal = service.getCell(cellname);
            switch (cellname) {
                case "Patient":
                    fillAutocomplete(patientIDorName, cellVal);
                    break;
                case "Service":
                    waitForVisibilityOfElementOnPage(serviceName);
                    new Select(serviceName).selectByVisibleText(cellVal);
                    break;
                case "Service App. Type":
                    waitForVisibilityOfElementOnPage(serviceType);
                    new Select(serviceType).selectByVisibleText(cellVal);
                    break;
                case "Location":
                    waitForVisibilityOfElementOnPage(location);
                    new Select(location).selectByVisibleText(cellVal);
                    break;
                case "Provider":
                    waitForVisibilityOfElementOnPage(provider);
                    new Select(provider).selectByVisibleText(cellVal);
                    break;

                case "Date":
                    waitForVisibilityOfElementOnPage(appointmentDate);
                    if (cellVal.contains("NOW")) {
                        cellVal = todayDateAsString();
                    }
                    appointmentDate.sendKeys(cellVal);
                    break;

                case "Start Time":
                    waitForVisibilityOfElementOnPage(startTime);
                    startTime.sendKeys(cellVal);
                    break;

                case "End Time":
                    waitForVisibilityOfElementOnPage(endTime);
                    endTime.sendKeys(cellVal);
                    break;
                case "Walk-in Appointment":
                    waitForVisibilityOfElementOnPage(walkInAppCheckbox);
                    if (cellVal.equalsIgnoreCase("Yes")) {
                        walkInAppCheckbox.click();
                    }
                    break;
                case "Notes":
                    waitForVisibilityOfElementOnPage(notes);
                    notes.clear();
                    notes.sendKeys(cellVal);
                    break;
            }
        }
        click(saveAppointmentBtn);
    }

    private String todayDateAsString() {
        DateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy");
        Date today = new Date();
        return dateFormat.format(today);
    }


    public void fillAutocomplete(WebElement autoComplete, String value) {
        waitForVisibilityOfElementOnPage(autoComplete);
        autoComplete.clear();
        autoComplete.sendKeys(value);
        waitForSpinner(driver);
        autoComplete.sendKeys(Keys.DOWN, Keys.RETURN);
    }

    public void cancel() {
        waitForSpinner();
        cancelAppointmentBtn.click();
    }
}
