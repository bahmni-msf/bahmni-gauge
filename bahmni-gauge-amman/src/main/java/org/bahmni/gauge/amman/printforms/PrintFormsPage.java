package org.bahmni.gauge.amman.printforms;

import com.thoughtworks.gauge.BeforeClassSteps;
import com.thoughtworks.gauge.Gauge;
import org.apache.commons.lang.StringUtils;
import org.bahmni.gauge.common.BahmniPage;
import org.bahmni.gauge.rest.BahmniRestClient;
import org.bahmni.gauge.util.StringUtil;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

import java.util.LinkedList;
import java.util.List;

public class PrintFormsPage extends BahmniPage{

    @FindBy(xpath = "//li//a[@class=\"conceptName\"]")
    private List<WebElement> listofFormsAvaiable;

    public List<String> getListofFormsDisplayed(){

        List<String> actualForms = new LinkedList<>();

        Gauge.writeMessage("Actual Forms Available :");

        for (WebElement form : listofFormsAvaiable){

            actualForms.add(form.getText());
            Gauge.writeMessage(form.getText());
        }

        return actualForms;
    }



}
