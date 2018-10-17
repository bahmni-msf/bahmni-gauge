package org.bahmni.gauge.common.specs;

import com.thoughtworks.gauge.BeforeClassSteps;
import com.thoughtworks.gauge.Step;
import org.bahmni.gauge.common.printforms.PrintFormsPage;
import org.bahmni.gauge.common.BahmniPage;
import org.bahmni.gauge.common.DriverFactory;
import org.bahmni.gauge.common.PageFactory;
import org.bahmni.gauge.rest.BahmniRestClient;
import org.junit.Assert;

import java.util.Collections;
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

    @Step("Validate the skeleton of print view for <formName> form")
    public void verifySkeletonOfPrintView(String formName){

        PrintFormsPage printFormsPage = PageFactory.get(PrintFormsPage.class);
        Assert.assertTrue("Print Forms view is missing some basic entities",printFormsPage.validateSkeleton(formName));
    }

    @Step("Validate if form tab is selected by default")
    public void checkIfFormTabSelectedByDefault(){
        PrintFormsPage printFormsPage = PageFactory.get(PrintFormsPage.class);
        Assert.assertTrue("Form Tab is not enabled by default",printFormsPage.validateActiveTab("form"));
    }

    @Step("Click on Code Sheet")
    public void clickOnCodeSheet(){
        PrintFormsPage printFormsPage = PageFactory.get(PrintFormsPage.class);
        printFormsPage.clickOnCodeSheet();

    }

    @Step("Validate if Code Sheet tab is enabled")
    public void checkIfCodeSheetIsEnabled(){
        PrintFormsPage printFormsPage = PageFactory.get(PrintFormsPage.class);
        Assert.assertTrue("Code Sheet is not enabled",printFormsPage.validateActiveTab("codeSheet"));

    }

    @Step("Validate the title of the code sheet for form <formName>")
    public void checkCodeSheetTitle(String formName){
        PrintFormsPage printFormsPage = PageFactory.get(PrintFormsPage.class);
        Assert.assertTrue("Title of codesheet is wrong",printFormsPage.checkTitleOfCodeSheet(formName));

    }


    private boolean validateFormsDisplayed(List<String> actualForms){

        List<String> expectedForms =  BahmniRestClient.get().getAllObservationTemplates();
        Collections.sort(expectedForms);
        Collections.sort(actualForms);
        return expectedForms.equals(actualForms);
    }
}
