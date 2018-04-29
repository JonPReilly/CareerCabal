
# Career Cabal

## Summary
Career Cabal is a job aggregation, search engine, and application tracking system design with the job hunter in mind.

The backend spiders scrape jobs from tech-centered job sites and place each [Job](https://github.com/JonPReilly/CareerCabal/blob/develop/career_cabal/apps/job/models.py) object into a database with things like title, company, city (as a geo-spatial object!), etc. A user can then search these jobs create [JobApplication](https://github.com/JonPReilly/CareerCabal/blob/develop/career_cabal/apps/jobApplication/models.py) objects and rapidly track and update their applications.

Career Cabal is a rewrite of [JobBard](https://github.com/JonPReilly/JobBard) (also written completely by me). JobBard also includes a [chrome extension](https://github.com/JonPReilly/JobBard/tree/master/Chrome%20Extension/JobBard) that automatically fills out job applications with the user's profile data.

## Technologies used

 1. [Django](https://www.djangoproject.com/) - User system and datbase object CRUD.
 2. [Django Rest Framework](https://www.django-rest-framework.org) - Connec5t Django/DB to React.js via REST API calls.
 3. [React.js](https://reactjs.org) - Front-end UI
 4. [PostgreSQL](https://www.postgresql.org/) + [PostGIS](http://postgis.net/) - Relational database with spatial extension for queries like "search for jobs within 5 miles of Boston"
 5. [Scrapy](https://scrapy.org/) - Scraping job applications
 6. [Selenium](https://www.seleniumhq.org/) - Scraping job applications from systems that require rendering javascript
## Installation and Running
### Installing
 1. Install backend dependencies
	 a. `pip install -r requirments.txt`
2. Install frontend dependencies
	a. `cd career_cabal/`
	b. `npm install`
### Running
1. Running the UI
	a. Run Django: `python career_cabal/manage.py runserver`
	b. Run Node.js: `node career_cabal/server.js`
2. Scraping
	a. `cd` into `job_scraping/job_scraping/spiders`
	b. `scrapy runspider <Spider.py file>` to scrape jobs into the DB

