# File Scraper

This project contains a Python script that scrapes all files from specified folders and subfolders and stores their contents in a single output file.

## Defining Paths

Paths for the file scraper are defined in the `paths.yml` file. This file should contain a list of directories to be scraped. Below is an example of how to define paths in `paths.yml`:

```yaml
paths:
  - /path/to/your/project/src
  - /path/to/your/project/config
  - /another/path/to/include
  - /yet/another/path/to/include

