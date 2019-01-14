package org.bahmni.gauge.common.clinical.domain;

import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import org.bahmni.gauge.common.FormElement;
import org.bahmni.gauge.common.TestSpecException;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;

import java.util.*;

import static org.bahmni.gauge.common.BahmniPage.hasChild;

public class ObservationForm {

    private List<WebElement> observationNodes;
    private Map<String, String> data = new HashMap<>();

    public Map<String, String> getData() {
        return data;
    }


    public ObservationForm(WebElement observationForm) {
        observationNodes = observationForm.findElements(By.cssSelector(".leaf-observation-node"));
    }

    public ObservationForm() {
        observationNodes = null;
    }


    public void fillUp(Table table) {
        enter(table, observationNodes);
    }

    public void enterUp(Table table, WebElement element) {
        List<WebElement> elementList = element.findElements(By.cssSelector(".form-builder-row"));
        elementList = filterElementList(elementList);
        enter(table, elementList);
    }

    public void enterUpAll(Table table, WebElement element) {
        List<WebElement> elementList = element.findElements(By.cssSelector(".form-builder-row"));
        elementList = filterElementList(elementList);
        enterHideLabel(table, elementList);
    }

    public void enterUpAllAddMore(Table table, WebElement element, String obs) {
        List<WebElement> elementList = element.findElements(By.cssSelector(".form-builder-row"));
        elementList = filterElementListExceptAddMore(elementList,obs);
        enterHideLabel(table, elementList);
    }

    public Map<String,String> getObsValueHideLabel(WebElement element,String obs){

        List<WebElement> elementList = element.findElements(By.cssSelector(".form-builder-row"));
        elementList = filterElementListExceptAddMore(elementList,obs);
        Map<String,String> obsValues= getValues(elementList);
        return obsValues;
    }

    public Map<String,String>  getObsValue(WebElement element) {

       List<WebElement> elementList = element.findElements(By.cssSelector(".form-builder-row"));
        elementList = filterElementList(elementList);
        Map<String,String> obsValues= getValues(elementList);
        return obsValues;
    }


    private List<WebElement> filterElementList(List<WebElement> elementList) {
        List<WebElement> listClone = new ArrayList<>(elementList);
        for(WebElement element : listClone) {
            if(element.findElements(By.cssSelector("label")).size() > 1 || hasChild(element,By.cssSelector(".table-header"))) {
                elementList.remove(element);
            }
        }
        return elementList;
    }

    private List<WebElement> filterElementListExceptAddMore(List<WebElement> elementList, String obs) {
        List<WebElement> listClone = new ArrayList<>(elementList);
        for(WebElement element : listClone) {

            List<WebElement> childElements= element.findElements(By.cssSelector("label"));

            if(childElements.size() > 1) {
                for (WebElement e : childElements
                ) {
                    if(!e.getText().equalsIgnoreCase(obs))
                        elementList.remove(element);
                }

            }
            if (hasChild(element,By.cssSelector(".table-header")))
                elementList.remove(element);
        }
        return elementList;
    }

