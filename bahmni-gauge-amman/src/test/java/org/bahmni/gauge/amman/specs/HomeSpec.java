package org.bahmni.gauge.amman.specs;

import com.thoughtworks.gauge.Step;
import org.bahmni.gauge.amman.home.HomePage;
import org.bahmni.gauge.common.BahmniPage;
import org.bahmni.gauge.common.DriverFactory;
import org.bahmni.gauge.common.PageFactory;

/**
 * Created by jaseenam on 5/1/17.
 */
public class HomeSpec {

    public void waitForAppReady() {
        BahmniPage.waitForSpinner(DriverFactory.getDriver());
    }

    @Step("Click on bed management app")
    public void goToBedManagementPage() {
        HomePage homePage = PageFactory.get(HomePage.class);
        waitForAppReady();
        homePage.clickBedManagementApp();
        waitForAppReady();
    }
}
