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

//    @Step("Click on bed management app")
//    public void goToBedManagementPage() {
//        HomePage homePage = PageFactory.get(HomePage.class);
//        waitForAppReady();
//        homePage.clickBedManagementApp();
//        waitForAppReady();
//    }
//
//    @Step("Click on operation theatre app")
//    public void goToOperationTheatrePage() {
//        HomePage homePage = PageFactory.get(HomePage.class);
//        waitForAppReady();
//        homePage.clickOperationTheatreApp();
//        waitForAppReady();
//    }

    @Step("Click on <module> module")
    public void goToAppPage(String module) {
        HomePage homePage = PageFactory.get(HomePage.class);
        waitForAppReady();
        switch (module) {
            case "bed management":
                homePage.clickBedManagementApp();
                break;

            case "operation theatre":
                homePage.clickOperationTheatreApp();
                break;

            case "ID doc upload":
                homePage.clickIDDocUploadApp();
                break;
        }
        waitForAppReady();
    }
}
