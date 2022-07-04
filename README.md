# Scraping BBC news with BeautifulSoup, Mongo DB and FastAPI

## Purpose
This quickstart project is a POC (proof of concept) to scrape new data from BBC webstite using Python, BeautifulSoup as a scraping tool, Mongo DB as a database and FastAPI to expose results via API

## Limitations and imporovement points
* This application uses BeautifulSoup as a scraping library, fast to implement but has limited scraping features compared to scrapy which is a complete framework.
* The main limitation with htis scraping approach is that, we need to specify classes and divs Ids to scrape after manually inspecting the webpage elements.
* This is an MVP (Minimum Viable Product) that aims to implement needed features fast. Personnally, my webscraping experience is basic, so I think there is room to improve the scraping by implementing a feature that autaumatically detects classes and divs identifiers to be scraped.  

## Production deployment
* This application could be deployed via docker, CICD pipeline using jenkins and Kubernetes as a container app 
* This application is weel suited to be integrated inside an Apache Airflow DAG that can be used as a second layer of ETL and mainly as a scheduler to be triggered on daily basis or some other interval. We can set up a frequency for the batch.
* For the time being the application deals mainly with static articles for which we need HTML/ CSS classes IDs. If it comes to upgrade, we can think of a scraping loop that generates a stream of scraped data. In this case a Kafka message broker would be a good idea as a layer.
* If we choose to go with a kafka message broker approach, it would be interesting and recommandable to use a schema registry as a tool of serialization / deserialization to ensure data structure coherence. 
* The prodicer sends the consumer schema to the schema registry and the schema registry saves it, and generates a schema ID then sends back the ID to the producer and the latter caches it.
* Avro Schema regisrty is widely used and compatitible with many programming languages and in our case Python. It is close to JSON and dynamic.
