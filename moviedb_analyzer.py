#-#!/usr/bin/env python3
from src.facade import Facade

def main():
    
    # Init and load file
    
    INPUT_PATH = "resources/movies_metadata.csv"
    INPUT_TYPE = 'csv'
    
    facade = Facade(input_type=INPUT_TYPE, 
                    input_path=INPUT_PATH)

    # Analyze
    facade.logger.info(f"Unique movies: {facade.count_unique_rows(['imdb_id', 'original_title'])}")

    facade.logger.info(f"Average ratings of all movies: {facade.find_average('vote_average')}")

    facade.logger.info(f"Top 5 highest rated movies: {facade.find_top(sort_column='vote_average', top=5, return_column='original_title')}")
    
    facade.logger.info(f"Movies released each year: {facade.movies_by_year('release_date')}")
    
    facade.logger.info(f"Movies released in each genre: {facade.movies_by_genre('genres')}")

    # Save as JSON
    
    OUTPUT_PATH = "resources/movies_metadata.json"
    OUTPUT_TYPE = 'json'
    
    facade.save_as(output_type=OUTPUT_TYPE,
                   output_path=OUTPUT_PATH)


if __name__ == "__main__":

    main()
