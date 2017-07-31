package org.bahmni.gauge.amman.specs;

import com.thoughtworks.gauge.BeforeClassSteps;
import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.Table;
import org.bahmni.gauge.amman.IDDoc.IDDocUploadPage;
import org.bahmni.gauge.common.PageFactory;
import org.bahmni.gauge.common.radiology.RadiologyUploadPage;

public class IDDocUploadPageSpec {
    private IDDocUploadPage IDdocUploadPage;

    public IDDocUploadPageSpec() {
        IDdocUploadPage = PageFactory.get(IDDocUploadPage.class);
    }

    public void waitForAppReady() {
        IDdocUploadPage.waitForSpinner();
    }

    @Step("Upload following documents in visit <visitNumber> <table>")
    public void uploadImage(int visitNumber, Table table) {
        IDdocUploadPage.uploadImage(visitNumber, table);
    }

    @Step("Save ID Doc upload")
    public void save() {
        waitForAppReady();
        IDdocUploadPage.save();
    }
}
