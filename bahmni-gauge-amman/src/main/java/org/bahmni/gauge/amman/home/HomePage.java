package org.bahmni.gauge.amman.home;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;

/**
 * Created by jaseenam on 4/28/17.
 */
public class HomePage extends org.bahmni.gauge.common.home.HomePage{

    @FindBy(how= How.ID, using = "bahmni.ipd")
    public WebElement bedManagement;

    public void clickBedManagementApp() {
        bedManagement.click();
    }
}
