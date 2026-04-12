USE sakila;
/*
a) The actor table includes the actor_id, first_name, last_name, and the last_update timestamp.
b) The film table includes information like film_id, title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features, and last_update.
c) The film_actor table contains both the actor_id and the film_id columns.
d) The rental table includes rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, and last_update. This information is hard to read because it uses ID numbers instead of names for customers and movies.
e) The inventory table includes inventory_id, film_id, store_id, and last_update, which maps specific copies of films to specific store locations.
f) To find film names rented on a specific date, I need to use the rental, inventory, and film tables. The rental table provides the date, the inventory table links the rental to a specific film_id, and the film table provides the actual name of that film.
 */
 
 SELECT rental_date,inventory_id FROM rental;
 SELECT inventory_id,film_id FROM inventory;
 SELECT film_id, title FROM film;
 