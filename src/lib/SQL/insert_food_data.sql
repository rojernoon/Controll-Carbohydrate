/*
CSVデータを一括でDBに格納する
*/
COPY FOOD(FoodName,AmountOfCarbohydrate)
FROM
'C:\dev\Controll-Carbohydrate\src\data\food_data.csv'
WITH csv;