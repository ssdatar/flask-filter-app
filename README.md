# San Francisco Restaurant Inspections
I am using the [San Francisco restaurant inspections data](https://data.sfgov.org/Health-and-Social-Services/Food-Inspections-LIVES-Standard/pyih-qa8i) found on the open data portal to build my Flask web app. The app allows people to explore inspection scores of restaurants and see what violations their favorite restaurants have been pulled up for.

## Filter options
I will allow people to filter by risk category, various levels of inspection scores (>90, 80-90, 70-80, 60-70, 50-60, <60), and name of restaurant. The main page will also have a map that is color coded by risk levels.

## Listing view
This will contain a table of every inspection the restaurant(s) requested by the user has had. Each row in the table in the listing will link to the detail about that inspection.

## Detail view
This will contain the date of inspection, the type of inspection, and what problems were found in the restaurant. I also plan to make calls to the Yelp API to show the Yelp rating for the chosen restaurant.

## Inspirations
* New York Times' take on [health inspection of NYC restaurants](http://www.nytimes.com/interactive/dining/new-york-health-department-restaurant-ratings-map.html)
* ProPublica's [Debt By Degrees](https://projects.propublica.org/colleges/)
* ProPublica's [Non-profit explorer](https://projects.propublica.org/nonprofits/)


