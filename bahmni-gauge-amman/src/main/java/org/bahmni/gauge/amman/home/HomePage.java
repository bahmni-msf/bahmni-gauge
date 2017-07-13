package org.bahmni.gauge.amman.home;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;

/**
 * Created by jaseenam on 4/28/17.
 */
public class HomePage extends org.bahmni.gauge.common.home.HomePage {

    @FindBy(how = How.ID, using = "bahmni.ipd")
    public WebElement bedManagement;

    @FindBy(how = How.ID, using = "bahmni.ot")
    public WebElement operationTheatre;

    @FindBy(how = How.ID, using = "bahmni.patient.document.upload")
    public WebElement IDDocUpload;

    public void clickBedManagementApp() {
        bedManagement.click();
    }

    public void clickOperationTheatreApp() {
        operationTheatre.click();
    }

    public void clickIDDocUploadApp() {
        IDDocUpload.click();
    }
}
