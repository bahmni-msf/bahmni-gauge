package org.bahmni.gauge.amman.OTScheduling;

import org.bahmni.gauge.amman.home.HomePage;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;

/**
 * Created by jaseenam on 20/07/17.
 */
public class otHomePage extends HomePage {
    @FindBy(how = How.CSS, using = ".ot-scheduling-nav li:nth-child(1)")
    WebElement surgicalQueues;

    @FindBy(how = How.CSS, using = ".ot-scheduling-nav li:nth-child(2)")
    WebElement OTScheduling;

    public void goToSurgicalQueues() {
        surgicalQueues.click();
    }

    public void goToOTScheduling() {
        OTScheduling.click();
    }
}
