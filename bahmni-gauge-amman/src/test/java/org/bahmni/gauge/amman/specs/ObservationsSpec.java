package org.bahmni.gauge.amman.specs;


import com.thoughtworks.gauge.BeforeClassSteps;
import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.Table;
import org.bahmni.gauge.amman.clinical.ObservationsPage;
import org.bahmni.gauge.common.BahmniPage;
import org.bahmni.gauge.common.DriverFactory;
import org.bahmni.gauge.common.PageFactory;

public class ObservationsSpec {
    @BeforeClassSteps
    public void waitForAppReady() {
        BahmniPage.waitForSpinner(DriverFactory.getDriver());
    }

    @Step("Select template <template> from observation page and fill details <table>")
    public void selectTemplateAndFillData(String template, Table table) {
        ObservationsPage observationsPage = PageFactory.get(ObservationsPage.class);
        observationsPage.selectTemplate(template);
        waitForAppReady();
        observationsPage.fillTemplateData(table);
    }

    @Step("Select template <template> from observation page and verify details <table>")
    public void selectTemplateAndVerifyData(String template, Table table) {
        ObservationsPage observationsPage = PageFactory.get(ObservationsPage.class);
        observationsPage.selectTemplate(template);
        waitForAppReady();
        observationsPage.verifyTemplateData(table);
    }

    @Step({"Select template <template> from observation page and fill details in <sectionName> section <table>", "Select template <template> from observation page and edit details in <sectionName> section <table>"})
    public void selectTemplateSectionAndFillData(String template, String section, Table table) {
        ObservationsPage observationsPage = PageFactory.get(ObservationsPage.class);
        observationsPage.selectTemplate(template);
        waitForAppReady();
        observationsPage.fillTemplateData(table, section);
    }

    @Step("Select template <template> from observation page and verify details in <sectionName> section <table>")
    public void selectTemplateSectionAndVerifyData(String template, String section, Table table) {
        ObservationsPage observationsPage = PageFactory.get(ObservationsPage.class);
        observationsPage.selectTemplate(template);
        waitForAppReady();
        observationsPage.verifyTemplateData(table, section);
    }

    @Step("Verify these forms are saved and disabled to add <table>")
    public void verifyFormsSavedAndDisabledToAdd(Table table) {
        ObservationsPage observationsPage = PageFactory.get(ObservationsPage.class);
        observationsPage.verifyFormSaved(table);

    }

    @Step("Verify this form is Add More form <template>")
    public void verifyFormsSavedAndAddMore(String template) {
        ObservationsPage observationsPage = PageFactory.get(ObservationsPage.class);
        observationsPage.verifyFormIsAddMore(template);
    }

    @Step("Select template <template> from the Observation Page")
    public void selectTemplate(String template) {
        ObservationsPage observationsPage = PageFactory.get(ObservationsPage.class);
        observationsPage.selectTemplate(template);
        waitForAppReady();
    }
}
