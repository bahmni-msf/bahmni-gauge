package org.bahmni.gauge.amman.AppointmentScheduling;

import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import org.openqa.selenium.By;
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
    @FindBy(how = How.LINK_TEXT, using = "Appointments List")
    WebElement appointmentsList;

    @FindBy(how = How.LINK_TEXT, using = "Add new appointment")
    WebElement addAppointmentBtn;

    @FindBy(how = How.CSS, using = ".app-today-btn")
    WebElement todayBtn;
    @FindBy(how = How.LINK_TEXT, using = "List view")
    WebElement listViewBtn;

    @FindBy(how = How.LINK_TEXT, using = "Calendar")
    WebElement calendarViewBtn;

    @FindBy(how = How.CSS, using = "#patientID")
    WebElement patientIDorName;

    @FindBy(how = How.CSS, using = "#speciality")
    WebElement speciality;

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

    @FindBy(how = How.CLASS_NAME, using = "walk-in-app")
    WebElement walkInAppCheckbox;

    @FindBy(how = How.CSS, using = "#notes")
    WebElement notes;

    @FindBy(how = How.CSS, using = ".create-new-app-container")
    WebElement addAppointmentSlider;

    @FindBy(how = How.XPATH, using = "//*[@id=\"create-appointment-form\"]/button")
    WebElement saveAppointmentBtn;


    public void clickAddNewAppointment() {
        //waitForElementOnPage(addAppointmentBtn);
        addAppointmentBtn.click();
        //waitForElement(driver, ExpectedConditions.visibilityOf(addAppointmentSlider));
    }

    public void addNewAppointment(Table table, List<String> colNames) {
        List<TableRow> services = table.getTableRows();
        TableRow service = services.get(0);

        for (String cellname : colNames) {
            String cellVal = service.getCell(cellname);
            switch (cellname) {
                case "Patient":
                    patientIDorName.clear();
                    fillAutocomplete(patientIDorName, cellVal);
                    break;
                case "Speciality":
                    new Select(speciality).selectByVisibleText(cellVal);
                    break;
                case "Service":
                    new Select(serviceName).selectByVisibleText(cellVal);
                    break;
                case "Service App. Type":
                    new Select(serviceType).selectByVisibleText(cellVal);
                    break;
                case "Location":
                    new Select(location).selectByVisibleText(cellVal);
                    break;
                case "Provider":
                    new Select(provider).selectByVisibleText(cellVal);
                    break;

                case "Date":
                    if (cellVal.contains("NOW")) {
                        cellVal = todayDateAsString();
                    }
                    appointmentDate.sendKeys(cellVal);
                    break;

                case "Start Time":
                    startTime.sendKeys(cellVal);
                    break;

                case "End Time":
                    endTime.sendKeys(cellVal);
                    break;
                case "Walk-in Appointment":
                    if (cellVal.equalsIgnoreCase("Yes")) {
                        walkInAppCheckbox.click();
                    }
                    break;
                case "Notes":
                    notes.clear();
                    notes.sendKeys(cellVal);
                    break;
            }
        }
        saveAppointmentBtn.click();
//        waitForElement(driver, ExpectedConditions.invisibilityOfElementLocated(By.className("create-new-app-container")));
        waitForSpinner(driver);
    }

    private String todayDateAsString() {
        DateFormat dateFormat = new SimpleDateFormat("MM-dd-yyyy");
        Date today = new Date();
        return dateFormat.format(today);
    }


    public void fillAutocomplete(WebElement autoComplete, String value) {
        autoComplete.sendKeys(value);
        List<WebElement> patientSearchResults = driver.findElements(By.className("ui-corner-all"));
//        waitForElement(driver, ExpectedConditions.visibilityOfAllElements(patientSearchResults));
        waitForSpinner(driver);
        autoComplete.sendKeys(Keys.DOWN, Keys.RETURN);
    }

    public void clickCalendarView() {
        calendarViewBtn.click();
    }

    public void clickListView() {
        listViewBtn.click();
    }

    public void clickToday() {
        todayBtn.click();
    }

    public void clickAppointmentsList() {
        appointmentsList.click();
    }
}
