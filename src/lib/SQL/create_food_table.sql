DROP TABLE IF EXISTS FOOD;

CREATE TABLE FOOD (
	ID SERIAL,
	FoodName char(20) UNIQUE,
	AmountOfCarbohydrate numeric,
	AmountOfFood numeric
	);
