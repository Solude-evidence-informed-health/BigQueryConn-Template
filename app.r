library(bigrquery)
library(jsonlite)

read_credentials <- function(credential_path) {
  creds <- fromJSON(credential_path)
  return(creds)
}

query_bigquery <- function(credential_path, query_path) {
  # Read credentials
  creds <- read_credentials(credential_path)
  
  # Authenticate with BigQuery
  bq_auth(path = creds)

  # Read the query from file
  query <- readLines(query_path, warn = FALSE)

  # Run the query
  result <- bq_project_query(query)

  # Convert the result to a dataframe
  df <- bq_table_download(result[[1]])
  
  return(df)
}

credential_path <- "./config/__________.json"
query_path <- "./queries/_______"

result_df <- query_bigquery(credential_path, query_path)

output_path <- "/database/data/raw/____________.csv"

write.csv(result_df, file = output_path, row.names = FALSE)
