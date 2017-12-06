package org.bahmni.gauge.amman.AppointmentScheduling;

import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;

import java.util.List;

/**
 * Created by jaseenam on 07/08/17.
 */
public class servicePage extends appointmentSchedulingAdminPage {
    @FindBy(how = How.ID, using = "name")
    WebElement serviceName;

    @FindBy(how = How.ID, using = "description")
    WebElement serviceDescription;

    @FindBy(how = How.ID, using = "duration")
    WebElement serviceDuration;

    @FindBy(how = How.ID, using = "start-time")
    WebElement serviceStartTime;

    @FindBy(how = How.ID, using = "end-time")
    WebElement serviceEndTime;

    @FindBy(how = How.ID, using = "max-load")
    WebElement serviceMaxLoad;

    @FindBy(how = How.ID, using = "location")
    WebElement serviceLocation;

    @FindBy(how = How.CSS, using = ".service-save-btn")
    WebElement saveServiceBtn;

    @FindBy(how = How.ID, using = "ok")
    WebElement saveEditServiceBtn;

    @FindBy(how = How.CLASS_NAME, using = "caution")
    WebElement cautionService;

    @FindBy(how = How.CSS, using = ".show-btn.fr")
    WebElement errorOkBtn;

    public String changeTimeFormat(String serviceTime) {
        serviceTime = serviceTime.replace(":", "");
        serviceTime = serviceTime.replace(" ", "");
        return serviceTime;
    }

    public void clickSaveServiceBtn() {
        saveServiceBtn.click();
    }

    public void addService(Table table, List<String>  colNames) {
        List<TableRow> services = table.getTableRows();
        TableRow service = services.get(0);

       for (String cellname: colNames){
           String cellVal = service.getCell(cellname);
            switch (cellname) {
                case "Service Name":
                    serviceName.clear();
                    serviceName.sendKeys(cellVal);
                    break;
                case "Description":
                    serviceDescription.clear();
                    serviceDescription.sendKeys(cellVal);
                    break;
                case "Duration":
                    serviceDuration.clear();
                    serviceDuration.sendKeys(cellVal);
                    break;
                case "Start Time":
                    serviceStartTime.sendKeys(changeTimeFormat(cellVal));
                    break;
                case "End Time":
                    serviceEndTime.sendKeys(changeTimeFormat(cellVal));
                    break;
                case "Max Load":
                    serviceMaxLoad.clear();
                    serviceMaxLoad.sendKeys(cellVal);
                    break;
                case "Location":
                    new Select(serviceLocation).selectByVisibleText(cellVal);
                    break;
            }
        }
        clickSaveServiceBtn();
    }

    public String cautionServiceText() {
        return cautionService.getText();
    }

    public void confirmEditService() {
        waitForElement(driver, ExpectedConditions.visibilityOfElementLocated(By.cssSelector(".ngdialog-overlay")));
        saveEditServiceBtn.click();
        waitForElement(driver, ExpectedConditions.invisibilityOfElementLocated(By.cssSelector(".ngdialog-overlay")));
    }

    public String confirmSaveServiceError() {
        waitForElement(driver, ExpectedConditions.visibilityOfElementLocated(By.cssSelector(".error-message-container")));
        String serviceSaveError = driver.findElement(By.cssSelector(".error-message")).getText();
        errorOkBtn.click();
        waitForElement(driver, ExpectedConditions.invisibilityOfElementLocated(By.cssSelector(".message-container.error-message-container")));
        return serviceSaveError;
    }
}