    private void enter(Table table, List<WebElement> elementList) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        if (rows.size() != 1) {
            throw new TestSpecException("Only one patient should be provided in the table");
        }
        TableRow row = rows.get(0);
        for (String label : columnNames) {
            String value = row.getCell(label);

            for (WebElement fieldset : elementList) {
                if (hasField(fieldset, label)) {
                    if (value.contains(":")) {
                        // This fills the form label which has combination of element type
                        // Issue: fills data for label which has similar partial text
                        String values[] = value.split(":");

                        List<FormElement> elements = getAllFieldType(fieldset);
                        int fieldCount = 0;
                        for (String val : values) {
                            if (val.equals(" ")) { // Skips if the empty value is provided
                                fieldCount++;
                                continue;
                            }
                            elements.get(fieldCount).fillUp(fieldset, val);
                            if (values.length == elements.size())
                                fieldCount++;
                                // This case failed in case of gynecology template, with has two sections of buttons
                            else {
                                break;
                            }
                        }

                    } else {
                        getFieldType(fieldset).fillUp(fieldset, value);
                        data.put(label, value);
                    }
                }
            }
        }
    }


    private static FormElement getFieldType(WebElement fieldset) {
        for (FormElement type : FormElement.allTypes) {
            if (hasChild(fieldset, type.getSelector())) {
                return type;
            }
        }

        return FormElement.UNKNOWN;
    }

    private static List<FormElement> getAllFieldType(WebElement fieldset) {
        return getAllFieldType(fieldset, 1);
    }

    private static List<FormElement> getAllFieldType(WebElement fieldset, int multipleLoopNum) {
        ArrayList<FormElement> types = new ArrayList<>();

        for (int i = 0; i < multipleLoopNum; i ++) {
            for (FormElement type : FormElement.allTypes) {
                if (hasChild(fieldset, type.getSelector())) {
                    types.add(type);
                }
            }
        }

        if (types.size() == 0)
            types.add(FormElement.UNKNOWN);
        return types;
    }

    private static boolean hasField(WebElement fieldset, String fieldName) {
        return fieldset.findElement(By.tagName("label")).getText().contains(fieldName);
    }

    /**
     *
     * @param table
     * @param elementList
     *
     * Fills the form with given data passed as  @param table in the form webElements.
     * Number of columns present in the table should be same as number of elements to fill in the form, as values are entered in the order of web elements present in form.
     *
     * Types of WebElements currently supported are:
     *
     *  INPUT, TEXT_AREA, SELECT, BUTTON, DIV_SELECT_SINGLE
     *
     * AddMore is supported for INPUT & TEXT_AREA.
     *
     * Pass the values ": :" separated for AddMore. For Example, if WEIGHT obs has addMore, in spec pass value as below
     *
     *  |WEIGHT|
     *  |40: :50|
     *
     *  Pass the values ":" separated for Notes. For Example, if WEIGHT obs has Notes, in spec pass value as below
     *
     *  |WEIGHT|
     *  |40:notes|
     */
    private void enterHideLabel(Table table, List<WebElement> elementList){
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

       //Only one patient data is expected to be passed
        if (rows.size() != 1) {
            throw new TestSpecException("Only one patient should be provided in the table");
        }
        TableRow row = rows.get(0);

        for (String label : columnNames) {
            String value = row.getCell(label);
            if(elementList.size() >= 1){
                for (WebElement fieldset : elementList) {

                    //checks is to support Notes and AddMore
                    if(value.contains(":")){
                        String values[] = value.split(":");

                        //Gets the types of webelements inside the row element - useful when we have multiple (2 in below case)
                        //elements inside same formbuilder-row. For example Note, AddMore
                        List<FormElement> elements = getAllFieldType(fieldset, 2);
                        int num = 0;
                        for (String val : values) {
                            if(val.equals(" ")){
                                num++;
                                continue;
                            }

                            elements.get(num).fillUp(fieldset, val);
                            num++;
                        }
                    } else {
                        getFieldType(fieldset).fillUp(fieldset, value);
                    }

                    data.put(label, value);
                    elementList.remove(0);
                    break;
                }
            }
        }
    }


    public Map<String,String> getValues(List<WebElement> elementList){

        Map<String,String> obsValues = new LinkedHashMap<>();
        Map<String,Integer> labelCounter= new HashMap<>();

        for (WebElement fieldset : elementList) {
            Map<String, String> temp = getFieldType(fieldset).getValue(fieldset);
            temp.forEach((k, v) -> {

                if(labelCounter.containsKey(k)){
                    labelCounter.put(k, labelCounter.get(k)+1);

                }
                else
                    labelCounter.put(k,0);

                if (obsValues.containsKey(k)){
                    obsValues.put(k+"_"+labelCounter.get(k).toString(),v);
                }
                else
                    obsValues.put(k,v);

            }
            );

        }
       return  obsValues;
    }

}
