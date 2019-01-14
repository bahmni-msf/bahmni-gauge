package org.bahmni.gauge.util;

import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import org.apache.commons.beanutils.BeanUtils;

import java.util.*;

public class TableTransformer {

    public static <Model> Model asEntity(Table table, Class<Model> type){
        return asEntityList(table, type).get(0);
    }

    public static <Model> List<Model> asEntityList(Table table, Class<Model> type) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        List<Model> entities=new ArrayList<>();
        if(rows.size() == 0)
            throw new IllegalArgumentException("The table either contains 0 rows or multiple rows!!");
        for(TableRow row:rows) {
            Map<String, String> rowMap = new HashMap<>();

            for (String column : columnNames) {
                rowMap.put(column, fieldTransform(row.getCell(column)));
            }

            try {
                Model obj = type.newInstance();
                BeanUtils.populate(obj, rowMap);

                entities.add(obj);
            } catch (Exception e) {
                throw new IllegalArgumentException("Unable to instantiate the object of the provided class");
            }
        }
        return entities;
    }

    public static String fieldTransform(String fieldValue){
        Random rnd=new Random();
        if(fieldValue.contains("#")) {
            StringBuilder sb = new StringBuilder(fieldValue);
            for(int i=0;i<sb.length();i++){
                if(sb.charAt(i)=='#')
                    sb.setCharAt(i,(char)(rnd.nextInt(9)+'0'));
            }
            fieldValue=sb.toString();
        }
        return fieldValue;
    }

    public static void updateEntityProperty(Object entity,String column,String value){

        try {
            BeanUtils.setProperty(entity,column,fieldTransform(value));

        }  catch (Exception e) {
            throw new IllegalArgumentException("Unable to instantiate the object of the provided class");
        }

    }

    //Use this method to get a two column table as LinkedHashMap
    public static Map<String,String> getTableAsMap(Table table){

        Map<String,String> data = new LinkedHashMap<>();

        for (TableRow tr: table.getTableRows()) {

            data.put(tr.getCellValues().get(0),tr.getCellValues().get(1));
        }
        return data;
    }

}
