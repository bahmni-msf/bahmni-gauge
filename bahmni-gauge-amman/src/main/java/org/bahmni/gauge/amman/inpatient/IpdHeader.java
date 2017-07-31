package org.bahmni.gauge.amman.inpatient;

import org.bahmni.gauge.common.BahmniPage;
import org.bahmni.gauge.common.inpatient.InpatientHeader;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;

public class IpdHeader extends InpatientHeader{
    @FindBy(how = How.CSS, using = ".bed-management-nav li:nth-child(1)")
    public WebElement admitTab;

    @FindBy(how = How.CSS, using = ".bed-management-nav li:nth-child(2)")
    public WebElement bedManagementTab;

    public void goToAdmitTab() {

        admitTab.click();
    }

    public void goToBedManagementTab() {

        bedManagementTab.click();
    }

}
