package org.bahmni.gauge.amman.specs;

import com.thoughtworks.gauge.BeforeClassSteps;
import com.thoughtworks.gauge.Step;
import org.bahmni.gauge.amman.printforms.PrintFormsPage;
import org.bahmni.gauge.common.BahmniPage;
import org.bahmni.gauge.common.DriverFactory;
import org.bahmni.gauge.common.PageFactory;
import org.bahmni.gauge.rest.BahmniRestClient;
import org.junit.Assert;

import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class PrintFormsSpec {

    @BeforeClassSteps
    public void waitForAppReady() {
        BahmniPage.waitForSpinner(DriverFactory.getDriver());
    }

    @Step("Validate if forms are listed in left hand side menu")
    public void verifyIfFormsAreListed() {
        PrintFormsPage printFormsPage = PageFactory.get(PrintFormsPage.class);
        Assert.assertTrue(validateFormsDisplayed(printFormsPage.getListofFormsDisplayed()));

    }

    private boolean validateFormsDisplayed(List<String> actualForms){

        List<String> expectedForms =  BahmniRestClient.get().getAllObservationTemplates();
        Collections.sort(expectedForms);
        Collections.sort(actualForms);
        return expectedForms.equals(actualForms);
    }
}
