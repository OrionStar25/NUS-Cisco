# Installation

1. Create conda environment

```bash
$ conda env create -f cisco.yml
$ conda activate myenv
$ conda env list # Verfiy if installation is correct
```

2. Install `pip` packages:

```bash
$ pip install -r requirements.txt
```

```
conda activate cisco

<!-- conda list -e > requirements.txt save all the info about packages to your folder -->

conda env export > cisco.yml

pip list --format=freeze > requirements.txt
```

# Task 1

## Question: 

The following website lists all the categories and their corresponding products in Cisco. Construct a `Category-Product` tree visualization.

Link: https://www.cisco.com/c/en/us/support/all-products.html. 

## Solution:

### Folder Structure

- `categories.json`: Lists all category names and their URLs in `JSON` format.

- `categories_products.json`: List all category names and their corresponding product names in `JSON` formal.

- `edges_list.csv`: A `csv` file containing 2 columns - `source`, `target`.
    - `source` is the category name
    - `target` is the product name
    - a directed graph is formed from `source --> target`.

- `graph.html`: The graphic visualization for the `Category-Product` tree.

- `visualization.ipynb`: Code to visualize the directed graph.

- `web_scraper.py`: Code to scrape categories and products from the given link.


### Run Web Scraper

```python
$ python web_scraper.py
```

I scraped data from the `A-Z` section on the products page, and not `0-9` section for several reasons:

1. Initially looking at the structure, it seemed like the `A-Z` section was the superset of all products. Hence, scraping those products would essentially count for the `0-9` section too. 

2. I ran the whole project on a CPU I wanted to first experiment on a subset of data. Currently there are ~700 products. More products can be scraped easily.

In case, we wish to scrape the `0-9` section too, certain additions need to be made in `web_scraper.py`:

1. Scrape using `id=prodByNumber` for `PRODUCT_TYPE_A`.
2. Scrape using `id=numeric` for `PRODUCT_TYPE_B`.
3. Similar handling for other products.

These changes will only change the visualization, i.e., the resulting graph will have more leaf nodes (products). Additonally, the flow for Task 2 and 3 remain unchanged.

### Visualization

Rerun the notebook `visualization.ipynb` using `Jupyter Notebook` to generate the interactive graph within the notebook. You can zoom in infinitely to get category and product names. (estimated time ~30secs).

**Note:** The interactive graph doesn't generate on VSCode.

Alternatively, you can open `graph.html` using VSCode's live server extension.
```
- Right click on graph.html
- Open with Live Server
```


# Task 2

## Question: 

Gather 1000 documents corresponding to each individual product delineated under Task 1.

For example, in the `All Supported Products` section on the webpage https://www.cisco.com/c/en/us/support/switches/index.html, each enumerated product on this list can be used as a query. By querying this product name in the Cisco search engine https://search.cisco.com/search, you can retrieve the top 1000 documents relevant to that particular product.

## Solution:

### Folder Structure

- `products.txt`: List of all Cisco products.

- `request.txt`: The curl used for sending a POST request to the Cisco search engine.

- `sample_response.json`: Sample reponse of the POST request on the Cisco search engine using a query.

- `search.py`: Code to get 1000 documents for each `query=product_name` using the Cisco seearch engine.

- `products/`: A directory of all of Cisco products containing 1000 relevant documents each. These are generated using `search.py`. 
```
 - product_name_1
        - 1.txt
        - 2.txt
        ...
        - 1000.txt
    - product_name_2
        - 1.txt
        - 2.txt
        ...
```

### Retrieve Documents

```python
$ python search.py
```

I retrieve 1000 documents for each of the ~700 products in batches of 50 each. Therefore, in total I have ~700K documents.

The response JSON is parse to create a document containing:
```
- title
- description
- content
- concept
```


# Task 3

## Question: 

After amassing 1000 documents per product, construct an index on your own, thereby enabling the implementation of a search functionality. For example, given an arbitrary query, your algorithm is supposed to output the most relevant documents.

## Solution:

### Folder Structure

- `create_index.py`: Code to create a FAISS index of all the documents.

- `query_search.ipynb`: Notebook to perform query search using the index and retrieve results.

- `faiss_index.pkl`: Pickle file of the created index.

### Create index

**Note:** This step is extremely computation and resources heavy. 

```python
$ python create_index.py
```

### Perform Query Search

1. Run `query_search.ipynb`.
2. Change the value for `query`, `K` as required.
3. Documents are retrieved in descending order of relevancy, i.e., more relevant documents have a lower L2 distance score and thus, recommended first.


# References

1. https://realpython.com/beautiful-soup-web-scraper-python/
2. https://memgraph.com/blog/graph-visualization-in-python
3. https://python.langchain.com/docs/integrations/vectorstores/faiss