# Recommendation engine for Openrice


This is an attempt in building a recommendation engine for Openrice (Yelp equivalent for Hong Kong restaurants).

This [Jupyter Notebook](./Openrice_Recommendation_script.ipynb) shows the rough steps on scraping the openrice website and building the recommendation engine.

Other [csv files](./assets/data) in this repository are the data files I scraped.

In general, I used SVD from Scipy to perform my recommendation engine.

I also added additional features where I adjust the recommendation engine to take into account region and restaurant types

Here's a brief [presentation](https://gitpitch.com/lyoelee/openrice_recommendator) I put together

p.s. Version 2.0 is ongoing...

Features include:
- separate .py files for different scraping steps
- storing outputs in zip files that is more efficient
- scrape MORE restaurants (from more regions & landmarks)
