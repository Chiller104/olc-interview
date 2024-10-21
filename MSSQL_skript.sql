---------------------------------(1)

SELECT 
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    CONCAT(a.address, ', ', ci.city, ', ', co.country) AS complete_address
FROM 
    rental r
JOIN 
    customer c ON r.customer_id = c.customer_id
JOIN 
    address a ON c.address_id = a.address_id
JOIN 
    city ci ON a.city_id = ci.city_id
JOIN 
    country co ON ci.country_id = co.country_id
WHERE 
    r.rental_date > DATEADD(YEAR, -1, GETDATE());


---------------------------------(2)

SELECT 
    c.name AS category_name,
    COUNT(f.film_id) AS film_count
FROM 
    film f
JOIN 
    film_category fc ON f.film_id = fc.film_id
JOIN 
    category c ON fc.category_id = c.category_id
GROUP BY 
    c.name
ORDER BY 
    film_count DESC;


---------------------------------(3)

SELECT 
    c.first_name,
    c.last_name,
    f.title AS film_title,
    DATEDIFF(day, DATEADD(day, 14, r.rental_date), r.return_date) AS overdue_days,
    CASE 
        WHEN r.return_date > DATEADD(day, 14, r.rental_date) THEN 
            DATEDIFF(day, DATEADD(day, 14, r.rental_date), r.return_date) * 0.01 * f.rental_rate
        ELSE 0
    END AS fine
FROM 
    customer c
JOIN 
    rental r ON c.customer_id = r.customer_id
JOIN 
    inventory i ON r.inventory_id = i.inventory_id
JOIN 
    film f ON i.film_id = f.film_id
WHERE 
    r.return_date > DATEADD(day, 14, r.rental_date)
ORDER BY 
    fine DESC;


---------------------------------(4)

SELECT 
    s.store_id,
    st.first_name,
    st.last_name,
    YEAR(r.rental_date) AS rental_year,
    COUNT(r.rental_id) AS total_rentals
FROM 
    rental r
JOIN 
    inventory i ON r.inventory_id = i.inventory_id
JOIN 
    film f ON i.film_id = f.film_id
JOIN 
    store s ON i.store_id = s.store_id
JOIN 
    staff st ON r.staff_id = st.staff_id
GROUP BY 
    s.store_id, st.first_name, st.last_name, YEAR(r.rental_date)
ORDER BY 
    s.store_id, rental_year, st.last_name;


---------------------------------(5)

CREATE PROCEDURE AddNewFilm

    @title NVARCHAR(255),
    @description NVARCHAR(MAX),
    @release_year VARCHAR(4),
    @language_id INT,
    @rental_duration INT,
    @rental_rate DECIMAL(5,2),
    @length INT,
    @replacement_cost DECIMAL(10,2),
    @rating NVARCHAR(10),
    @special_features NVARCHAR(200),
    @store_id INT
AS
BEGIN
    BEGIN TRANSACTION;
	BEGIN TRY
	    INSERT INTO film (title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, special_features, rating)
        VALUES (@title, @description, @release_year, @language_id, @rental_duration, @rental_rate, @length, @replacement_cost, @special_features, @rating);
        
        DECLARE @film_id INT = SCOPE_IDENTITY();
        
        INSERT INTO inventory (film_id, store_id)
        VALUES (@film_id, @store_id);
        
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        ROLLBACK TRANSACTION;
        THROW;
    END CATCH
END;


/*-------------example insert

EXEC AddNewFilm 
    @title = 'Once Upon a Time in Hollywood', 
    @description = 'Comedy by Tarantino', 
    @release_year = 2019, 
    @language_id = 1, 
    @rental_duration = 17, 
    @rental_rate = 9.99, 
    @length = 161, 
    @replacement_cost = 48.00, 
    @rating = 'PG-13',
	@special_features = 'Behind the Scenes',
    @store_id = 2;