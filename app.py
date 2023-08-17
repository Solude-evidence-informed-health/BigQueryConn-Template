from database.bigqueryconn import BigQueryConn

PATH_CREDENTIALS = "./config/solude_big_query_service.json"
PATH_QUERIES = "./queries/"
PATH_DATA = "./database/data/raw/"

bqconn = BigQueryConn(PATH_CREDENTIALS)

query_filename = "amostras_resistracker.txt" # TODO: Adicionar nome do arquivo de query
path_query = PATH_QUERIES + query_filename

def get_and_save_data():
    try:
        df_sample = bqconn.get_data_df(path_query)
        df_sample.to_csv(PATH_DATA + query_filename[0:-4] + ".csv", index=False)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    get_and_save_data()